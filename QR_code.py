# Exemple d'utilisation des methodes


import scraping as scraping
from scraping import WikipediaScraper
from single import Single  # spotify est un module que j'ai creer
from manager import Manager
import scraping as scraping
from scraping import WikipediaScraper


class QRCodeGenerator:
    def __init__(self, url):
        self.url = url
        self.scraper = WikipediaScraper(url)

    def generate_qr_code(self):
        # Extraction des détails des singles
        self.scraper.scrape()

        # Génération des codes QR
        self.scraper.generate_qr_codes()


# URL de la page à extraire
url = "https://fr.wikipedia.org/wiki/Liste_des_singles_num%C3%A9ro_un_en_France"

# Création de l'objet QRCodeGenerator
qr_generator = QRCodeGenerator(url)

# Génération des codes QR
qr_generator.generate_qr_code()
