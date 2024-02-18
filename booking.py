import sqlite3

class BookingManager:
    """
    Clasa BookingManager gestionează rezervările pentru spectacole.
    """

    def __init__(self, db_name):
        """
        Inițializarea conexiunii cu baza de date.
        
        Args:
            db_name (str): Numele fișierului bazei de date SQLite.
        """
        try:
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print("Eroare la conectarea la baza de date:", e)

    def reserve_ticket(self, show_id, nume_utilizator, email):
        """
        Rezervă un bilet pentru un spectacol.

        Args:
            show_id (int): ID-ul spectacolului.
            nume_utilizator (str): Numele utilizatorului care face rezervarea.
            email (str): Adresa de email a utilizatorului.

        Raises:
            sqlite3.Error: O eroare care apare în timpul executării operațiilor cu baza de date.
        """
        try:
            self.cursor.execute("BEGIN")
            locuri_disponibile = self.cursor.execute("SELECT locuri_disponibile FROM spectacole WHERE id=?", (show_id,)).fetchone()[0]
            if locuri_disponibile <= 0:
                print("Ne pare rău, nu mai sunt locuri disponibile pentru acest spectacol.")
                return
            self.cursor.execute("INSERT INTO rezervari (show_id, nume_utilizator, email) VALUES (?, ?, ?)", (show_id, nume_utilizator, email))
            self.cursor.execute("UPDATE spectacole SET locuri_disponibile = locuri_disponibile - 1 WHERE id=?", (show_id,))
            print("Biletul a fost rezervat cu succes!")
        except sqlite3.Error as e:
            print("Eroare la rezervare:", e)
            self.conn.rollback()
        else:
            self.conn.commit()

    def cancel_reservation(self, email):
        """
        Anulează o rezervare existentă pe baza adresei de email.

        Args:
            email (str): Adresa de email a utilizatorului pentru care se anulează rezervarea.

        Raises:
            sqlite3.Error: O eroare care apare în timpul executării operațiilor cu baza de date.
        """
        try:
            self.cursor.execute("BEGIN")
            rezervare = self.cursor.execute("SELECT * FROM rezervari WHERE email=?", (email,)).fetchone()
            if rezervare is None:
                print("Nu există o rezervare activă asociată cu acest email.")
                return
            show_id = rezervare[1]
            self.cursor.execute("DELETE FROM rezervari WHERE email=?", (email,))
            self.cursor.execute("UPDATE spectacole SET locuri_disponibile = locuri_disponibile + 1 WHERE id=?", (show_id,))
            print("Rezervarea a fost anulată cu succes!")
        except sqlite3.Error as e:
            print("Eroare la anulare rezervare:", e)
            self.conn.rollback()
        else:
            self.conn.commit()

    def get_user_details(self, email):
        """
        Obține detaliile rezervărilor pentru un utilizator bazat pe adresa de email.

        Args:
            email (str): Adresa de email a utilizatorului pentru care se obțin detaliile rezervărilor.
        """
        try:
            user_details = self.cursor.execute("SELECT * FROM rezervari WHERE email=?", (email,)).fetchall()
            if not user_details:
                print("Nu există rezervări pentru acest utilizator.")
            else:
                print("Detalii rezervări:")
                for detail in user_details:
                    print(f"ID Spectacol: {detail[1]}, Nume Utilizator: {detail[2]}")
        except sqlite3.Error as e:
            print("Eroare la obținerea detaliilor utilizatorului:", e)

    def close_connection(self):
        """
        Închide conexiunea cu baza de date.
        """
        self.conn.close()
