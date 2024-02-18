import sqlite3

class DatabaseManager:
    """
    Clasa DatabaseManager gestionează baza de date SQLite și operațiile asociate cu aceasta.
    """

    def __init__(self, db_name):
        """
        Inițializează managerul bazei de date cu numele bazei de date.

        Args:
            db_name (str): Numele bazei de date SQLite.
        """
        try:
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print("Eroare la conectarea la baza de date:", e)

    def create_tables(self):
        """
        Creează tabelele necesare în baza de date, dacă nu există deja.

        Returns:
            None
        """
        try:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS spectacole (
                    id INTEGER PRIMARY KEY,
                    nume TEXT,
                    data_ora TEXT,
                    pret INTEGER,
                    locuri_disponibile INTEGER,
                    locatie TEXT,
                    tip TEXT
                )
            ''')

            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS rezervari (
                    id INTEGER PRIMARY KEY,
                    show_id INTEGER,
                    nume_utilizator TEXT,
                    email TEXT,
                    FOREIGN KEY(show_id) REFERENCES spectacole(id)
                )
            ''')

            self.conn.commit()
        except sqlite3.Error as e:
            print("Eroare la crearea tabelelor:", e)

    def insert_spectacol(self, nume, data_ora, pret, locuri_disponibile, locatie, tip):
        """
        Inserează un nou spectacol în tabelul 'spectacole'.

        Args:
            nume (str): Numele spectacolului.
            data_ora (str): Data și ora spectacolului.
            pret (int): Prețul unui bilet pentru spectacol.
            locuri_disponibile (int): Numărul de locuri disponibile pentru spectacol.
            locatie (str): Locația spectacolului.
            tip (str): Tipul spectacolului.

        Returns:
            None
        """
        try:
            self.cursor.execute('''
                INSERT INTO spectacole (nume, data_ora, pret, locuri_disponibile, locatie, tip)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (nume, data_ora, pret, locuri_disponibile, locatie, tip))
            self.conn.commit()
        except sqlite3.Error as e:
            print("Eroare la inserarea spectacolului:", e)

    def close_connection(self):
        """
        Închide conexiunea cu baza de date.

        Returns:
            None
        """
        self.conn.close()
