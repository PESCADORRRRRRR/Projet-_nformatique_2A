import unittest
from manager import Manager
from unittest import mock
#ce test est utilisé car Le fichier manager.py contient du code qui dépend d'un service externe, comme une API web
class TestManager(unittest.TestCase):

    @mock.patch.object(Manager, "rechercher_audio_artiste_titre")
    def test_rechercher_audio_artiste_titre(self, mock_rechercher_audio_artiste_titre):
        """
        Teste la méthode `rechercher_audio_artiste_titre` de la classe `Manager` en utilisant Mocking.
        """
        # Configuration du mock
        mock_rechercher_audio_artiste_titre.return_value = {
            "titre": "Balance ton quoi",
            "lien_spotify": "https://open.spotify.com/track/3s1eN125m7HUX6L7Z9Q9qA",
            "extrait_audio": "https://audio-preview.spotify.com/v1/artists/6610075Y7j872zL825HA1K/tracks/3s1eN125m7HUX6L7Z9Q9qA"
        }

        # Appel de la méthode à tester
        manager = Manager()
        audio_info = manager.rechercher_audio_artiste_titre("Angèle", "Balance ton quoi")

        # Vérification du résultat
        self.assertEqual(audio_info, {
            "titre": "Balance ton quoi",
            "lien_spotify": "https://open.spotify.com/track/3s1eN125m7HUX6L7Z9Q9qA",
            "extrait_audio": "https://audio-preview.spotify.com/v1/artists/6610075Y7j872zL825HA1K/tracks/3s1eN125m7HUX6L7Z9Q9qA"
        })

        # Vérification que la méthode `rechercher_audio_artiste_titre` a été appelée avec les bons arguments
        mock_rechercher_audio_artiste_titre.assert_called_with("Angèle", "Balance ton quoi")

if __name__ == "__main__":
    unittest.main()
