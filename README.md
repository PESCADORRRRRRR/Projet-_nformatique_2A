# Titre du projet

## Description

Brève description de votre projet.

## Fonctionnalités

Liste des fonctionnalités principales de votre projet.

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


## Test statique 

Tests statiques
Pour exécuter les tests statiques et vérifier la qualité du code, suivez les étapes suivantes :

Assurez-vous d'avoir installé les dépendances nécessaires en suivant les instructions de la section "Installation" du README.

Ouvrez un terminal et accédez au répertoire racine du projet.

Exécutez la commande suivante pour exécuter les tests statiques :

Copy
python -m pytest tests_static/
Cette commande exécutera tous les tests statiques présents dans le dossier tests_static/ et affichera les résultats.

Assurez-vous que tous les tests statiques passent avec succès avant de continuer à travailler sur le projet. Si des erreurs ou des avertissements sont détectés, veuillez les corriger conformément aux normes de qualité du projet.




## Analyse dynamique

### Test unitaire  

Ce projet est livré avec une suite complète de tests unitaires pour vérifier le bon fonctionnement de chaque fonction et module. Les tests unitaires sont écrits en utilisant le framework de tests `unittest` de Python.

Pour exécuter les tests unitaires, vous pouvez utiliser la commande suivante :
python -m unittest discover tests


Les tests unitaires utilisent également des techniques de mocking pour isoler les fonctionnalités spécifiques à tester. Le mocking permet de simuler le comportement de certaines parties de votre code afin de se concentrer uniquement sur la logique que vous souhaitez tester.

Nous utilisons la bibliothèque `unittest.mock` de Python pour effectuer les tests de mocking. Cela nous permet de créer des objets simulés, de définir des comportements spécifiques pour ces objets et de vérifier que les interactions attendues se produisent.

Assurez-vous de lire la documentation des tests unitaires et du mocking pour comprendre comment écrire et exécuter ces tests. Vous pouvez trouver des exemples dans les fichiers de tests du projet.

Il est recommandé d'exécuter les tests unitaires régulièrement, y compris les tests de mocking, pour vous assurer que votre code fonctionne correctement et qu'il répond aux exigences spécifiées.


## Utilisation

Instructions d'utilisation de votre projet.

## Auteurs

Liste des auteurs du projet.

## Licence

Licence du projet.

## Contact

Informations de contact pour les auteurs du projet.

## Conclusion

Résumé des points forts de votre projet.

## Code source

Lien vers le dépôt de code source du projet.