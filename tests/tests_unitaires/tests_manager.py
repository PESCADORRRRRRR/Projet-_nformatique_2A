import unittest
from manager import Manager

class TestManager(unittest.TestCase):
    def setUp(self):
        self.manager = Manager()

    def test_rechercher_audio_artiste_titre(self):
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

    def test_rechercher_audio_artiste_titre_piste_inexistante(self):
        artist_name = "Artiste Inexistant"
        song_title = "Titre Inexistant"
        audio_info = self.manager.rechercher_audio_artiste_titre(artist_name, song_title)

        self.assertIsNone(audio_info)

if __name__ == '__main__':
    unittest.main()