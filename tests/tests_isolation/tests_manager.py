import unittest
from manager import Manager
from unittest import mock
import os 


client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

# Ce test est utilisé car le fichier manager.py contient du code qui dépend d'un service externe, comme une API web

class TestManager(unittest.TestCase):

    """
    Classe de test pour la classe `Manager`.
    """

    @mock.patch.object(Manager, "rechercher_audio_artiste_titre")
    def test_rechercher_audio_artiste_titre(self, mock_rechercher_audio_artiste_titre):
        """
        Teste la méthode `rechercher_audio_artiste_titre` de la classe `Manager`.

        Parameters
        ----------
        mock_rechercher_audio_artiste_titre : MagicMock
            Le mock de la méthode `rechercher_audio_artiste_titre` du manager.

        Returns
        -------
        None
        """

        # Configuration du mock
        mock_rechercher_audio_artiste_titre.return_value = {
            "titre": "Balance ton quoi",
            "lien_spotify": "https://open.spotify.com/track/3s1eN125m7HUX6L7Z9Q9qA",
            "extrait_audio": "https://audio-preview.spotify.com/v1/artists/6610075Y7j872zL825HA1K/tracks/3s1eN125m7HUX6L7Z9Q9qA"
        }

        # Appel de la méthode à tester
        
        manager = Manager(client_id, client_secret)

        audio_info = manager.rechercher_audio_artiste_titre("Angèle", "Balance ton quoi")

        # Vérification du résultat
        self.assertEqual(audio_info, {
            "titre": "Balance ton quoi",
            "lien_spotify": "https://open.spotify.com/track/3s1eN125m7HUX6L7Z9Q9qA",
            "extrait_audio": "https://audio-preview.spotify.com/v1/artists/6610075Y7j872zL825HA1K/tracks/3s1eN125m7HUX6L7Z9Q9qA"
        })

        # Vérification que la méthode `rechercher_audio_artiste_titre` a été appelée avec les bons arguments
        mock_rechercher_audio_artiste_titre.assert_called_with("Angèle", "Balance ton quoi")

    @mock.patch.object(Manager, "rechercher_audio_artiste_titre")
    def test_rechercher_audio_artiste_titre_sans_resultat(self, mock_rechercher_audio_artiste_titre):
        """
        Teste la méthode `rechercher_audio_artiste_titre` de la classe `Manager` sans résultat.

        Parameters
        ----------
        mock_rechercher_audio_artiste_titre : MagicMock
            Le mock de la méthode `rechercher_audio_artiste_titre` du manager.

        Returns
        -------
        None
        """

        # Configuration du mock
        mock_rechercher_audio_artiste_titre.return_value = None

        # Appel de la méthode à tester
        manager = Manager(client_id, client_secret)
        audio_info = manager.rechercher_audio_artiste_titre("Artiste inconnu", "Chanson introuvable")

        # Vérification du résultat
        self.assertIsNone(audio_info)

        # Vérification que la méthode `rechercher_audio_artiste_titre` a été appelée avec les bons arguments
        mock_rechercher_audio_artiste_titre.assert_called_with("Artiste inconnu", "Chanson introuvable")



    
    
if __name__ == "__main__":
    unittest.main()
