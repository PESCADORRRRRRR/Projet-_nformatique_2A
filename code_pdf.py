
# Exemple d'utilisation des methodes


import scraping as scraping
from scraping import WikipediaScraper
from single import Single  # spotify est un module que j'ai creer
from manager import Manager
import scraping as scraping
from scraping import WikipediaScraper


class PDFGenerator:
    def __init__(self, url):
        """
        Initialise un générateur de fichiers PDF basé sur une URL donnée.

        Args:
            url (str): L'URL à partir de laquelle les détails des singles seront extraits.

        Raises:
            Exception: Si une erreur survient lors de l'initialisation du scraper.

        """
        self.url = url
        try:
            self.scraper = WikipediaScraper(url)
        except Exception as e:
            raise Exception("Erreur lors de l'initialisation du scraper :", e)
        
    def generate_PDF(self, nom_dossier_qr_codes, nom_dossier_sortie_pdf,dimension_qr_code):
        """
        Génère des fichiers PDF à partir des détails des singles extraits.

        Args:
            nom_dossier_qr_codes (str): Le nom du dossier contenant les codes QR.
            nom_dossier_sortie_pdf (str): Le nom du dossier de sortie pour les fichiers PDF.

        Raises:
            Exception: Si une erreur survient lors de la génération des PDF

        """
        try:
            # Extraction des détails des singles
            self.scraper.scrape()

            # Génération des codes QR
            self.scraper.generate_PDF(nom_dossier_qr_codes, nom_dossier_sortie_pdf, dimension_qr_code)

        except Exception as e:
            raise Exception("Erreur lors de la génération des PDF :", e)   
        

# URL de la page à extraire
url = "https://fr.wikipedia.org/wiki/Liste_des_singles_num%C3%A9ro_un_en_France"

# Création de l'objet QRCodeGenerator
PDFgenerator = PDFGenerator(url)

# Génération des codes QR
nom_dossier_sortie_pdf = "PDF"
nom_dossier_qr_codes = "image_qr_code"
dimension_qr_code = 400

PDFgenerator.generate_PDF(nom_dossier_qr_codes, nom_dossier_sortie_pdf,dimension_qr_code)
