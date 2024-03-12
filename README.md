# Titre du projet

## Description



## Installation

Deux options d'installation sont disponibles :

1. **Installation avec Docker (recommandé) :**

   - Installer Docker.
   - Construire l'image Docker :
     - Ouvrez un terminal et accédez au répertoire du projet.
     - Exécutez la commande suivante : `docker build -t my-app ..`.
   - Exécuter le conteneur Docker :
     - Exécutez la commande suivante : `docker run -it my-app`.

2. **Installation manuelle :**

   Pour installer les dépendances nécessaires à l'exécution de ce projet, veuillez suivre les étapes suivantes :

   1. Installer Python 3.8 ou supérieur.
   2. Installer Poetry.
   3. Installer les dépendances du projet.

   Le fichier `requirements.txt` est situé dans le même dossier que ce fichier README.

   Remarques :
   - Vous pouvez également installer les dépendances manuellement en utilisant la commande `pip install -r requirements.txt`.

3. **Intallation et utilisation Linting avec Pylint (recommandé) :**

Assurez-vous d'avoir Python 3.8 ou supérieur installé.
Installez Pylint avec la commande suivante :
pip3 install black isort pylint


Exécution de Pylint:

Ouvrez un terminal et accédez au répertoire contenant vos fichiers Python.
Exécutez la commande suivante pour lancer Pylint sur chaque fichier :
pylint scraping.py
pylint manager.py
pylint single.py
pylint qr_code.py

## Dépendances

Ce projet utilise les dépendances suivantes :

- beautifulsoup4==4.10.0
- qrcode==1.15.0
- requests==2.27.1
- spotify (module local)

## Test

Pour exécuter les tests de ce projet, nous utilisons `tox` pour automatiser le processus. Assurez-vous d'avoir `tox` installé sur votre système.

Pour exécuter les tests, suivez les étapes suivantes :

1. Installez les dépendances nécessaires :
pip install pytest coverage

2. À la racine du projet, exécutez `tox` avec la commande appropriée pour l'environnement Python souhaité :
- Pour exécuter les tests unitaires et statiques :
  ```
  tox -e py38
  ```

- Pour exécuter les tests d'isolation :
  ```
  tox -e py39
  ```

- Pour exécuter les tests fonctionnels :
  ```
  tox -e py38-functional  # Pour Python 3.8
  tox -e py39-functional  # Pour Python 3.9
  ```

Cela exécutera les tests correspondants à partir des dossiers de tests spécifiés dans le fichier `tox.ini`. Assurez-vous de vérifier les résultats des tests et de résoudre tout problème avant de soumettre des contributions.

N'hésitez pas à consulter le fichier `tox.ini` pour plus de détails sur la configuration des tests.

## Utilisation



## Auteurs

Goua Beedi Henri

## Licence



## Contact



## Conclusion

Résumé des points forts de votre projet.

## Code source

Lien vers le dépôt de code source du projet.