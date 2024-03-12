from unittest import mock

from single import Single

@mock.patch.object(Single, "rechercher_audio_artiste_titre")
def test_jouer_extrait_audio(mock_rechercher_audio):
    # Configuration du mock
    mock_rechercher_audio.return_value = {
        "lien_spotify": "https://open.spotify.com/track/123456789",
        "extrait_audio": "https://www.youtube.com/watch?v=abcdefghij"
    }

    # Appel de la méthode à tester
    single = Single("Titre du single", "Artiste du single", "2023-03-08")
    single.jouer_extrait_audio()

    # Vérification des appels au mock
    mock_rechercher_audio.assert_called_once()

    # Vérification des arguments passés au mock
    assert mock_rechercher_audio.call_args[0][0] == "Artiste du single"
    assert mock_rechercher_audio.call_args[0][1] == "Titre du single"

