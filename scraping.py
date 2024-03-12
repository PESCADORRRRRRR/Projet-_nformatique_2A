# Importation des bibliothèques nécessaires
from bs4 import BeautifulSoup
import requests
from single import Single #spotify est un module que j'ai creer 
from manager import Manager 
import sqlite3
from datetime import datetime
import os
import qrcode


class WikipediaScraper:
    """
        Constructeur de la classe.

        :param url: L'URL de la page à scraper.
    """
    
    
    def __init__(self, url):
        self.url = url
        self.singles = []
        self.db_conn = sqlite3.connect('base_donnee.db')
        self.db_cursor = self.db_conn.cursor()

    def scrape(self):
        """
        Méthode pour effectuer le scraping des informations sur les singles.
        """
        
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
                if len(cells) >= 4:
                    # Extraction des détails du single : titre, artiste et date
                    date = cells[1].text.strip()
                    artiste = cells[2].text.strip()
                    titre = cells[3].text.strip()

                    # Stockage des détails du single dans un dictionnaire
                    single = {
                        "titre": titre,
                        "artiste": artiste,
                        "date": date
                    }

                    # Ajout du dictionnaire à la liste des singles
                    self.singles.append(single)
    
    
    

    
    def afficher_artistes_titres(self):
        """
        Méthode pour afficher les artistes et titres des singles.
        """
        
        if self.singles:
            for single in self.singles:
                
                single_instance = Single(single["titre"], single["artiste"], single["date"])
                single_instance.afficher_informations()
                print("-------------------")
        else:
            print("Aucun single trouvé.")
    

    def rechercher_extraits_audio(self):
        """
        Méthode pour rechercher les extraits audio des singles.
        """
        if self.singles:
            for single in self.singles:
                single_instance = Single(single["titre"], single["artiste"], single["date"])
                single_instance.afficher_informations()
                single_instance.jouer_extrait_audio()
                print("-------------------")
        else:
            print("Aucun single trouvé.")
    
    
       
        
        
    
    
    
    
    
    def rechercher_singles(self):
        """
        Méthode pour rechercher des singles spécifiques.
        """
        # Demander à l'utilisateur de saisir le critère de recherche et la valeur de recherche
        critere = input("Entrez le critère de recherche (titre, artiste ou date) : ")
        valeur_recherche = input("Entrez la valeur de recherche : ") #si tu choisi artiste comme critère , tu mettra le nom de l'artiste en valeur_recherche

        # Créer une liste pour stocker les singles correspondants à la recherche
        singles_recherches = []

        # Parcourir la liste des singles extraits
        for single in self.singles:
            # Vérifier si le critère de recherche est "titre" et si la valeur de recherche est présente dans le titre du single
            if critere.lower() == "titre" and valeur_recherche.lower() in single["titre"].lower():
                singles_recherches.append(single)
            # Vérifier si le critère de recherche est "artiste" et si la valeur de recherche est présente dans le nom de l'artiste du single
            elif critere.lower() == "artiste" and valeur_recherche.lower() in single["artiste"].lower():
                singles_recherches.append(single)
            # Vérifier si le critère de recherche est "date" et si la valeur de recherche est présente dans la date du single
            elif critere.lower() == "date" and valeur_recherche.lower() in single["date"].lower():
                singles_recherches.append(single)

        # Vérifier si des singles correspondants ont été trouvés
        if singles_recherches:
            # Parcourir les singles correspondants et afficher leurs informations
            for single in singles_recherches:
                single_instance = Single(single["titre"], single["artiste"], single["date"])
                single_instance.afficher_informations()
                print("-------------------")
        else:
            print("Aucun single trouvé pour la valeur de recherche spécifiée.")
            
    
    def inserer_dans_liste(self):
        singles = []
        
        # Parcourir la liste des singles extraits
        for single_data in self.singles:

            # Récupérer les informations du single
            titre = single_data.get("titre", "")
            artiste = single_data.get("artiste", "")
            date = single_data.get("date", "")

            # Créer une instance de la classe Single avec les données du single
            single = Single(titre, artiste, date)

            audio_info = single.rechercher_audio_artiste_titre()

            lien_spotify = audio_info.get("lien_spotify") if audio_info else None
            extrait_audio = audio_info.get("extrait_audio") if audio_info else None

            try:
                # Vérifier si la date contient plusieurs valeurs séparées par une virgule
                if ',' in date:
                    # Diviser la chaîne en une liste de dates individuelles
                    dates = date.split(',')
                else:
                    dates = [date]

                # Convertir chaque date au format 'DD/MM/YYYY' en 'YYYY-MM-DD' et insérer individuellement
                for date in dates:
                    # Supprimer les espaces avant et après la chaîne de caractères de la date
                    date = date.strip()

                    # Supprimer le "[1]" à la fin de la date, s'il est présent
                    if '[1]' in date:
                        date = date.split('[1]')[0]

                    formatted_date = datetime.strptime(date, "%d/%m/%Y").strftime("%Y-%m-%d")

                    # Créer un dictionnaire avec les détails du single
                    single_info = {
                        "titre": titre,
                        "artiste": artiste,
                        "date": formatted_date,
                        "lien_spotify": lien_spotify,
                        "extrait_audio": extrait_audio
                    }

                    # Ajouter le dictionnaire à la liste des singles
                    singles.append(single_info)

            except ValueError:
                print("Erreur lors de la conversion de la date")

        return singles
    
    
    
        
    def generate_qr_codes(self):
        # Spécifiez le nom du dossier principal
        nom_dossier = "QRCODE"

        # Spécifiez le nom du sous-dossier
        nom_s_dossier = "image_qr"

        # Obtenez le chemin absolu du dossier principal en utilisant le chemin courant du script
        chemin_dossier_principal = os.path.abspath(nom_dossier)

        # Obtenez le chemin absolu du sous-dossier en utilisant os.path.join() pour concaténer les noms de dossiers
        chemin_sous_dossier = os.path.join(chemin_dossier_principal, nom_s_dossier)

        # Créez le dossier s'il n'existe pas déjà
        os.makedirs(chemin_sous_dossier, exist_ok=True)

        for single_data in self.singles:
            titre = single_data.get("titre", "")
            artiste = single_data.get("artiste", "")
            date = single_data.get("date", "")

            single = Single(single_data["titre"], single_data["artiste"], single_data["date"])

            audio_info = single.rechercher_audio_artiste_titre()

            lien_spotify = audio_info.get("lien_spotify") if audio_info else None
            extrait_audio = audio_info.get("extrait_audio") if audio_info else None

            try:
                lien=lien_spotify
                qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
                if extrait_audio is not None:
                    lien=extrait_audio
                
                qr.add_data(lien)
                qr.make(fit=True)

                    # Enregistrez l'image du QR code dans le dossier spécifié avec un nom de fichier unique
                nom_fichier = f"qr_code_{titre}.png"
                chemin_fichier = os.path.join(chemin_sous_dossier, nom_fichier)

                image = qr.make_image(fill_color="black", back_color="white")
                image.save(chemin_fichier)   
                

                

            except Exception as e:
                print(f"Error generating QR code for {titre} by {artiste}: {str(e)}")
    
    
    
                    
    
            
# Exemple d'utilisation des methodes


import scraping as scraping
from scraping import WikipediaScraper
from single import Single#spotify est un module que j'ai creer 
from manager import Manager


# URL de la page à extraire
url = "https://fr.wikipedia.org/wiki/Liste_des_singles_num%C3%A9ro_un_en_France"

# Création de l'objet WikipediaScraper
scraper = WikipediaScraper(url)

# Extraction des détails des singles
scraper.scrape()

#scraper.generate_qr_codes()








# Test de la méthode get_singles_info
#singles = scraper.inserer_dans_liste()

# Affichage des informations des singles
#for single in singles:
 #   print(f"Title: {single.title}")
  #  print(f"Artist: {single.artist}")
    
   # print("----------------------------")


#scraper.inserer_dans_base_de_donnees3()


#scraper.afficher_infos_artistes()

     

# Exemple d'utilisation pour Recherche des extraits audio
#scraper.rechercher_extraits_audio()

# Exemple d'utilisation afficher les infos
#scraper.afficher_artistes_titres()

# Exemple d'utilisation pour rechercher des singles 
#scraper.rechercher_singles()

# Insérer les informations des singles dans la base de données


