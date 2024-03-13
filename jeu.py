import random
import os

class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.score = 0

    def incrementer_score(self):
        self.score += 1

class Partie:
    def __init__(self, joueurs, dossier_qr_codes):
        self.joueurs = joueurs
        self.dossier_qr_codes = dossier_qr_codes
        self.score_max = 10

    def choisir_qr_code_au_hasard(self):
        qr_codes = os.listdir(self.dossier_qr_codes)
        qr_code_choisi = random.choice(qr_codes)
        return qr_code_choisi

    def poser_question_au_joueur(self, joueur):
        reponse = input(f"{joueur.nom}, êtes-vous prêt à jouer ? (Oui/Non) : ")
        return reponse.lower() == "oui"

    def poser_question_au_jury(self, jury):
        reponse = input(f"{jury.nom}, le joueur a-t-il trouvé la musique ? (Oui/Non) : ")
        return reponse.lower() == "oui"
    
    def demander_nombre_joueurs():
        nombre_joueurs = input("Entrez le nombre de joueurs : ")
        return int(nombre_joueurs)
        
    def demander_noms_joueurs(nombre_joueurs):
        joueurs = []
        for i in range(nombre_joueurs):
            nom_joueur = input(f"Entrez le nom du joueur {i+1} : ")
            joueur = Joueur(nom_joueur)
            joueurs.append(joueur)
        return joueurs

    def demander_lancement_partie():
        lancement = input("Êtes-vous prêt à lancer la partie ? (Oui/Non) : ")
        return lancement.lower() == "oui"

    def lancer_partie(self):
        nombre_joueurs = self.demander_nombre_joueurs()
        joueurs = self.demander_noms_joueurs(nombre_joueurs)
        
        
        if self.demander_lancement_partie():
            print("La partie va commencer !")
            joueur_actuel = self.joueurs[0]
            jurie = None
            score_joueurs = {joueur: 0 for joueur in joueurs}
            score_max = 10

            while True:
                print(f"C'est au tour de {joueur_actuel.nom} de jouer.")

                if jurie:
                    print(f"{joueur_actuel.nom} est le joueur en jeu et {jurie.nom} est le jury.")

                if self.poser_question_au_joueur(joueur_actuel):
                    qr_code_choisi = self.choisir_qr_code_au_hasard()
                    print(f"QR code choisi : {qr_code_choisi}")

                    if self.poser_question_au_jury(jurie):
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
                jurie = Jury(joueur_actuel.nom)


class Jury(Joueur):
    def __init__(self, nom):
        super().__init__(nom)
        
        
        
        

dossier_qr_codes = "chemin/vers/le/dossier/qr_codes"

partie=Partie()

partie.lancer_partie(dossier_qr_codes)