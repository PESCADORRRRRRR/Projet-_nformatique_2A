import unittest
from manager import Manager

class TestManager(unittest.TestCase):

    def test_rechercher_audio_artiste_titre(self):
        """
        Teste la méthode `rechercher_audio_artiste_titre` de la classe `Manager`.
        """
        # Création d'une instance de la classe `Manager`
        manager = Manager()

        # Recherche d'informations audio pour une chanson connue
        audio_info = manager.rechercher_audio_artiste_titre("Angèle", "Balance ton quoi")

        # Vérification des informations audio
        self.assertEqual(audio_info["titre"], "Balance ton quoi")
        self.assertEqual(audio_info["lien_spotify"], "https://open.spotify.com/track/3s1eN125m7HUX6L7Z9Q9qA")
        self.assertEqual(audio_info["extrait_audio"], "https://audio-preview.spotify.com/v1/artists/6610075Y7j872zL825HA1K/tracks/3s1eN125m7HUX6L7Z9Q9qA")

        # Recherche d'informations audio pour une chanson inexistante
        audio_info = manager.rechercher_audio_artiste_titre("Artiste inconnu", "Chanson inexistante")

        # Vérification que la recherche n'a pas trouvé de résultat
        self.assertEqual(audio_info, None)

if __name__ == "__main__":
    unittest.main()
