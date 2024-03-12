import unittest
from single import Single

class TestSingle(unittest.TestCase):

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
        single = Single("Balance ton quoi", "Angèle", "2018-07-06")

        # Appel de la méthode `rechercher_audio_artiste_titre`
        audio_info = single.rechercher_audio_artiste_titre()

        # Vérification des informations audio
        self.assertEqual(audio_info["lien_spotify"], "https://open.spotify.com/track/3s1eN125m7HUX6L7Z9Q9qA")
        self.assertEqual(audio_info["extrait_audio"], "https://audio-preview.spotify.com/v1/artists/6610075Y7j872zL825HA1K/tracks/3s1eN125m7HUX6L7Z9Q9qA")

    def test_afficher_informations(self):
        """
        Teste la méthode `afficher_informations` de la classe `Single`.
        """
        # Création d'une instance de la classe `Single`
        single = Single("Balance ton quoi", "Angèle", "2018-07-06")

        # Capture de la sortie de la console
        with self.assertLogs() as cm:
            single.afficher_informations()

        # Vérification de la sortie
        self.assertEqual(len(cm.output), 3)
        self.assertEqual(cm.output[0], "Titre : Balance ton quoi")
        self.assertEqual(cm.output[1], "Artiste : Angèle")
        self.assertEqual(cm.output[2], "Date : 2018-07-06")

    def test_jouer_extrait_audio(self):
        """
        Teste la méthode `jouer_extrait_audio` de la classe `Single`.
        """
        # Création d'une instance de la classe `Single`
        single = Single("Balance ton quoi", "Angèle", "2018-07-06")

        # Capture de la sortie de la console
        with self.assertLogs() as cm:
            single.jouer_extrait_audio()

        # Vérification de la sortie
        self.assertEqual(len(cm.output), 2)
        self.assertEqual(cm.output[0], "Lien Spotify : https://open.spotify.com/track/3s1eN125m7HUX6L7Z9Q9qA")
        self.assertEqual(cm.output[1], "Extrait Audio : https://audio-preview.spotify.com/v1/artists/6610075Y7j872zL825HA1K/tracks/3s1eN125m7HUX6L7Z9Q9qA")

if __name__ == "__main__":
    unittest.main()

