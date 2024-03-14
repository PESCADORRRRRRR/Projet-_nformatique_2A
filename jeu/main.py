from service_jeu import Partie , Joueur
import tkinter as tk


class InterfaceGraphique(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Nom de votre jeu")
        self.partie = Partie()  # Créez une instance de votre classe Partie
        self.creer_interface()

    def creer_interface(self):
        label_titre = tk.Label(self, text="Bienvenue dans votre jeu")
        label_titre.pack()

        bouton_demarrer = tk.Button(self, text="Démarrer", command=self.lancer_partie)
        bouton_demarrer.pack()

        label_instructions = tk.Label(self, text="Cliquez sur le bouton Démarrer pour commencer la partie")
        label_instructions.pack()

        label_scores = tk.Label(self, text="Scores:")
        label_scores.pack()

        for joueur in self.partie.joueurs:
            label_joueur = tk.Label(self, text=f"{joueur.nom}: {joueur.score}")
            label_joueur.pack()

        bouton_quitter = tk.Button(self, text="Quitter", command=self.quitter_partie)
        bouton_quitter.pack()

    def lancer_partie(self):
        self.partie.lancer_partie()

        # Mettez à jour les scores des joueurs dans l'interface graphique
        for widget in self.winfo_children():
            if isinstance(widget, tk.Label) and widget.winfo_text().startswith("Scores:"):
                widget.destroy()

        label_scores = tk.Label(self, text="Scores:")
        label_scores.pack()

        for joueur in self.partie.joueurs:
            label_joueur = tk.Label(self, text=f"{joueur.nom}: {joueur.score}")
            label_joueur.pack()

    def quitter_partie(self):
        self.destroy()
# Créez une instance de votre classe InterfaceGraphique
interface = InterfaceGraphique()

# Exécutez l'application Tkinter
interface.mainloop()