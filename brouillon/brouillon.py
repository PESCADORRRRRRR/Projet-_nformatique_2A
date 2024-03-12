import qrcode
import os

# Texte à convertir en QR code
texte = "https://open.spotify.com/track/4ogT4OJXV0yxFvl4yCIZmm"

# Création de l'objet QRCode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Ajout du contenu au QR code
qr.add_data(texte)
qr.make(fit=True)




# Spécifiez le nom du dossier dans lequel vous souhaitez enregistrer le QR code
nom_dossier = "QRCODE"

# Obtenez le chemin absolu du dossier en utilisant le chemin courant du script
chemin_dossier = os.path.abspath(nom_dossier)

# Créez le dossier s'il n'existe pas déjà
os.makedirs(chemin_dossier, exist_ok=True)

# Enregistrez l'image du QR code dans le dossier spécifié avec un nom de fichier unique
nom_fichier = "qr_code1.png"
chemin_fichier = os.path.join(chemin_dossier, nom_fichier)

image = qr.make_image(fill_color="black", back_color="white")
image.save(chemin_fichier)

# Création de l'image du QR code
image = qr.make_image(fill_color="black", back_color="white")

# Enregistrement de l'image
image.save("qr_code.png")