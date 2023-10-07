# Importer les modules nécessaires
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty, ListProperty, StringProperty
from random import randint, choice

# Définir les constantes du jeu
NOMS = ["Alice", "Bob", "Charlie", "David", "Eve", "Fiona", "George", "Helen", "Ivan", "Julia"] # Les noms possibles des joueurs
MAX_JOUEURS = 10 # Le nombre maximum de joueurs
MIN_JOUEURS = 2 # Le nombre minimum de joueurs
EAU_INITIALE = 10 # La quantité initiale d'eau du camp
NOURRITURE_INITIALE = 10 # La quantité initiale de nourriture du camp
BOIS_INITIAL = 0 # La quantité initiale de bois du camp
PLANCHES_INITIALES = 0 # Le nombre initial de planches sur le radeau
PLANCHES_NÉCESSAIRES = 10 # Le nombre de planches nécessaires pour terminer le radeau
EAU_CONSOMMÉE = 1 # La quantité d'eau consommée par joueur par tour
NOURRITURE_CONSOMMÉE = 1 # La quantité de nourriture consommée par joueur par tour
BOIS_CONVERTI = 1 # La quantité de bois convertie en planche par tour
MIN_PÊCHE = 1 # Le nombre minimum de poissons pêchés par tour
MAX_PÊCHE = 3 # Le nombre maximum de poissons pêchés par tour
MIN_BOIS = 1 # Le nombre minimum de bois ramassés par tour
MAX_BOIS = 5 # Le nombre maximum de bois ramassés par tour
PROBA_PIQÛRE = 0.2 # La probabilité d'être piqué en allant chercher du bois
MIN_EAU = 0 # La quantité minimum d'eau récupérée par tour
MAX_EAU = 3 # La quantité maximum d'eau récupérée par tour

# Définir les classes des écrans du jeu

class EcranAccueil(Screen):
    """L'écran d'accueil du jeu, où on peut entrer le nombre de joueurs et lancer la partie."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation="vertical")
        self.label = Label(text="Bienvenue dans le jeu des naufragés !\n\nEntrez le nombre de joueurs (entre {} et {}) et appuyez sur le bouton pour commencer la partie.".format(MIN_JOUEURS, MAX_JOUEURS))
        self.input = TextInput(multiline=False, input_filter="int")
        self.button = Button(text="Lancer la partie")
        self.button.bind(on_press=self.lancer_partie)
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.input)
        self.layout.add_widget(self.button)
        self.add_widget(self.layout)

    def lancer_partie(self, instance):
        """Lance la partie si le nombre de joueurs est valide."""
        try:
            nb_joueurs = int(self.input.text)
            if MIN_JOUEURS <= nb_joueurs <= MAX_JOUEURS:
                self.manager.get_screen("jeu").initialiser_partie(nb_joueurs)
                self.manager.current = "jeu"
            else:
                self.label.text = "Le nombre de joueurs doit être entre {} et {} !".format(MIN_JOUEURS, MAX_JOUEURS)
        except ValueError:
            self.label.text = "Veuillez entrer un nombre entier !"


class EcranJeu(Screen):
    """L'écran du jeu, où les joueurs peuvent effectuer des actions et voir l'état du camp."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation="vertical")
        self.layout_haut = BoxLayout(orientation="horizontal")
        self.layout_bas = BoxLayout(orientation="horizontal")
        self.label_joueur = Label(text="", size_hint=(0.5, 1))
        self.label_camp = Label(text="", size_hint=(0.5, 1))
        self.button_peche = Button(text="Pêcher", size_hint=(0.33, 1))
        self.button_bois = Button(text="Chercher du bois", size_hint=(0.33, 1))
        self.button_eau = Button(text="Récupérer l'eau", size_hint=(0.33, 1))
        self.button_peche.bind(on_press=self.pecher)
        self.button_bois.bind(on_press=self.chercher_bois)
        self.button_eau.bind(on_press=self.recuperer_eau)
        self.layout_haut.add_widget(self.label_joueur)
        self.layout_haut.add_widget(self.label_camp)
        self.layout_bas.add_widget(self.button_peche)
        self.layout_bas.add_widget(self.button_bois)
        self.layout_bas.add_widget(self.button_eau)
        self.layout.add_widget(self.layout_haut)
        self.layout.add_widget(self.layout_bas)
        self.add_widget(self.layout)

    def initialiser_partie(self, nb_joueurs):
        """Initialise la partie avec le nombre de joueurs donné."""
        self.joueurs = [] # La liste des joueurs
        self.eau = EAU_INITIALE # La quantité d'eau du camp
        self.nourriture = NOURRITURE_INITIALE # La quantité de nourriture du camp
        self.bois = BOIS_INITIAL # La quantité de bois du camp
        self.planches = PLANCHES_INITIALES # Le nombre de planches sur le radeau
        self.meteo = randint(MIN_EAU, MAX_EAU) # La quantité d'eau disponible dans le ciel
        for i in range(nb_joueurs):
            nom = choice(NOMS) # Choisir un nom aléatoire
            NOMS.remove(nom) # Retirer le nom de la liste des noms possibles
            joueur = Joueur(nom) # Créer un objet joueur avec le nom choisi
            self.joueurs.append(joueur) # Ajouter le joueur à la liste des joueurs
        self.tour = 0 # Le numéro du tour actuel
        self.joueur_actif = None # Le joueur qui doit jouer
        self.message = "" # Le message à afficher au joueur actif
        self.actualiser_ecran() # Actualiser l'écran avec les informations initiales

    def actualiser_ecran(self):
        """Actualise l'écran avec les informations du jeu."""
        if len(self.joueurs) == 0: # Si tous les joueurs sont morts
            self.label_joueur.text = "Tous les joueurs sont morts !\n\nLa partie est terminée."
            self.label_camp.text = ""
            self.desactiver_boutons()
            return
        if self.planches >= PLANCHES_NÉCESSAIRES: # Si le radeau est terminé
            gagnants = [joueur.nom for joueur in self.joueurs] # La liste des noms des joueurs survivants
            if len(gagnants) == 1: # Si il y a un seul gagnant
                texte_gagnants = gagnants[0] # Le texte à afficher est le nom du gagnant
            else: # Si il y a plusieurs gagnants
                texte_gagnants = ", ".join(gagnants[:-1]) + " et " + gagnants[-1] # Le texte à afficher est la liste des noms séparés par des virgules et un "et" avant le dernier nom
            self.label_joueur.text = "{} ont réussi à quitter l'île à temps !\n\nLa partie est terminée.".format(texte_gagnants)
            self.label_camp.text = ""
            self.desactiver_boutons()
            return
        if not self.joueur_actif: # Si il n'y a pas de joueur actif
            self.joueur_actif = self.joueurs[self.tour % len(self.joueurs)] # Choisir le joueur actif selon le numéro du tour et le nombre de joueurs
            if not (self.eau > 0 and self.nourriture > 0): # Si il n'y a plus d'eau ou de nourriture au camp
                self.manager.get_screen("vote").lancer_vote(self.joueurs) # Lancer un vote pour éliminer un joueur
                return
            else: # Sinon, consommer l'eau et la nourriture du camp pour le joueur actif
                self.eau -= EAU_CONSOMMÉE 
                if not (self.eau > 0 and self.nourriture > 0): #


                self.message = "Attention ! Il n'y a plus assez d'eau ou de nourriture au camp !\n\nUn vote va être organisé pour éliminer un joueur."
                self.actualiser_ecran()
            return
            self.message = "C'est à {} de jouer !\n\nQue voulez-vous faire ?".format(self.joueur_actif.nom)
            self.actualiser_ecran()
            else: # Si il y a un joueur actif
                    self.message += "\n\nC'est toujours à {} de jouer !\n\nQue voulez-vous faire ?".format(self.joueur_actif.nom)
                    self.actualiser_ecran()

    def pecher(self, instance):
        """Permet au joueur actif de pêcher des poissons."""
        nb_poissons = randint(MIN_PÊCHE, MAX_PÊCHE) # Choisir un nombre aléatoire de poissons pêchés
        self.nourriture += nb_poissons # Ajouter les poissons à la nourriture du camp
        self.message = "{} a pêché {} poissons !".format(self.joueur_actif.nom, nb_poissons)
        self.terminer_tour() # Terminer le tour du joueur actif

    def chercher_bois(self, instance):
        """Permet au joueur actif d'aller chercher du bois."""
        nb_bois = randint(MIN_BOIS, MAX_BOIS) # Choisir un nombre aléatoire de bois ramassés
        self.bois += nb_bois # Ajouter le bois au camp
        pique = random() < PROBA_PIQÛRE # Déterminer si le joueur est piqué ou non
        if pique: # Si le joueur est piqué
            self.joueur_actif.pique = True # Marquer le joueur comme piqué
            self.message = "{} a ramassé {} bois, mais il a été piqué par un insecte !".format(self.joueur_actif.nom, nb_bois)
        else: # Sinon
            self.message = "{} a ramassé {} bois.".format(self.joueur_actif.nom, nb_bois)
        self.terminer_tour() # Terminer le tour du joueur actif

    def recuperer_eau(self, instance):
        """Permet au joueur actif de récupérer l'eau du ciel."""
        self.eau += self.meteo # Ajouter l'eau du ciel à l'eau du camp
        self.message = "{} a récupéré {} eau du ciel.".format(self.joueur_actif.nom, self.meteo)
        self.terminer_tour() # Terminer le tour du joueur actif

    def terminer_tour(self):
        """Termine le tour du joueur actif et passe au suivant."""
        if self.bois >= BOIS_CONVERTI: # Si il y a assez de bois au camp
            self.bois -= BOIS_CONVERTI # Retirer le bois converti en planche
            self.planches += 1 # Ajouter une planche au radeau
            if not (self.planches >= PLANCHES_NÉCESSAIRES): # Si le radeau n'est pas encore terminé
                self.message += "\n\nUne planche a été ajoutée au radeau !"
        if self.joueur_actif.pique: # Si le joueur actif est piqué
            gueri = random() < 0.5 # Déterminer si le joueur guérit ou non
            if gueri: # Si le joueur guérit
                self.joueur_actif.pique = False # Marquer le joueur comme guéri
                self.message += "\n\n{} se sent mieux et n'est plus piqué.".format(self.joueur_actif.nom)
            else: # Sinon
                mort = random() < 0.5 # Déterminer si le joueur meurt ou non
                if mort: # Si le joueur meurt
                    self.joueurs.remove(self.joueur_actif) # Retirer le joueur de la liste des joueurs
                    self.message += "\n\n{} succombe à sa piqûre et meurt !".format(self.joueur_actif.nom)
                else: # Sinon
                    self.message += "\n\n{} souffre toujours de sa piqûre.".format(self.joueur_actif.nom)
        self.tour += 1 # Augmenter le numéro du tour
        self.meteo = randint(MIN_EAU, MAX_EAU) # Choisir une nouvelle quantité d'eau dans le ciel
        self.joueur_actif = None # Réinitialiser le joueur actif
        self.actualiser_ecran() # Actualiser l'écran avec les nouvelles informations

    def desactiver_boutons(self):
        """Désactive les boutons d'actions."""
        self.button_peche.disabled = True
        self.button_bois.disabled = True
        self.button_eau.disabled = True
