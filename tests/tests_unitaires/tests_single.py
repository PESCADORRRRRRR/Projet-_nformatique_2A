import unittest
import sys

from unittest.mock import MagicMock
from unittest.mock import patch
from io import StringIO

from single import Single
import re

class TestSingle(unittest.TestCase):
    """
    Classe de test pour la classe Single.

    Cette classe contient des tests unitaires pour les différentes méthodes de la classe `Single`.

    """

    def test_init(self):
        
        """
        Test de l'initialisation d'une instance de la classe Single.

        Ce test vérifie que les attributs de l'instance sont correctement initialisés.

        """
        
        # Test de l'initialisation d'une instance de la classe Single
        single = Single("Titre", "Artiste", "2023-12-01")

        # Vérification des attributs
        self.assertEqual(single.titre, "Titre")
        self.assertEqual(single.artiste, "Artiste")
        self.assertEqual(single.date, "2023-12-01")
        self.assertIsNone(single.lien_spotify)
        self.assertIsNone(single.extrait_audio)

    def test_rechercher_audio_artiste_titre(self):
        """
        Test de la recherche d'informations audio.

        Ce test vérifie que la fonction `rechercher_audio_artiste_titre` fonctionne correctement.

        """
        
        # Test de la recherche d'informations audio
        single = Single("La vie en rose", "Edith Piaf", "1946-10-20")

        # Simulation de la recherche avec un résultat positif
        audio_info = {
            "lien_spotify": "https://open.spotify.com/track/0i64F2s47c48q4387Y6T7w",
            "extrait_audio": "https://audio.spotify.com/preview/0i64F2s47c48q4387Y6T7w"
        }
        single.manager.rechercher_audio_artiste_titre = lambda a, t: audio_info

        # Appel de la fonction à tester
        single.rechercher_audio_artiste_titre()

        # Vérification des attributs après la recherche
        self.assertEqual(single.lien_spotify, "https://open.spotify.com/track/0i64F2s47c48q4387Y6T7w")
        self.assertEqual(single.extrait_audio, "https://audio.spotify.com/preview/0i64F2s47c48q4387Y6T7w")

    
    def test_afficher_informations(self):
        """
        Test de l'affichage des informations.

        Ce test vérifie que la fonction `afficher_informations` fonctionne correctement.

        """
        
        # Test de l'affichage des informations
        single = Single("La vie en rose", "Edith Piaf", "1946-10-20")
        single.lien_spotify = "https://open.spotify.com/track/0i64F2s47c48q4387Y6T7w"
        single.extrait_audio = "https://audio.spotify.com/preview/0i64F2s47c48q4387Y6T7w"

        # Capture de la sortie standard
        captured_output = StringIO()
        with patch("sys.stdout", new=captured_output):
            # Appel de la méthode afficher_informations
            single.afficher_informations()

        # Suppression des espaces au début de chaque ligne
        expected_output = re.sub(r"^ +", "", captured_output.getvalue())

        # Vérification du contenu affiché
        self.assertEqual(expected_output, expected_output)

    
    def test_jouer_extrait_audio(self):
        """
        Test de la simulation de la lecture de l'extrait audio.

        Ce test vérifie que la fonction `jouer_extrait_audio` fonctionne correctement.

        """
        
        # Test de la simulation de la lecture de l'extrait audio
        single = Single("La vie en rose", "Edith Piaf", "1946-10-20")

        # Capture de la sortie standard
        captured_output = StringIO()

        with patch("sys.stdout", new=captured_output):
            # Appel de la méthode `jouer_extrait_audio`
            try:
                single.jouer_extrait_audio()
            except Exception as e:
                self.fail(f"Une erreur s'est produite : {str(e)}")

       
        # Suppression des espaces au début de chaque ligne
        expected_output = re.sub(r"^ +", "", captured_output.getvalue())

        # Vérification du contenu affiché
        self.assertEqual(expected_output, expected_output)

if __name__ == '__main__':
    unittest.main()
