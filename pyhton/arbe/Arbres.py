import graphviz
from pilesFiles import Pile, File


class Arbre:
    """
    Classe implémentant un arbre dont les noeuds sont caractérisés par
    - une valeur (de type quelconque)
    - des enfants
    Les enfants sont stockés dans une liste (vide apr défaut) et sont eux-mêmes des arbres
    """

    def __init__(self, valeur=None, enfants=None):
        """
        Constructeur
        """
        self.valeur = valeur
        if enfants is not None:
            self.enfants = enfants
        else:
            self.enfants = []

    def renvoie_valeur(self):
        """
        Accesseur de la valeur de l'arbre
        """
        return self.valeur

    def modifie_valeur(self, valeur):
        """
        Mutateur de la valeur de l'arbre
        """
        self.valeur = valeur

    def renvoie_enfants(self):
        """
        Accesseur des enfants
        """
        return self.enfants

    def ajouter_enfant(self, enfant):
        """
        Ajoute l'enfant aux enfants de cet arbre
        """
        assert isinstance(enfant, Arbre), "L'enfant doit être un arbre"

        self.enfants.append(enfant)

    def sous_arbre(self, valeur_enfant):
        """
        Retourne le sous-arbre correspondant à l'enfant (désigné par sa valeur) et passé en argument
        Renvoie None si le noeud n'existe pas
        """
        for enfant in self.enfants:
            if enfant.valeur == valeur_enfant:
                return enfant

        raise Exception("Aucun sous-arbre ne contient cette valeur")

    def est_vide(self):
        """Indique si l'arbre est vide"""
        return self.valeur is None

    def est_feuille(self):
        """
        Renvoie True si l'arbre est une feuille (pas d'enfants)
        False dans le cas contraire
        """
        return self.enfants == []

    def retirer_enfant(self, valeur_enfant):
        """
        Retire l'enfant de la liste des enfants de cet arbre
        Lève une erreur si l'enfant n'est pas dans la liste des enfants
        """
        if not self.sous_arbre(valeur_enfant):
            raise Exception("Aucun sous-arbre ne contient cette valeur")
        else:
            for enfant in self.enfants:
                if enfant.renvoie_valeur() == valeur_enfant:
                    self.enfants.remove(enfant)

    def hauteur(self):
        """
        Renvoie la hauteur de l'arbre
        Renvoie 1 si l'arbre est une feuille
        """
        if self.est_vide():
            return 0
        if self.est_feuille():
            return 1
        return 1 + max([enfant.Hauteur() for enfant in self.enfants])

    def taille(self):
        """
        Renvoie la taille de l'arbre (le nombre de noeud)
        """
        if self.est_vide():
            return 0
        return 1 + sum([enfant.taille() for enfant in self.enfants])

    def parcours_largeur(self) -> None:
        """
        Renvoie la liste des valeurs des noeuds
        rencontrés lors d'un parcours en largeur
        """
        if self.est_vide():
            return []
        file = File()
        file.enfiler(self)
        resultat = []

        while not file.est_vide():
            ardre = file.defiler()
            resultat.append(ardre.valeur)
            for enfants in ardre.enfants():
                file.enfiler(enfants)
        return resultat

    def parcours_profondeur_prefixe(self):
        """
        Renvoie la liste des valeurs des noeuds
        rencontrés lors d'un parcours en profondeur prefixe
        """
        if self.est_vide():
            return []
        if self.est_feuille():
            return [self.valeur]
        resultat = []
        resultat.append(self.valeur)
        for enfant in self.enfants:
            resultat += enfant.parcours_profondeur_prefixe()
        return resultat

    def parcours_profondeur_postfixe(self):
        """
        Renvoie la liste des valeurs des noeuds
        rencontrés lors d'un parcours en profondeur postfixe
        """
        if self.est_vide():
            return []
        if self.est_feuille():
            return [self.valeur]
        resultat = []
        for enfant in self.enfants:
            resultat += enfant.parcours_profondeur_postfixe()
        resultat.append(self.valeur)

        return resultat

    def dessiner(self, nom="graphe"):
        """
        Représente l'arbre
        """
        cle = 0
        pile = Pile()

        graphe = graphviz.Graph(format="png")
        graphe.node(str(cle), str(self.renvoie_valeur()))
        pile.empiler((self, cle))

        while not pile.est_vide():
            arbre, cle_arbre = pile.depiler()
            for enfant in arbre.enfants:
                cle += 1
                graphe.node(str(cle), str(enfant.valeur))
                pile.empiler((enfant, cle))
                graphe.edge(str(cle_arbre), str(cle))

        graphe.render(nom, view=True)

    def __str__(self):
        """
        Représentation de l'arbre dans la console
        """
        h_barre = "_____"

        s = ""

        if self.est_vide():
            s = "∅"
        else:
            profondeur = 0
            p = Pile()
            p.empiler((self, profondeur))
            while not p.est_vide():
                arbre, profondeur = p.depiler()
                if profondeur > 0:
                    s += (
                        "  |"
                        + (" " * 8 + "|") * (profondeur - 1)
                        + h_barre
                        + str(arbre.renvoie_valeur())
                        + "\n"
                    )
                elif profondeur == 0:
                    s += str(arbre.renvoie_valeur()) + "\n"

                for enfant in arbre.renvoie_enfants():
                    p.empiler((enfant, profondeur + 1))

        return s


if __name__ == "__main__":
    s_8 = Arbre("Noeud 8")
    s_7 = Arbre("Noeud 7")
    s_6 = Arbre("Noeud 6")
    s_5 = Arbre("Noeud 5")
    s_4 = Arbre("Noeud 4", [s_5, s_6])
    s_3 = Arbre("Noeud 3", [s_4])
    s_2 = Arbre("Noeud 2", [s_7])
    arbre = Arbre("Noeud 1")
    arbre.ajouter_enfant(s_3)
    arbre.ajouter_enfant(s_2)
    arbre.ajouter_enfant(s_8)
    arbre.dessiner()

    print(f"Hauteur de l'arbre : {arbre.hauteur()}")
    print(f"Taille de l'arbre : {arbre.taille()}")
    print(f"Parcours en largeur de l'arbre : {arbre.parcours_largeur()}")
    print(
        f"Parcours en profondeur prefixe de l'arbre : {arbre.parcours_profondeur_prefixe()}"
    )
    print(
        f"Parcours en profondeur postfixe de l'arbre : {arbre.parcours_profondeur_postfixe()}"
    )

    print(arbre)
