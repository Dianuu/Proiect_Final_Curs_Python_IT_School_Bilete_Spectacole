class ShowManager:
    """
    Clasa ShowManager gestionează afișarea spectacolelor disponibile.
    """

    def __init__(self, db_manager):
        """
        Inițializează managerul de spectacole cu un manager de bază de date.

        Args:
            db_manager (object): Managerul de bază de date.
        """
        self.db_manager = db_manager

    def show_available_shows(self):
        """
        Afișează spectacolele disponibile împreună cu detaliile acestora.
        
        Returns:
            None
        """
        cursor = self.db_manager.cursor.execute("SELECT * FROM spectacole")
        print("\nSpectacole disponibile:")
        for show in cursor:
            print(f"{show[0]}. {show[1]} - Data și Ora: {show[2]}, Locuri Disponibile: {show[4]}, Preț: {show[3]}, Locație: {show[5]}")

