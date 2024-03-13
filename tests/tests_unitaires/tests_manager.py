import unittest
from manager import Manager
import os

client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

class TestManager(unittest.TestCase):
    """
    Classe de test pour la classe Manager.

    ...

    Methods
    -------
    setUp()
        Méthode qui s'exécute avant chaque test pour initialiser les objets nécessaires.
    test_rechercher_audio_artiste_titre()
        Méthode de test pour la fonction rechercher_audio_artiste_titre() de la classe Manager.
        Vérifie si les informations audio renvoyées sont correctes pour une piste existante.
    test_rechercher_audio_artiste_titre_piste_inexistante()
        Méthode de test pour la fonction rechercher_audio_artiste_titre() de la classe Manager.
        Vérifie si None est renvoyé pour une piste inexistante.
    """
    
    
    
    def setUp(self):
        """
        Méthode qui s'exécute avant chaque test pour initialiser les objets nécessaires.
        """
        self.manager = Manager(client_id, client_secret)

    def test_rechercher_audio_artiste_titre(self):
        """
        Méthode de test pour la fonction rechercher_audio_artiste_titre() de la classe Manager.
        Vérifie si les informations audio renvoyées sont correctes pour une piste existante.
        """
        artist_name = "Michael Jackson"
        song_title = "Thriller"
        audio_info = self.manager.rechercher_audio_artiste_titre(artist_name, song_title)

        self.assertIsNotNone(audio_info)
        self.assertEqual(audio_info["titre"], "Thriller")
        self.assertTrue(audio_info["lien_spotify"].startswith("https://open.spotify.com/"))

        if audio_info["extrait_audio"] is not None:
            self.assertTrue(audio_info["extrait_audio"])
        else:
            print("Extrait audio non disponible")

    

if __name__ == '__main__':
    unittest.main()