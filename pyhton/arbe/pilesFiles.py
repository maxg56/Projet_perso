class Element:
    def __init__(self, valeur, successeur=None):
        """
        Constructeur
        valeur est de type quelconque
        successeur est un élément ou None par défaut
        """
        self.valeur = valeur
        self.successeur = successeur

    def get_valeur(self):
        """
        Accesseur de la valeur
        """
        return self.valeur

    def get_successeur(self):
        """
        Accesseur du successeur
        """
        return self.successeur

    def set_valeur(self, nouvelle_valeur):
        """
        Mutateur de la valeur
        """
        self.valeur = nouvelle_valeur

    def set_successeur(self, nouveau_successeur):
        """
        Mutateur du successeur
        """
        self.successeur = nouveau_successeur

    def __repr__(self):
        """
        Représentation en str
        """
        return str(self.valeur) + " -> Pointe vers : " + str(id(self.successeur))



class Pile:
    """
    Classe implémentant une pile à l'aide d'une liste chaînée
    """

    def __init__(self):
        """
        Constructeur
        Retourne une pile vide
        """
        self.tete = None

    def est_vide(self):
        """
        Teste si la pile est vide
        Renvoie True ou False selon la réponse
        """
        return self.tete == None

    def empiler(self, valeur):
        """
        Empile une nouvelle donnée à l'aide d'un élément sur la pile
        """
        element = Element(valeur)
        element.successeur = self.tete
        self.tete = element

    def depiler(self):
        """
        Dépile et retourne la première valeur de la pile
        Si la pile est vide, renvoie une erreur 
        """
        if self.est_vide():
            raise Exception('La pile est vide !')
        else:
            top = self.tete
            self.tete = self.tete.successeur

            return top.valeur

    def afficher(self):
        """
        Affichage de la pile
        """
        if self.est_vide():
            print("La pile est vide")
        else:

            pointeur = self.tete

            while pointeur != None:
                print(pointeur.valeur)
                pointeur = pointeur.successeur

class File:
    """
    Classe implémentant une file à l'aide d'une liste chaînée
    """

    def __init__(self):
        """
        Constructeur
        Retourne une file vide
        """
        self.tete = None
        self.queue = None

    def est_vide(self):
        """
        Teste si la file est vide
        Renvoie True ou False selon la réponse
        """
        return self.tete == None

    def enfiler(self, valeur):
        """
        Enfile une nouvelle donnée à l'aide d'un élément sur la file
        """
        element = Element(valeur)
        if self.est_vide() :
            self.tete = element
            self.queue = element
        else :
            self.queue.successeur = element
            self.queue = element

    def defiler(self):
        """
        Défile et retourne la première valeur de la file
        Si la file est vide, renvoie une erreur 
        """
        if self.est_vide():
            raise Exception('La file est vide !')
        else:
            top = self.tete
            self.tete = self.tete.successeur

            return top.valeur

    def afficher(self):
        """
        Affichage de la file
        """
        if self.est_vide():
            print("La file est vide")
        else:
            s = ""

            pointeur = self.tete
            s += str(pointeur.valeur)

            while pointeur.successeur != None:
                pointeur = pointeur.successeur
                s += " <-- " + str(pointeur.valeur)

            print(s, end="\n\n")


if __name__ == "__main__":
    """
    # On crée une pile vide
    pile = Pile()
    pile.afficher()

    # On ajoute l'élément 1
    pile.empiler(1)
    pile.afficher()

    # On ajoute l'élément 2
    pile.empiler(2)
    pile.afficher()

    # On dépile le 2
    elt = pile.depiler()
    pile.afficher()

    # On dépile le 1
    elt = pile.depiler()
    pile.afficher()

     # On dépile un dernier élément (erreur car la pile est déjà vide)
    elt = pile.depiler()
    """

    # On crée une file vide
    f = File()
    f.afficher()

    # On ajoute l'élément 1
    f.enfiler(1)
    f.afficher()

    # On ajoute l'élément 2
    f.enfiler(2)
    f.enfiler(3)
    f.enfiler(4)
    f.enfiler(5)
    f.afficher()

    # On dépile le 1
    elt = f.defiler()
    print(elt)
    f.afficher()

    # On dépile le 2
    elt = f.defiler()
    print(elt)
    f.afficher()

     # On dépile un dernier élément (erreur car la file est déjà vide)
    elt = f.defiler()
    