# Importation des bibliothèques nécessaires
from bs4 import BeautifulSoup
import requests

# URL de la page à extraire
url = "https://fr.wikipedia.org/wiki/Liste_des_singles_num%C3%A9ro_un_en_France"

# Envoi d'une requête GET à l'URL et récupération du contenu HTML de la page
response = requests.get(url)
html_content = response.content

# Utilisation de BeautifulSoup pour analyser le contenu HTML
soup = BeautifulSoup(html_content, "html.parser")

# Recherche de la table contenant les informations sur les singles numéro un en France
table = soup.find("table", class_="wikitable")

# Extraction des lignes de la table
rows = table.find_all("tr")

# Création d'une liste pour stocker les détails des singles
singles = []

# Parcours de chaque ligne de la table
for row in rows:
    # Extraction des cellules de la ligne
    cells = row.find_all("td")
    
    # Vérification si la ligne contient suffisamment de cellules
    if len(cells) >= 3:
        # Extraction des détails du single : titre, artiste et date
        titre = cells[1].text.strip()
        artiste = cells[2].text.strip()
        date = cells[3].text.strip()
        
        # Stockage des détails du single dans un dictionnaire
        single = {
            "titre": titre,
            "artiste": artiste,
            "date": date
        }
        
        # Ajout du dictionnaire à la liste des singles
        singles.append(single)

# Affichage des détails des singles
for single in singles:
    print(single)
