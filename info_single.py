# Importer la classe SinglesManager depuis le fichier scraping.py
import scraping
from scraping import WikipediaScraper

# URL de la page à extraire
url = "https://fr.wikipedia.org/wiki/Liste_des_singles_num%C3%A9ro_un_en_France"

# Création de l'objet WikipediaScraper
scraper = WikipediaScraper(url)

# Extraction des détails des singles
scraper.scrape()


# Créer une instance de SinglesManager en passant la liste des singles
manager = SinglesManager(scraper.singles)
# Fonction pour vérifier si un artiste est présent dans la liste
def is_artiste_present(artiste):
    artiste_present = manager.is_artiste_present(artiste)
    if artiste_present:
        print("L'artiste est présent dans la liste des singles.")
    else:
        print("L'artiste n'est pas présent dans la liste des singles.")

# Fonction pour obtenir les informations d'un artiste spécifique
def get_info_artiste(artiste):
    info_artiste = manager.get_info_artiste(artiste)
    if info_artiste:
        print("Informations de l'artiste :")
        print("Titre :", info_artiste["titre"])
        print("Date :", info_artiste["date"])
    else:
        print("L'artiste n'est pas présent dans la liste des singles.")
        
        

# Vérifier si un artiste est présent dans la liste
is_artiste_present("Nekfeu")

# Obtenir les informations d'un artiste spécifique
get_info_artiste("Nekfeu")