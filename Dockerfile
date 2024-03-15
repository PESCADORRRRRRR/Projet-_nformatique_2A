# Utilisez une image de base appropriée pour votre application Python
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers requis dans le conteneur
COPY main.py .
COPY QR_code.py .
COPY code_pdf.py .
COPY requirements.txt .

# Installer les dépendances de votre application
RUN pip install --no-cache-dir -r requirements.txt

# Exécuter votre application lorsque le conteneur démarre
CMD ["python", "main.py"]