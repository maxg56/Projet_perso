import random
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

kivy.require("2.0.0")

Nourriture = {3: 5, 4: 7, 5: 8, 6: 10, 7: 12, 8: 13, 9: 15, 10: 16, 11: 18, 12: 20}
Eau = {3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18, 10: 20, 11: 22, 12: 24}
Foret = ["v", "v", "v", "v", "f"]


class Carte:
    def __init__(self) -> None:
        pass


class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.inventaire = []
        self.etat = "vivant"

    def get_etat(self):
        return self.etat

    def affiche_inventaire(self):
        return self.inventaire

    def set_etat(self, etat):
        self.etat = etat


class Quand:
    def __init__(self, nombre_de_joueurs):
        self.bois = 0
        self.radeau_count = 0
        self.nourriture = Nourriture[nombre_de_joueurs]
        self.eau = Eau[nombre_de_joueurs]
        self.meteo = [random.randint(0, 3) for _ in range(7 + random.randint(1, 5))]
        self.meteo[len(self.meteo) - 1] = 3

    def affiche_bois(self):
        return self.bois

    def affiche_radeau(self):
        return self.radeau_count

    def affiche_nourriture(self):
        return self.nourriture

    def affiche_meteo(self):
        return self.meteo

    def construire_radeau(self):
        while self.bois >= 6:
            self.radeau_count += 1
            self.bois -= 6

    def peche(self):
        self.nourriture += random.randint(1, 3)

    def chercher_du_bois(self, nombre):
        if 1 <= nombre <= 5:
            random.shuffle(Foret)
            if Foret[nombre - 1] == "f":
                self.bois += 1
                self.construire_radeau()
                return False
            else:
                self.bois += nombre
                self.construire_radeau()
                return True

    def recuperer_eau(self, meteo):
        self.eau += meteo


class GalaraPagosGame:
    def __init__(self, nombre_de_joueurs):
        self.joueurs = [Joueur(nom) for nom in range(1, nombre_de_joueurs + 1)]
        self.quand = Quand(nombre_de_joueurs)
        self.current_player_index = 0  # Initialize with the first player
        self.interface = None

    def next_turn(self):
        if self.current_player_index == len(self.joueurs)-1:
            self.quand.eau -= len(self.joueurs)
            self.quand.nourriture -= len(self.joueurs)
            if self.quand.eau == 0 or self.quand.nourriture == 0:
                pass
        self.current_player_index = (self.current_player_index + 1) % len(self.joueurs)

    def action_button_pressed(self):
        # Call the peche method when the button is pressed
        self.quand.peche()
        self.next_turn()
        # Update the interface with the current player's information
        self.interface.update_interface(self.joueurs[self.current_player_index])

    def bois_button_pressed(self):
        # Call the chercher_du_bois method when the button is pressed
        if self.quand.chercher_du_bois(random.randint(1, 5)) == False:
            self.joueurs[self.current_player_index].set_etat("Blessé")
        self.next_turn()
        # Update the interface with the current player's information
        self.interface.update_interface(self.joueurs[self.current_player_index])


class MainWidget(BoxLayout):
    def __init__(self, game, **kwargs):
        super().__init__(**kwargs)
        self.game = game
        self.orientation = "vertical"
        self.current_player_label = Label(text="Current Player: ")
        self.inventory_label = Label(text="Inventory: ")
        self.water_label = Label(text="Water: ")
        self.food_label = Label(text="Food: ")
        self.raft_label = Label(text="Rafts: ")
        self.wood_label = Label(text="Wood: ")
        self.peche_button = Button(text="Pecher")
        self.peche_button.bind(on_press=self.on_peche_button_pressed)
        self.bois_button = Button(text="Chercher du Bois")
        self.bois_button.bind(on_press=self.on_bois_button_pressed)
        self.add_widget(self.current_player_label)
        self.add_widget(self.inventory_label)
        self.add_widget(self.water_label)
        self.add_widget(self.food_label)
        self.add_widget(self.raft_label)
        self.add_widget(self.wood_label)
        self.add_widget(self.peche_button)
        self.add_widget(self.bois_button)

    def update_interface(self, joueur):
        self.current_player_label.text = f"Current Player: {joueur.nom}"
        self.inventory_label.text = (
            f"Inventory: {', '.join(joueur.affiche_inventaire())}"
        )
        self.water_label.text = f"Water: {self.game.quand.eau}"
        self.food_label.text = f"Food: {self.game.quand.nourriture}"
        self.raft_label.text = f"Rafts: {self.game.quand.radeau_count}"
        self.wood_label.text = f"Wood: {self.game.quand.bois}"

    def on_peche_button_pressed(self, instance):
        self.game.action_button_pressed()

    def on_bois_button_pressed(self, instance):
        self.game.bois_button_pressed()


class GalapagosApp(App):
    def build(self):
        game = GalaraPagosGame(nombre_de_joueurs=4)
        game.interface = MainWidget(game)
        return game.interface


if __name__ == "__main__":
    GalapagosApp().run()
