class Element:
    """_summary_"""

    def __init__(self, valeur):
        self.valeur = valeur
        self.successeur = None

    def renvoie_valeur(self):
        return self.valeur

    def renvoie_successeur(self):
        return self.successeur

    def modifie_valeur(self, valeur):
        self.valeur = valeur

    def modifie_successeur(self, successeur):
        self.successeur = successeur

    def __str__(self):
        return f" {self.valeur} -> {self.successeur } "


class Piles:
    def __init__(self):
        self.tette = None

    def est_vide(self):
        return self.tette is None

    def empiler(self, x):
        nouvel_element = Element(x)
        if not self.est_vide():
            nouvel_element.successeur = self.tette

        self.tette = nouvel_element

    def depiler(self):
        if self.est_vide():
            raise ValueError("LA pile set vide")

        v = self.tette.valeur
        self.tette = self.tette.successeur

        return v
    
    def __str__(self) -> str:
        if self.est_vide():
            return "la pile est vide"
        else :
            return f"Hout || {self.tette} || Bas".format()


if __name__ == "__main__":
    # Tests
    pile = Piles()
    assert pile.est_vide()
    pile.empiler(1)
    pile.empiler(2)
    print(pile)
    assert not pile.est_vide()
    assert pile.depiler() == 2
    assert pile.depiler() == 1
    assert pile.est_vide()
    print(pile)
