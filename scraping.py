# Importation des bibliothèques nécessaires
from bs4 import BeautifulSoup
import requests
class WikipediaScraper:
    def __init__(self, url):
        self.url = url
        self.singles = []

    def scrape(self):
        # Envoi d'une requête GET à l'URL et récupération du contenu HTML de la page
        response = requests.get(self.url)
        html_content = response.content

        # Utilisation de BeautifulSoup pour analyser le contenu HTML
        soup = BeautifulSoup(html_content, "html.parser")

        # Recherche de toutes les tables contenant les informations sur les singles numéro un en France
        tables = soup.find_all("table", class_="wikitable")

        # Parcours de chaque table
        for table in tables:
            # Extraction des lignes de la table
            rows = table.find_all("tr")[1:]  # Ignorer la première ligne (en-tête)

            # Parcours de chaque ligne de la table
            for row in rows:
                # Extraction des cellules de la ligne
                cells = row.find_all("td")

                # Vérification si la ligne contient suffisamment de cellules
                if len(cells) >= 3:
                    # Extraction des détails du single : titre, artiste et date
                    date = cells[1].text.strip()
                    artiste = cells[2].text.strip()
                    titre = cells[3].text.strip()
                    #on suit l'ordre des colonnes qui est sur wiki

                    # Stockage des détails du single dans un dictionnaire
                    single = {
                        "titre": titre,
                        "artiste": artiste,
                        "date": date
                    }

                    # Ajout du dictionnaire à la liste des singles
                    self.singles.append(single)

    def print_singles(self):
        for single in self.singles:
            titre = single["titre"]
            artiste = single["artiste"]
            date = single["date"]
            print("Titre:", titre)
            print("Artiste:", artiste)
            print("Date:", date)
            print("-------------------")
            



class SinglesManager:
    def __init__(self, singles):
        self.singles = singles

    def is_artiste_present(self, artiste):
        # Vérifie si l'artiste est présent dans la liste des singles
        for single in self.singles:
            if single["artiste"] == artiste:  # Vérifie si le nom de l'artiste correspond à celui recherché
                return True
        return False

    def get_info_artiste(self, artiste):
        # Récupère les informations du premier single correspondant à l'artiste
        for single in self.singles:
            if single["artiste"] == artiste:  # Vérifie si le nom de l'artiste correspond à celui recherché
                return single
        return None