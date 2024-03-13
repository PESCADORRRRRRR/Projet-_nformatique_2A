import unittest
from manager import Manager
from unittest import mock
from single import Single
import os 


client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

@mock.patch.object(Manager, "rechercher_audio_artiste_titre")
def test_rechercher_audio_artiste_titre(self, mock_rechercher_audio):
    """
    Test de la méthode `rechercher_audio_artiste_titre`.

    Ce test vérifie que la méthode appelle la méthode `rechercher_audio_artiste_titre` du gestionnaire
    avec les bons arguments et retourne le résultat attendu.
    """
    # Configuration du mock
    mock_rechercher_audio.return_value = {
        "lien_spotify": "https://open.spotify.com/track/123456789",
        "extrait_audio": "https://www.youtube.com/watch?v=abcdefghij"
    }

    # Appel de la méthode à tester
    single = Single("Titre du single", "Artiste du single", "2023-03-08")
    audio_info = single.rechercher_audio_artiste_titre()

    # Vérification des appels au mock
    mock_rechercher_audio.assert_called_once()

    # Vérification des arguments passés au mock
    assert mock_rechercher_audio.call_args[0][0] == "Artiste du single"
    assert mock_rechercher_audio.call_args[0][1] == "Titre du single"

    # Vérification du résultat
    assert audio_info == {
        "lien_spotify": "https://open.spotify.com/track/123456789",
        "extrait_audio": "https://www.youtube.com/watch?v=abcdefghij"
    }
