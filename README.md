# Génération de cartes pour un jeu de société quizz musical - Hitster

Ce projet vise à générer des cartes pour un jeu de société quizz musical basé sur le concept de Hitster. Hitster est un jeu de quizz musical dans lequel les joueurs doivent retrouver le titre et l'artiste de différents titres populaires de différentes époques, et les ordonner dans l'ordre chronologique.

## Concept

Le jeu de société Hitster utilise des cartes qui contiennent un QR code vers un extrait audio du titre sur Spotify, ainsi que des informations telles que l'année, l'artiste et le titre de la chanson. L'objectif de ce projet est de générer notre propre jeu Hitster, car le jeu de base est limité en termes de cartes.

## Implémentation

Nous utilisons l'API Spotify pour récupérer les informations sur les titres musicaux, y compris les extraits audio. Nous extrayons également les données à partir de la liste des singles numéro un en France disponible sur Wikipedia. Les étapes d'implémentation comprennent :

1. Scraping de la liste des singles numéro un en France à partir de la page Wikipedia.

2. Récupération des informations sur les titres musicaux à partir de l'API Spotify en utilisant un jeton d'API valide.

3. Recherche des extraits audio correspondants à chaque titre à l'aide de l'API Spotify.

4. Génération de fichiers PDF pour chaque extrait audio contenant un QR code vers l'extrait et les informations sur l'artiste, le titre et la date de l'œuvre.

Les fichiers PDF générés peuvent ensuite être imprimés et utilisés comme cartes dans le jeu de société Hitster.


## Prérequis

vant d'exécuter le code, vous devez vous assurer d'avoir les éléments suivants :

- Un jeton d'API valide pour accéder à l'API Spotify.
- Les bibliothèques et dépendances requises, qui sont répertoriées dans le fichier requirements.txt.

## Utilisation

1. Exécutez le script main.py pour générer les codes QR et les fichiers PDF. Tant que la génération des codes QR n'est pas terminée, la génération des fichiers PDF des cartes ne commencera pas.

2. Les fichiers PDF seront enregistrés dans le dossier  dossiers_de_sorties/.

3. Vous pouvez maintenant imprimer les fichiers PDF et les utiliser dans le jeu de société Hitster.

## Installation

Trois options d'installation sont disponibles :

1. ## Installation avec Docker (recommandé)

- Assurez-vous d'avoir Docker installé sur votre machine: [Lien pour cloner le dépôt.](https://github.com/PESCADORRRRRRR/Projet-_nformatique_2A/tree/main)

- Installer Docker.
- Construire l'image Docker :
   - Ouvrez un terminal et accédez au répertoire du projet.
   - Exécutez la commande suivante : docker build -t my-app ...
- Exécuter le conteneur Docker :
    - Exécutez la commande suivante : docker run -it my-app.

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
pylint QR_code.py
pylint code_pdf.py
pylint jeu.py
pylint main.py


## Dépendances

Ce projet utilise les dépendances suivantes :

- beautifulsoup4==4.10.0
- qrcode==1.15.0
- requests==2.27.1



## Tests

Ce projet comprend des tests pour garantir la qualité du code et la fiabilité des fonctionnalités. Les tests sont organisés en plusieurs catégories : tests unitaires, tests statiques et tests d'isolation.

### Exécution des tests

Pour exécuter tous les tests, vous devez avoir l'environnement Tox installé. Si vous ne l'avez pas encore, vous pouvez l'installer en utilisant la commande suivante :

```shell
pip install tox
```

Pour exécuter les tests, suivez les étapes suivantes :

1. Installez les dépendances nécessaires :
pip install pytest coverage

2. À la racine du projet, exécutez la commande suivante pour lancer les tests dans des environnements virtuels isolés :

```
  tox 
```
Cela exécutera les tests dans des environnements virtuels isolés afin de garantir la reproductibilité des résultats.


3. Si vous souhaitez exécuter des tests spécifiques pour un environnement Python particulier, utilisez la commande appropriée :
- Pour exécuter les tests unitaires et statiques :
  ```
  tox -e py
  ```
- Pour exécuter les tests d'isolation :
  ```
  tox -e isolation
  ```
- Pour exécuter les tests fonctionnels :
  ```
  tox -e fonctionnels
 
  ```

Cela exécutera les tests correspondants à partir des dossiers de tests spécifiés dans le fichier `tox.ini`. Assurez-vous de vérifier les résultats des tests et de résoudre tout problème avant de soumettre des contributions.

N'hésitez pas à consulter le fichier `tox.ini` pour plus de détails sur la configuration des tests.

#### Organisation des tests
Les tests sont organisés en trois catégories principales :

-Tests unitaires : Ils vérifient le bon fonctionnement des différentes unités de code, telles que les fonctions, les méthodes ou les classes. Les fichiers de test correspondants se trouvent dans le répertoire tests/tests_unitaires et ont des noms se terminant par tests.py.

-Tests statiques : Ils vérifient la conformité du code aux normes de style et aux bonnes pratiques. Ces tests sont utiles pour assurer la lisibilité et la maintenabilité du code. Les fichiers de test correspondants se trouvent dans le répertoire tests/_tests_static et ont des noms se terminant par _tests.py.

-Tests d'isolation : Ils vérifient l'isolation des fonctionnalités et des dépendances. Ces tests sont importants pour s'assurer qu'une unité de code fonctionne correctement de manière indépendante sans interférence avec d'autres parties du système. Les fichiers de test correspondants se trouvent dans le répertoire tests/tests_isolation et ont des noms se terminant par _tests.py.

## Diagrammes de Classe

Ce projet utilise des diagrammes de classe pour visualiser la structure et les relations des classes. Vous pouvez trouver les fichiers HTML correspondants dans le dossier "diagramme de class". Voici une description de chaque diagramme de classe :

- ###### diagramme_manager.html : 
Un diagramme de classe représentant la classe Manager et la classe SpotifyAPI. Il montre les attributs, les méthodes et les relations entre les classes.

- ###### diagramme_pdf.html : 
Un diagramme de classe représentant la classe PDFGenerator et la classe WikipediaScraper. Il montre les attributs, les méthodes et les relations entre les classes.

- ###### diagramme_QR.html : 
Un diagramme de classe représentant la classe QRCodeGenerator et la classe WikipediaScraper. Il montre les attributs, les méthodes et les relations entre les classes.

- ###### diagramme_single.html : 
Un diagramme de classe représentant la classe Single et la classe Manager. Il montre les attributs et les méthodes de chaque classe.



## Auteurs

Goua Beedi Henri

## Licence
Ce projet est sous licence MIT License. Veuillez consulter le fichier LICENSE pour plus de détails.

La licence MIT est une licence open source permissive qui permet à quiconque d'utiliser, de modifier, de distribuer et de vendre votre logiciel, à condition que le copyright et l'avis de licence soient inclus dans toutes les copies du logiciel. Elle offre une flexibilité et une liberté considérables pour les utilisateurs et les contributeurs du projet.


## Conclusion

La génération de cartes pour un jeu de société quizz musical basé sur le concept de Hitster offre une expérience divertissante aux joueurs. En utilisant des API telles que Spotify  et en extrayant les informations de la liste des singles numéro un en France depuis Wikipedia, nous pouvons créer un jeu personnalisé avec une variété de titres musicaux.

Ce projet permet aux joueurs de tester leurs connaissances musicales en retrouvant le titre, l'artiste et l'année de différents titres populaires. Les cartes générées, avec les QR codes vers les extraits audio, offrent une interaction ludique et immersive.

En suivant les étapes d'implémentation décrites dans ce projet, vous serez en mesure de générer vos propres cartes pour le jeu de société Hitster. Assurez-vous de respecter les conditions d'utilisation des API et des sources de données pour une utilisation légale et éthique.

N'hésitez pas à personnaliser ce projet en ajoutant de nouvelles fonctionnalités ou en adaptant le code selon vos besoins et vos préférences. Amusez-vous bien et profitez du jeu de société quizz musical !

## Code source

[Lien vers le dépôt de code source du projet.](https://github.com/PESCADORRRRRRR/Projet-_nformatique_2A/tree/main)