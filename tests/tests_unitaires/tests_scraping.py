import unittest
from scraping import WikipediaScraper

class TestWikipediaScraper(unittest.TestCase):

    def test_scrape(self):
        """
        Teste la méthode `scrape` de la classe `WikipediaScraper`.
        """
        # URL de la page à scraper
        url = "https://fr.wikipedia.org/wiki/Liste_des_num%C3%A9ros_un_en_France"

        # Création d'une instance de la classe `WikipediaScraper`
        scraper = WikipediaScraper(url)

        # Appel de la méthode `scrape`
        scraper.scrape()

        # Vérification du nombre de singles extraits
        self.assertGreaterEqual(len(scraper.singles), 100)

        # Vérification des informations d'un single
        single = scraper.singles[0]
        self.assertEqual(single["titre"], "Balance ton quoi")
        self.assertEqual(single["artiste"], "Angèle")
        self.assertEqual(single["date"], "6 juillet 2018")

    def test_afficher_artistes_titres(self):
        """
        Teste la méthode `afficher_artistes_titres` de la classe `WikipediaScraper`.
        """
        # Création d'une instance de la classe `WikipediaScraper` avec une liste de singles vide
        scraper = WikipediaScraper("")
        scraper.singles = [{
            "titre": "Balance ton quoi",
            "artiste": "Angèle",
            "date": "6 juillet 2018"
        }]

        # Capture de la sortie de la console
        with self.assertLogs() as cm:
            scraper.afficher_artistes_titres()

        # Vérification de la sortie
        self.assertEqual(len(cm.output), 2)
        self.assertEqual(cm.output[0], "Balance ton quoi - Angèle")
        self.assertEqual(cm.output[1], "-------------------")

if __name__ == "__main__":
    unittest.main()

