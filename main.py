from database import DatabaseManager
from menu import Menu
from shows import ShowManager
from booking import BookingManager

def print_welcome_message():
    """
    Afișează un mesaj de bun venit cu un design simplu în linia de comandă.
    """
    welcome_message = """
****************************
*                          *
*   Bine ați venit la      *
*   aplicația de emitere   *
* bilete pentru spectacole!*
*                          *
****************************
"""
    print(welcome_message)

def main():
    """
    Funcția principală a aplicației de emitere bilete spectacole.
    """
    print_welcome_message()

   
    db_manager = DatabaseManager('bilete_spectacole.db')
    db_manager.create_tables()

   
    show_manager = ShowManager(db_manager)
    booking_manager = BookingManager('bilete_spectacole.db')

    while True:
       
        choice = Menu.get_main_menu_choice()

        if choice == "1":
            show_manager.show_available_shows()

        elif choice == "2":
            show_manager.show_available_shows()
            show_id = int(input("Introduceți ID-ul spectacolului pentru care doriți să rezervați un bilet: "))
            nume_utilizator = input("Introduceți numele dumneavoastră: ")
            email = input("Introduceți adresa de email: ")
            booking_manager.reserve_ticket(show_id, nume_utilizator, email)

        elif choice == "3":
            email = input("Introduceți adresa de email pentru anularea rezervării: ")
            booking_manager.cancel_reservation(email)

        elif choice == "4":
            email = input("Introduceți adresa de email pentru a vizualiza detaliile rezervărilor: ")
            booking_manager.get_user_details(email)

        elif choice == "5":
            booking_manager.close_connection()
            print("La revedere!")
            break

if __name__ == "__main__":
    main()
