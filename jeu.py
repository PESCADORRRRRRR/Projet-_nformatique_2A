import random
import os
from PIL import Image

# Spécifiez le nom du dossier principal
nom_dossier = "dossiers_de_sorties"

# Spécifiez le nom du sous-dossier
nom_s_dossier = "image_qr_code"

# Obtenez le chemin absolu du dossier principal en utilisant le chemin courant du script
chemin_dossier_principal = os.path.abspath(nom_dossier)

# Obtenez le chemin absolu du sous-dossier en utilisant os.path.join() pour concaténer les noms de dossiers
chemin_sous_dossier = os.path.join(chemin_dossier_principal, nom_s_dossier)

class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.score = 0

    def incrementer_score(self):
        self.score += 1

class Partie:
    def __init__(self):
        self.joueurs = []
        self.dossier_qr_codes = chemin_sous_dossier
        self.score_max = 10

    def choisir_qr_code_au_hasard(self):
        qr_codes = os.listdir(self.dossier_qr_codes)
        qr_code_choisi = random.choice(qr_codes)
        return qr_code_choisi

    def poser_question_au_joueur(self, joueur):
        reponse = input(f"{joueur.nom}, êtes-vous prêt à jouer ? (Oui/Non) : ")
        return reponse.lower() == "oui"
    

    def afficher_qr_code(self, image_qr_code):
        chemin_image = os.path.join(chemin_sous_dossier, image_qr_code)
        image = Image.open(chemin_image)
        image.show()

    def poser_question_au_jury(self, jury):
        reponse = input(f"{jury.nom}, le joueur a-t-il trouvé la musique ? (Oui/Non) : ")
        return reponse.lower() == "oui"
    
    def demander_nombre_joueurs(self):
        nombre_joueurs = input("Entrez le nombre de joueurs : ")
        return int(nombre_joueurs)
        
    def demander_noms_joueurs(self, nombre_joueurs):
        joueurs = []
        for i in range(nombre_joueurs):
            nom_joueur = input(f"Entrez le nom du joueur {i+1} : ")
            joueur = Joueur(nom_joueur)
            joueurs.append(joueur)
        return joueurs

    def demander_lancement_partie(self):
        lancement = input("Êtes-vous prêt à lancer la partie ? (Oui/Non) : ")
        return lancement.lower() == "oui"

    def lancer_partie(self):
        nombre_joueurs = self.demander_nombre_joueurs()
        self.joueurs = self.demander_noms_joueurs(nombre_joueurs)

        if self.demander_lancement_partie():
            print("La partie va commencer !")
            joueur_actuel = self.joueurs[0]
            jury = self.joueurs[1]

            while True:
                print(f"C'est au tour de {joueur_actuel.nom} de jouer.")

                if jury:
                    print(f"{joueur_actuel.nom} est le joueur en jeu et {jury.nom} est le jury.")

                if self.poser_question_au_joueur(joueur_actuel):
                    qr_code_choisi = self.choisir_qr_code_au_hasard()
                    print(f"QR code choisi : {qr_code_choisi}")
                    # Afficher le QR code
                    self.afficher_qr_code(qr_code_choisi)

                    if jury and self.poser_question_au_jury(jury):
                        joueur_actuel.incrementer_score()
                        print(f"Le joueur {joueur_actuel.nom} a trouvé la musique et gagne 1 point !")
                        if joueur_actuel.score >= self.score_max:
                            print(f"Le joueur {joueur_actuel.nom} a atteint {self.score_max} points. Il remporte la partie !")
                            break
                    else:
                        print(f"Le joueur {joueur_actuel.nom} n'a pas trouvé la musique.")
                else:
                    print(f"Le joueur {joueur_actuel.nom} choisit de ne pas jouer cette fois-ci.")

                index_joueur_suivant = (self.joueurs.index(joueur_actuel) + 1) % len(self.joueurs)
                joueur_actuel = self.joueurs[index_joueur_suivant]
                
                index_jury_suivant = (index_joueur_suivant + 1) % len(self.joueurs)
                jury = self.joueurs[index_jury_suivant]

                # Afficher le score de chaque joueur avant que le joueur suivant ne commence à jouer
                print("Scores actuels :")
                for joueur in self.joueurs:
                    print(f"Score de {joueur.nom} : {joueur.score}")

            # Afficher le score final de chaque joueur
            print("Scores finaux :")
            for joueur in self.joueurs:
                print(f"Score de {joueur.nom} : {joueur.score}")

class Jury(Joueur):
    def __init__(self, nom):
        super().__init__(nom)


partie = Partie()
partie.lancer_partie()