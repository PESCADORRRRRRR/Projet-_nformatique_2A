from manager import Manager

class Single:
    """
    Représente un single musical avec un titre, un artiste et une date de sortie.

    Attributes:
        titre (str): Le titre du single.
        artiste (str): L'artiste du single.
        date (str): La date de sortie du single au format "YYYY-MM-DD".
        manager (Manager): Une instance de la classe Manager pour effectuer des opérations de gestion de la musique.

    Methods:
        rechercher_audio_artiste_titre(): Recherche et retourne les informations audio du single (lien Spotify et extrait audio).
        afficher_informations(): Affiche les informations du single (titre, artiste, date).
        jouer_extrait_audio(): Joue l'extrait audio du single s'il est trouvé, sinon affiche un message d'avertissement.

    Usage:
        # Création d'une instance de la classe Single
        single = Single("Titre du single", "Artiste du single", "Date du single")

        # Affichage des informations du single
        single.afficher_informations()

        # Lecture de l'extrait audio du single
        single.jouer_extrait_audio()
    """
    
    def __init__(self, titre, artiste, date):
        """
        Initialise une instance de la classe Single avec un titre, un artiste et une date.

        Args:
            titre (str): Le titre du single.
            artiste (str): L'artiste du single.
            date (str): La date de sortie du single au format "YYYY-MM-DD".
        """
        self.titre = titre
        self.artiste = artiste
        self.date = date
        self.manager = Manager()

    def rechercher_audio_artiste_titre(self):
        """
        Recherche et retourne les informations audio du single (lien Spotify et extrait audio).

        Returns:
            dict: Un dictionnaire contenant les informations audio du single (lien Spotify et extrait audio).
        """
        return self.manager.rechercher_audio_artiste_titre(self.artiste, self.titre)

    def afficher_informations(self):
        """
        Affiche les informations du single (titre, artiste, date).
        """
        print("Titre :", self.titre)
        print("Artiste :", self.artiste)
        print("Date :", self.date)

    def jouer_extrait_audio(self):
        """
        Joue l'extrait audio du single s'il est trouvé, sinon affiche un message d'avertissement.
        """
        audio_info = self.rechercher_audio_artiste_titre()
        if audio_info:
            print("Lien Spotify :", audio_info["lien_spotify"])
            print("Extrait Audio :", audio_info["extrait_audio"])
        else:
            print("Aucun extrait audio trouvé pour ce single")

    def stocker_info(self, liste_info):
        """
        Stocke les informations du single (titre, artiste, date, lien Spotify, extrait audio) dans une liste.

        Args:
            liste_info (list): La liste dans laquelle stocker les informations du single.
        """
        audio_info = self.rechercher_audio_artiste_titre()
        info_single = {
            "titre": self.titre,
            "artiste": self.artiste,
            "date": self.date,
            "lien_spotify": audio_info.get("lien_spotify") if audio_info else None,
            "extrait_audio": audio_info.get("extrait_audio") if audio_info else None
        }
        liste_info.append(info_single)
        
        return liste_info

# Créez une instance de la classe Single
single = Single("Titre du single", "Artiste du single", "Date du single")

# Affichez les informations du single
single.afficher_informations()

# Jouez l'extrait audio du single
single.jouer_extrait_audio()