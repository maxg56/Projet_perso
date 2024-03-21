# Importer les modules nécessaires
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from random import randint

# Définir les variables globales
joueurs = 0 # Le nombre de joueurs
noms = [] # La liste des noms des joueurs
eau = 100 # Le niveau d'eau du camp
nourriture = 100 # Le niveau de nourriture du camp
bois = 100 # Le niveau de bois du camp
plats = 0 # Le nombre de plats sur le radeau
meteo = "Ensoleillé" # La météo du jour

# Définir les écrans de l'application
class EcranAccueil(Screen):
    # L'écran d'accueil qui demande le nombre de joueurs et lance la partie
    def __init__(self, **kwargs):
        super(EcranAccueil, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation="vertical")
        self.label = Label(text="Bienvenue dans le jeu du radeau !\nCombien de joueurs êtes-vous ?")
        self.input = TextInput(multiline=False)
        self.button = Button(text="Lancer la partie")
        self.button.bind(on_press=self.lancer_partie)
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.input)
        self.layout.add_widget(self.button)
        self.add_widget(self.layout)

    def lancer_partie(self, instance):
        # Lancer la partie en vérifiant que le nombre de joueurs est valide
        global joueurs, noms
        try:
            joueurs = int(self.input.text)
            if joueurs > 0:
                noms = [f"Joueur {i+1}" for i in range(joueurs)]
                self.manager.current = "ecran_jeu"
            else:
                self.label.text = "Veuillez entrer un nombre de joueurs positif."
        except ValueError:
            self.label.text = "Veuillez entrer un nombre de joueurs valide."


class EcranJeu(Screen):
    # L'écran de jeu qui affiche les informations du camp et les actions possibles
    def __init__(self, **kwargs):
        super(EcranJeu, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation="vertical")
        self.layout_haut = BoxLayout(orientation="horizontal", size_hint=(1, 0.2))
        self.layout_bas = BoxLayout(orientation="horizontal", size_hint=(1, 0.2))
        self.layout_milieu = BoxLayout(orientation="vertical", size_hint=(1, 0.6))
        self.label_nom = Label(text=f"Nom: {Window.title}")
        self.label_eau = Label(text=f"Eau: {eau}")
        self.label_nourriture = Label(text=f"Nourriture: {nourriture}")
        self.label_bois = Label(text=f"Bois: {bois}")
        self.label_plats = Label(text=f"Plats: {plats}")
        self.label_meteo = Label(text=f"Météo: {meteo}")
        self.button_pecher = Button(text="Pêcher")
        self.button_pecher.bind(on_press=self.pecher)
        self.button_bois = Button(text="Chercher du bois")
        self.button_bois.bind(on_press=self.chercher_bois)
        self.button_eau = Button(text="Récupérer l'eau")
        self.button_eau.bind(on_press=self.recuperer_eau)
        self.label_message = Label(text="")
        self.layout_haut.add_widget(self.label_nom)
        self.layout_haut.add_widget(self.label_eau)
        self.layout_haut.add_widget(self.label_nourriture)
        self.layout_haut.add_widget(self.label_bois)
        self.layout_haut.add_widget(self.label_plats)
        self.layout_haut.add_widget(self.label_meteo)
        self.layout_bas.add_widget(self.button_pecher)
        self.layout_bas.add_widget(self.button_bois)
        self.layout_bas.add_widget(self.button_eau)
        self.layout_milieu.add_widget(self.label_message)
        self.layout.add_widget(self.layout_haut)
        self.layout.add_widget(self.layout_milieu)
        self.layout.add_widget(self.layout_bas)
        self.add_widget(self.layout)

    def pecher(self, instance):
        # Pêcher un poisson et ajouter un plat sur le radeau
        global plats, nourriture, eau
        plats += 1
        self.label_plats.text = f"Plats: {plats}"
        self.label_message.text = "Vous avez pêché un poisson et ajouté un plat sur le radeau."
        self.actualiser()

    def chercher_bois(self, instance):
        # Chercher du bois et ajouter du bois au camp
        global bois, nourriture, eau
        bois += randint(10, 20)
        self.label_bois.text = f"Bois: {bois}"
        self.label_message.text = "Vous avez trouvé du bois et ajouté du bois au camp."
        self.actualiser()

    def recuperer_eau(self, instance):
        # Récupérer de l'eau et ajouter de l'eau au camp
        global eau, nourriture, bois
        eau += randint(10, 20)
        self.label_eau.text = f"Eau: {eau}"
        self.label_message.text = "Vous avez récupéré de l'eau et ajouté de l'eau au camp."
        self.actualiser()

    def actualiser(self):
        # Actualiser les niveaux d'eau et de nourriture du camp et la météo du jour
        global eau, nourriture, meteo
        eau -= randint(1, 5) * joueurs
        nourriture -= randint(1, 5) * joueurs
        self.label_eau.text = f"Eau: {eau}"
        self.label_nourriture.text = f"Nourriture: {nourriture}"
        meteo = ["Ensoleillé", "Nuageux", "Pluvieux", "Orageux"][randint(0, 3)]
        self.label_meteo.text = f"Météo: {meteo}"
        if eau <= 0 or nourriture <= 0:
            self.manager.current = "ecran_vote"

class EcranVote(Screen):
    # L'écran de vote qui demande aux joueurs de choisir qui éliminer du radeau
    def __init__(self, **kwargs):
        super(EcranVote, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation="vertical")
        self.label = Label(text="L'eau ou la nourriture a atteint 0. Il faut éliminer quelqu'un du radeau.\nQui voulez-vous éliminer ?")
        # Créer un bouton pour chaque nom de joueur
        self.buttons = []
        for nom in noms:
            button = Button(text=nom)
            button.bind(on_press=self.voter)
            self.buttons.append(button)
            self.layout.add_widget(button)
        self.add_widget(self.layout)

    def voter(self, instance):
        # Voter pour éliminer quelqu'un du radeau et afficher le résultat
        global joueurs, noms
        vote = instance.text
        if vote == Window.title:
            self.label.text = "Vous ne pouvez pas voter pour vous-même."
            return
        else:
            joueurs -= 1
            noms.remove(vote)
            if joueurs == 0:
                self.manager.current = "ecran_fin"
            else:
                self.manager.current = "ecran_jeu"
                self.label.text = f"{vote} a été éliminé du radeau.\nIl reste {joueurs} joueurs."


class EcranFin(Screen):
    # L'écran de fin qui affiche le message de fin du jeu
    def __init__(self, **kwargs):
        super(EcranFin, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation="vertical")
        self.label = Label(text="Vous êtes le dernier survivant du radeau.\nBravo ! Vous avez gagné le jeu !")
        self.layout.add_widget(self.label)
        self.add_widget(self.layout)


# Créer le gestionnaire d'écrans
sm = ScreenManager()
sm.add_widget(EcranAccueil(name="ecran_accueil"))
sm.add_widget(EcranJeu(name="ecran_jeu"))
sm.add_widget(EcranVote(name="ecran_vote"))
sm.add_widget(EcranFin(name="ecran_fin"))

# Créer l'application principale
class RadeauApp(App):
    def build(self):
        return sm

# Lancer l'application
if __name__ == "__main__":
    RadeauApp().run()
