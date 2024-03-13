# Importation des bibliothèques nécessaires
from bs4 import BeautifulSoup
import requests
from single import Single  # spotify est un module que j'ai creer
from manager import Manager
import sqlite3
from datetime import datetime
import os
import qrcode
from reportlab.lib.pagesizes import letter

from reportlab.pdfgen import canvas
from PIL import Image


from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas




class WikipediaScraper:
    """
    Classe utilisée pour extraire et manipuler les données des singles numéro un en France à partir de Wikipedia.
    """

    def __init__(self, url):
        """
        Initialise une instance de la classe WikipediaScraper.

        :param url: L'URL de la page Wikipedia contenant les informations sur les singles numéro un en France.
        """

        self.url = url
        self.singles = []
        self.db_conn = sqlite3.connect("base_donnee.db")
        self.db_cursor = self.db_conn.cursor()

    def scrape(self):
        """
        Récupère les informations des singles numéro un en France à partir de la page Wikipedia spécifiée dans l'URL.
        """

        try:
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
                        single = {"titre": titre, "artiste": artiste, "date": date}

                        # Ajout du dictionnaire à la liste des singles
                        self.singles.append(single)

        except requests.exceptions.RequestException as e:
            print("Erreur lors de la requête HTTP :", e)
        except Exception as e:
            print("Une erreur inattendue s'est produite :", e)

    def afficher_artistes_titres(self):
        """
        Affiche les artistes et les titres des singles.
        """

        if self.singles:
            for single in self.singles:
                try:

                    single_instance = Single(
                        single["titre"], single["artiste"], single["date"]
                    )
                    single_instance.afficher_informations()
                    print("-------------------")
                except Exception as e:
                    print(
                        "Une erreur s'est produite lors de l'affichage des informations :",
                        e,
                    )
        else:
            print("Aucun single trouvé.")

    def rechercher_extraits_audio(self):
        """
        Recherche et joue les extraits audio des singles.
        """

        if self.singles:
            for single in self.singles:
                single_instance = Single(
                    single["titre"], single["artiste"], single["date"]
                )
                single_instance.afficher_informations()
                single_instance.jouer_extrait_audio()
                print("-------------------")
        else:
            print("Aucun single trouvé.")

    def rechercher_singles(self):
        """
        Recherche les singles en fonction du critère spécifié par l'utilisateur.
        """
        try:
            # Demander à l'utilisateur de saisir le critère de recherche et la valeur de recherche
            critere = input(
                "Entrez le critère de recherche (titre, artiste ou date) : "
            )
            valeur_recherche = input("Entrez la valeur de recherche : ")

            # Créer une liste pour stocker les singles correspondants à la recherche
            singles_recherches = []

            # Parcourir la liste des singles extraits
            for single in self.singles:
                try:
                    # Vérifier si le critère de recherche est "titre" et si la valeur de recherche est présente dans le titre du single
                    if (
                        critere.lower() == "titre"
                        and valeur_recherche.lower() in single["titre"].lower()
                    ):
                        singles_recherches.append(single)
                    # Vérifier si le critère de recherche est "artiste" et si la valeur de recherche est présente dans le nom de l'artiste du single
                    elif (
                        critere.lower() == "artiste"
                        and valeur_recherche.lower() in single["artiste"].lower()
                    ):
                        singles_recherches.append(single)
                    # Vérifier si le critère de recherche est "date" et si la valeur de recherche est présente dans la date du single
                    elif (
                        critere.lower() == "date"
                        and valeur_recherche.lower() in single["date"].lower()
                    ):
                        singles_recherches.append(single)
                except Exception as e:
                    print("Erreur lors de la recherche des singles :", e)

            # Vérifier si des singles correspondants ont été trouvés
            if singles_recherches:
                # Parcourir les singles correspondants et afficher leurs informations
                for single in singles_recherches:
                    try:
                        single_instance = Single(
                            single["titre"], single["artiste"], single["date"]
                        )
                        single_instance.afficher_informations()
                        print("-------------------")
                    except Exception as e:
                        print(
                            "Erreur lors de l'affichage des informations du single :", e
                        )
            else:
                print("Aucun single trouvé pour la valeur de recherche spécifiée.")
        except Exception as e:
            print("Erreur lors de la recherche des singles :", e)

    def inserer_dans_liste(self):
        """
        Insère les données des singles dans une liste et renvoie la liste des singles.

        :return: La liste des singles avec leurs informations.

        """

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
                if "," in date:
                    # Diviser la chaîne en une liste de dates individuelles
                    dates = date.split(",")
                else:
                    dates = [date]

                # Convertir chaque date au format 'DD/MM/YYYY' en 'YYYY-MM-DD' et insérer individuellement
                for date in dates:
                    # Supprimer les espaces avant et après la chaîne de caractères de la date
                    date = date.strip()

                    # Supprimer le "[1]" à la fin de la date, s'il est présent
                    if "[1]" in date:
                        date = date.split("[1]")[0]

                    formatted_date = datetime.strptime(date, "%d/%m/%Y").strftime(
                        "%Y-%m-%d"
                    )

                    # Créer un dictionnaire avec les détails du single
                    single_info = {
                        "titre": titre,
                        "artiste": artiste,
                        "date": formatted_date,
                        "lien_spotify": lien_spotify,
                        "extrait_audio": extrait_audio,
                    }

                    # Ajouter le dictionnaire à la liste des singles
                    singles.append(single_info)

            except ValueError:
                print("Erreur lors de la conversion de la date")

        return singles

    
    def generate_qr_codes(self, nom_dossier_sortie_qr_code):
        """
        Génère des codes QR pour les données des singles et les enregistre dans un dossier spécifié.

        :param nom_dossier_sortie_qr_code: Le nom du dossier de sortie pour les codes QR.

        """
        
        # Spécifiez le nom du dossier principal
        nom_dossier = "dossiers_de_sorties"

        # Spécifiez le nom du sous-dossier
        nom_s_dossier = nom_dossier_sortie_qr_code

        # Obtenez le chemin absolu du dossier principal en utilisant le chemin courant du script
        chemin_dossier_principal = os.path.abspath(nom_dossier)

        # Obtenez le chemin absolu du sous-dossier en utilisant os.path.join() pour concaténer les noms de dossiers
        chemin_sous_dossier = os.path.join(chemin_dossier_principal, nom_s_dossier)

        # Créez le dossier s'il n'existe pas déjà
        os.makedirs(chemin_sous_dossier, exist_ok=True)

        for single_data in self.singles:
            titre = single_data.get("titre", "")
            artiste = single_data.get("artiste", "")
            date_str = single_data.get("date", "")

            # Conversion de la chaîne de caractères en date
            date_list = date_str.split(',')
            for date_str in date_list:
                try:
                    date = datetime.strptime(date_str.strip(), "%d/%m/%Y")

                    # Extraction de l'année
                    annee = date.year

                    single = Single(
                        single_data["titre"], single_data["artiste"], single_data["date"]
                    )

                    audio_info = single.rechercher_audio_artiste_titre()

                    lien_spotify = audio_info.get("lien_spotify") if audio_info else None
                    extrait_audio = audio_info.get("extrait_audio") if audio_info else None

                    lien = lien_spotify
                    qr = qrcode.QRCode(
                        version=1,
                        error_correction=qrcode.constants.ERROR_CORRECT_L,
                        box_size=10,
                        border=4,
                    )
                    if extrait_audio is not None:
                        lien = extrait_audio

                    if lien is not None:
                        qr.add_data(lien)
                        qr.make(fit=True)

                        # Enregistrez l'image du QR code dans le dossier spécifié avec un nom de fichier unique
                        nom_fichier = f"qr_code_{titre}_{artiste}_{annee}.png"
                        chemin_fichier = os.path.join(chemin_sous_dossier, nom_fichier)

                        image = qr.make_image(fill_color="black", back_color="white")
                        image.save(chemin_fichier)

                except Exception as e:
                    print(f"Erreur lors de la génération du code QR pour {titre} par {artiste} : {str(e)}")
    
              
                
    def generate_PDF(self, nom_dossier_qr_codes, nom_dossier_sortie_pdf,dimension_qr_code):
        """
        Génère des fichiers PDF à partir des codes QR contenus dans un dossier spécifié.

        Args:
            nom_dossier_qr_codes (str): Le nom du dossier contenant les codes QR.
            nom_dossier_sortie_pdf (str): Le nom du dossier de sortie pour les fichiers PDF.

        Returns:
            None

        Raises:
            FileNotFoundError: Si le dossier contenant les codes QR ou le dossier de sortie pour les PDF n'existe pas.
            Exception: Si une erreur survient lors de la génération des PDF.

        """
        try:
            # Spécifiez le nom du dossier principal
            nom_dossier = "dossiers_de_sorties"

            # Obtenez le chemin absolu du dossier principal en utilisant le chemin courant du script
            chemin_dossier_principal = os.path.abspath(nom_dossier)

            # Obtenez le chemin absolu du dossier contenant les codes QR
            chemin_dossier_qr_codes = os.path.join(chemin_dossier_principal, nom_dossier_qr_codes)

            # Obtenez le chemin absolu du dossier de sortie pour les PDF
            chemin_dossier_sortie_pdf = os.path.join(chemin_dossier_principal, nom_dossier_sortie_pdf)

            dimension =dimension_qr_code

            # Vérifiez si le dossier contenant les codes QR existe
            if not os.path.exists(chemin_dossier_qr_codes):
                raise FileNotFoundError(f"Le dossier '{nom_dossier_qr_codes}' n'existe pas.")

            # Créez le dossier de sortie pour les PDF s'il n'existe pas déjà
            os.makedirs(chemin_dossier_sortie_pdf, exist_ok=True)

            # Parcourez les fichiers des codes QR
            for nom_fichier in os.listdir(chemin_dossier_qr_codes):
                if nom_fichier.endswith(".png"):
                    chemin_fichier_qr_code = os.path.join(chemin_dossier_qr_codes, nom_fichier)

                    # Créez un nouveau PDF pour chaque code QR
                    nom_fichier_pdf = f"{nom_fichier[:-4]}.pdf"
                    chemin_fichier_pdf = os.path.join(chemin_dossier_sortie_pdf, nom_fichier_pdf)

                    try:
                        
                        # Créez un objet Canvas pour le PDF
                        
                        pdf = canvas.Canvas(chemin_fichier_pdf, pagesize=landscape(letter))

                        # Supprimez la partie "qr_code_" au début du nom de fichier
                        nom_fichier_sans_prefixe = nom_fichier.replace("qr_code_", "")

                        # Supprimez l'extension ".png" à la fin du nom de fichier
                        nom_fichier_sans_extension = nom_fichier_sans_prefixe.replace(".png", "")

                        # Divisez le nom de fichier en utilisant le caractère "_" comme séparateur
                        elements = nom_fichier_sans_extension.split("_")

                        # Le premier élément de la liste est le titre
                        titre = elements[0]

                        # Le deuxième élément de la liste est l'artiste
                        artiste = elements[1]

                        # Le troisième élément de la liste est l'année
                        annee = elements[2]

                        # Calculez les coordonnées pour placer le carré au centre de la page
                        page_width, page_height = landscape(letter)
                        square_size = dimension # Taille du carré
                        square_x = (page_width - square_size) / 2
                        square_y = (page_height - square_size) / 2

                        # Dessinez le carré sur la première page du PDF
                        pdf.rect(square_x, square_y, square_size, square_size)
                        pdf.setFont("Helvetica", 12)

                        # Calculez les coordonnées pour placer le texte dans le carré
                        text_x = square_x + 10
                        text_y = square_y + square_size - 50  # Décalez légèrement le titre vers le haut

                        # Vérifiez si le texte du titre dépasse le carré
                        if pdf.stringWidth(titre, "Helvetica-Bold", 30) > square_size - 20:
                            pdf.setFont("Helvetica-Bold", 20)  # Réduisez la taille de police pour le titre
                            pdf.drawCentredString(square_x + (square_size / 2), text_y, titre[:30] + "\n" + titre[30:])
                        else:
                            pdf.setFont("Helvetica-Bold", 30)  # Utilisez la taille de police normale pour le titre
                            pdf.drawCentredString(square_x + (square_size / 2), text_y, titre)

                        # Calculez les coordonnées pour placer le texte de l'artiste dans le carré
                        text_x = square_x + 10
                        text_y = square_y + 30  # Décalez légèrement l'artiste vers le bas

                        # Vérifiez si le texte de l'artiste dépasse le carré
                        if pdf.stringWidth(artiste, "Helvetica", 30) > square_size - 20:
                            pdf.setFont("Helvetica", 20)  # Réduisez la taille de police pour l'artiste
                            pdf.drawCentredString(square_x + (square_size / 2), text_y, artiste[:30] + "\n" + artiste[30:])
                        else:
                            pdf.setFont("Helvetica", 30)  # Utilisez la taille de police normale pour l'artiste
                            pdf.drawCentredString(square_x + (square_size / 2), text_y, artiste)

                        # Vérifiez si le texte de l'année dépasse le carré
                        if pdf.stringWidth(annee, "Helvetica", 60) > square_size - 20:
                            pdf.setFont("Helvetica", 40)  # Réduisez la taille de police pour l'année
                            pdf.drawCentredString(square_x + (square_size / 2), square_y + (square_size / 2), annee[:4] + "\n" + annee[4:])
                        else:
                            pdf.setFont("Helvetica", 60)  # Utilisez la taille de police normale pour l'année
                            pdf.drawCentredString(square_x + (square_size / 2), square_y + (square_size / 2), annee)

                        # Ajoutez le code QR sur la deuxième page du PDF
                        pdf.showPage()
                        # Calculez les coordonnées pour centrer le code QR
                        
                        qr_code_width = dimension
                        qr_code_height = dimension
                        qr_code_x = (page_width - qr_code_width) / 2
                        qr_code_y = (page_height - qr_code_height) / 2

                        pdf.drawInlineImage(chemin_fichier_qr_code, qr_code_x, qr_code_y, width=qr_code_width, height=qr_code_height)

                        # Sauvegardez le PDF
                        pdf.save()

                    except Exception as e:
                        print(f"Une erreur est survenue lors de la génération du PDF '{nom_fichier_pdf}': {e}")

        except FileNotFoundError as e:
            print(e)
        except Exception as e:
            print(f"Une erreur est survenue lors de la génération des PDF : {e}")
    
    
    
# Exemple d'utilisation des methodes


import scraping as scraping
from scraping import WikipediaScraper
from single import Single  # spotify est un module que j'ai creer
from manager import Manager


# URL de la page à extraire
url = "https://fr.wikipedia.org/wiki/Liste_des_singles_num%C3%A9ro_un_en_France"

# Création de l'objet WikipediaScraper
scraper = WikipediaScraper(url)

# Extraction des détails des singles
scraper.scrape()

# scraper.rechercher_extraits_audio()

# Génération des codes QR
nom_dossier_sortie_pdf = "PDF"
nom_dossier_qr_codes = "image_qr_code"
dimension_qr_code= 400
#scraper.generate_qr_codes(nom_dossier_qr_codes)

scraper.generate_PDF(nom_dossier_qr_codes, nom_dossier_sortie_pdf,dimension_qr_code)


# Test de la méthode get_singles_info
# singles = scraper.inserer_dans_liste()

# Affichage des informations des singles
# for single in singles:
#   print(f"Title: {single.title}")
#  print(f"Artist: {single.artist}")

# print("----------------------------")


# scraper.inserer_dans_base_de_donnees3()


# scraper.afficher_infos_artistes()


# Exemple d'utilisation pour Recherche des extraits audio
# scraper.rechercher_extraits_audio()

# Exemple d'utilisation afficher les infos
# scraper.afficher_artistes_titres()

# Exemple d'utilisation pour rechercher des singles
# scraper.rechercher_singles()

# Insérer les informations des singles dans la base de données
