from QR_code import QRCodeGenerator
from code_pdf import PDFGenerator

# URL de la page à extraire
url = "https://fr.wikipedia.org/wiki/Liste_des_singles_num%C3%A9ro_un_en_France"

# Création de l'objet QRCodeGenerator
qr_generator = QRCodeGenerator(url)

# Génération des codes QR
nom_dossier_qr_codes = "image_qr_code"
qr_generator.generate_qr_code(nom_dossier_qr_codes)

# Vérification si la génération des codes QR est terminée
while not qr_generator.is_generation_completed():
    continue

# Création de l'objet PDFGenerator
pdf_generator = PDFGenerator(url)

# Vérification si la génération des codes QR est terminée avant de générer les fichiers PDF
#Tant que la génération des codes QR n'est pas terminée, la génération des fichiers PDF des cartes ne commencera pas. 
if qr_generator.is_generation_completed():
    # Génération des fichiers PDF
    nom_dossier_sortie_pdf = "PDF"
    dimension_qr_code = 400
    pdf_generator.generate_PDF(nom_dossier_qr_codes, nom_dossier_sortie_pdf, dimension_qr_code)
else:
    print("La génération des codes QR n'est pas terminée. Veuillez patienter.")