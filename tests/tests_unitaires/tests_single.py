import unittest
import sys

from unittest.mock import MagicMock
from unittest.mock import patch
from io import StringIO

from single import Single

class TestSingle(unittest.TestCase):
    """
    Classe de test pour la classe `Single`.
    """

    def test_init(self):
        """
        Teste la méthode d'initialisation de la classe `Single`.
        """
        # Création d'une instance de la classe `Single`
        single = Single("Titre du single", "Artiste du single", "2023-11-14")

        # Vérification des attributs de l'instance
        self.assertEqual(single.titre, "Titre du single")
        self.assertEqual(single.artiste, "Artiste du single")
        self.assertEqual(single.date, "2023-11-14")

    def test_rechercher_audio_artiste_titre(self):
        """
        Teste la méthode `rechercher_audio_artiste_titre` de la classe `Single`.
        """
        # Création d'une instance de la classe `Single`
        single = Single("Onizuka", "PNL", "2016-11-18")

        # Mock de la méthode `rechercher_audio_artiste_titre` du manager
        mock_manager = MagicMock()
        mock_manager.rechercher_audio_artiste_titre.return_value = {
            "lien_spotify": "https://spotify.com/single",
            "extrait_audio": "https://spotify.com/extrait"
        }
        single.manager = mock_manager

        # Appel de la méthode `rechercher_audio_artiste_titre`
        result = single.rechercher_audio_artiste_titre()

        # Vérification du résultat
        expected_result = {
            "lien_spotify": "https://spotify.com/single",
            "extrait_audio": "https://spotify.com/extrait"
        }
        self.assertEqual(result, expected_result)
        mock_manager.rechercher_audio_artiste_titre.assert_called_once_with("PNL", "Onizuka")
        
        
    def test_afficher_informations(self):
        """
        Teste la méthode `afficher_informations` de la classe `Single`.
        """
        # Création d'une instance de la classe `Single`
        single = Single("Onizuka", "PNL", "2016-11-18")

        # Capture de la sortie standard
        captured_output = StringIO()
        with patch("sys.stdout", new=captured_output):
            # Appel de la méthode `afficher_informations`
            single.afficher_informations()

        # Récupération de la sortie capturée
        output = captured_output.getvalue().strip()

        # Vérification du résultat
        expected_output = "Titre : Onizuka\nArtiste : PNL\nDate : 2016-11-18"
        self.assertEqual(output, expected_output)    
        
    def test_jouer_extrait_audio(self):
        """
        Teste la méthode `jouer_extrait_audio` de la classe `Single`.
        """
        # Création d'une instance de la classe `Single`
        single = Single("Onizuka", "PNL", "2016-11-18")

        # Capture de la sortie standard
        captured_output = StringIO()
        with patch("sys.stdout", new=captured_output):
            # Mock de la méthode `rechercher_audio_artiste_titre`
            single.rechercher_audio_artiste_titre = lambda: {
                "lien_spotify": "https://spotify.com/single",
                "extrait_audio": "https://spotify.com/extrait"
            }
            
            # Appel de la méthode `jouer_extrait_audio`
            single.jouer_extrait_audio()

        # Récupération de la sortie capturée
        output = captured_output.getvalue().strip()

        # Vérification du résultat
        expected_output = "Lien Spotify : https://spotify.com/single\nExtrait Audio : https://spotify.com/extrait"
        self.assertEqual(output, expected_output)
        
    
    
    
    
    
if __name__ == "__main__":
    unittest.main()
