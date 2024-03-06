#Etaoe1
import scraping
from scraping import WikipediaScraper


# URL de la page à extraire
url = "https://fr.wikipedia.org/wiki/Liste_des_singles_num%C3%A9ro_un_en_France"

# Création de l'objet WikipediaScraper
scraper = WikipediaScraper(url)

# Extraction des détails des singles
scraper.scrape()

# Affichage des détails des singles
scraper.print_singles()


