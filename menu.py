class Menu:
    """
    Clasa Menu definește metodele pentru afișarea și obținerea opțiunilor din meniul principal.
    """

    @staticmethod
    def show_main_menu():
        """
        Afișează meniul principal al aplicației.

        Returns:
            None
        """
        print("\nMeniu principal:")
        print("1. Vizualizare spectacole disponibile")
        print("2. Rezervare bilet")
        print("3. Anulare rezervare")
        print("4. Vizualizare detalii utilizator")
        print("5. Ieșire")

    @staticmethod
    def get_main_menu_choice():
        """
        Obține opțiunea aleasă de utilizator din meniul principal.

        Returns:
            str: Opțiunea aleasă de utilizator.
        """
        while True:
            Menu.show_main_menu()
            choice = input("Alegeți o opțiune: ")
            if choice in ["1", "2", "3", "4", "5"]:
                return choice
            else:
                print("Opțiune invalidă. Vă rugăm să alegeți din nou.")


