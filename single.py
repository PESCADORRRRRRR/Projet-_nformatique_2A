from manager import Manager
import os


class Single:
    """
    Représente un single musical avec un titre, un artiste, une date de sortie et des informations audio.

    Attributes:
        titre (str): Le titre du single.
        artiste (str): L'artiste du single.
        date (str): La date de sortie du single au format "YYYY-MM-DD".
        lien_spotify (str): Le lien vers le single sur Spotify.
        extrait_audio (str): L'extrait audio du single.
        manager (Manager): Le gestionnaire de recherche audio.

    Methods:
        __init__(self, titre, artiste, date): Initialise une instance de la classe Single.
        rechercher_audio_artiste_titre(self): Recherche et retourne les informations audio du single.
        afficher_informations(self): Affiche les informations du single.
        jouer_extrait_audio(self): Joue l'extrait audio du single.
        stocker_info(self, liste_info): Stocke les informations du single dans une liste.

    Usage:
        single = Single("Coup du marteau", "Tam sir", "Date du single")
        single.rechercher_audio_artiste_titre()
        single.afficher_informations()
        single.jouer_extrait_audio()
        single.stocker_info(liste_info)
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

        client_id = os.getenv("SPOTIFY_CLIENT_ID")
        client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

        self.manager = Manager(client_id, client_secret)

        self.lien_spotify = None
        self.extrait_audio = None

    def rechercher_audio_artiste_titre(self):
        """
        Recherche les informations audio du single (lien Spotify et extrait audio).

        Returns:
            audio_info (dict): Un dictionnaire contenant les informations audio du single.
        """
        try:
            audio_info = self.manager.rechercher_audio_artiste_titre(
                self.artiste, self.titre
            )
            if audio_info:
                self.lien_spotify = audio_info["lien_spotify"]
                self.extrait_audio = audio_info["extrait_audio"]
            return audio_info
        except Exception as e:
            print(
                "Une erreur s'est produite lors de la recherche des informations audio :",
                str(e),
            )
            return {}

    def afficher_informations(self):
        """
        Affiche les informations du single.
        """
        print("Titre :", self.titre)
        print("Artiste :", self.artiste)
        print("Date :", self.date)

        if self.lien_spotify:
            print("Lien Spotify :", self.lien_spotify)
        else:
            print("Lien Spotify non disponible")

        if self.extrait_audio:
            print("Extrait Audio :", self.extrait_audio)
        else:
            print("Extrait Audio non disponible")

    def jouer_extrait_audio(self):
        """
        Joue l'extrait audio du single s'il est trouvé, sinon affiche un message d'avertissement.
        """
        if self.extrait_audio:
            # Simule la lecture
            print(f"Lecture de l'extrait audio de {self.titre}...")
        else:
            print("Aucun extrait audio trouvé pour ce single")

    def stocker_info(self, liste_info):
        """
        Stocke les informations du single (titre, artiste, date, lien Spotify, extrait audio) dans une liste.

        Args:
            liste_info (list): La liste dans laquelle stocker les informations du single.

        Returns:
            liste_info (list): La liste mise à jour avec les informations du single.
        """
        try:
            audio_info = self.rechercher_audio_artiste_titre()
            info_single = {
                "titre": self.titre,
                "artiste": self.artiste,
                "date": self.date,
                "lien_spotify": self.lien_spotify,
                "extrait_audio": self.extrait_audio,
            }

            liste_info.append(info_single)

            return liste_info
        except Exception as e:
            print(
                "Une erreur s'est produite lors du stockage des informations du single :",
                str(e),
            )
            return liste_info


from single import Single


# Chargement des variables d'environnement
client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

# Création du gestionnaire avec les informations d'identification
manager = Manager(client_id, client_secret)

# Création d'une instance de la classe Single
single = Single("Coup du marteau", "Tam sir", "Date du single")

# Affichage des informations du single
# single.afficher_informations()

# Jouez l'extrait audio du single
single.jouer_extrait_audio()
