import scraping as scraping
from scraping import WikipediaScraper
from single import Single
from manager import Manager

class QR_code_Single:
    def __init__(self, url):
        self.url = url
        self.scraper = WikipediaScraper(self.url)
        self.manager = Manager()

    
    def creer_QR_code(self):
        self.scraper.generate_qr_codes()
        
        


# URL de la page à extraire
url = "https://fr.wikipedia.org/wiki/Liste_des_singles_num%C3%A9ro_un_en_France"

# Création de l'objet QR_code_Single
stockage = QR_code_Single(url)

#creation des QR_code des singles

stockage.creer_QR_code()
