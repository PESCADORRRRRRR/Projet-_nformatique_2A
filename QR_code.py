# Exemple d'utilisation des methodes


import scraping as scraping
from scraping import WikipediaScraper
from single import Single  # spotify est un module que j'ai creer
from manager import Manager
import scraping as scraping
from scraping import WikipediaScraper


class QRCodeGenerator:
    def __init__(self, url):
        """
        Initialise un générateur de codes QR pour une URL donnée.

        :param url: L'URL à partir de laquelle les informations seront extraites.
        """
        self.url = url
        self.is_completed = False
        try:
            self.scraper = WikipediaScraper(url)
        except Exception as e:
            raise Exception("Erreur lors de l'initialisation du scraper :", e)

    def generate_qr_code(self, nom_dossier_sortie_qr_code):
        """
        Génère les codes QR à partir des détails des singles extraits de l'URL.

        :param nom_dossier_sortie_qr_code: Le nom du dossier de sortie pour les codes QR générés.
        """
        try:
            # Extraction des détails des singles
            self.scraper.scrape()

            # Génération des codes QR
            self.scraper.generate_qr_codes(nom_dossier_sortie_qr_code)
            self.is_completed = True
            
        except Exception as e:
            raise Exception("Erreur lors de la génération des codes QR :", e)
    
    def is_generation_completed(self):
        return self.is_completed


