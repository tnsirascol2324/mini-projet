import random as rd

class Sorcier : 
    """
    Attributs d'instance :
        nom : chaine de caractere, nom du Sorcier
        pv : entier positif ou nul, points de vie du Soricer
        degats : entier>0 degats maximum du Sorcier
    Methodes :
        init() : constructeur de la classe Sorcier
        attaque () : renvoie les degats faits à l'adversaire 
        nombre aleatoire compris avec 1 et degats avec randit()

    """
    # Constructeur
    def __init__(self, paramnom, parampv= 500, paramdegats =70):
        #Attributs d'instances
        self.nom = paramnom
        self.pv = parampv
        self.degats = paramdegats
    #Methode
    def attaque(self):
        attaque_degats = rd.randint(10, self.degats)
        return attaque_degats
    
sorcier1 = Sorcier("Harry Potter")
sorcier2 = Sorcier("Voldemort")
print(sorcier1.nom, "pv:", sorcier1.pv, "degats:", sorcier1.degats)
print(sorcier2.nom, "pv:", sorcier2.pv, "degats:", sorcier2.degats)

while sorcier1.pv>=0 and sorcier2.pv>=0 :
    sorcier1_degats = sorcier1.attaque()
    sorcier2.pv -= sorcier1_degats 

    if sorcier2.pv <=0 :
        sorcier2.pv == 0
        print(sorcier2.nom, "est au tapis")
    else :
        print(sorcier2.nom,"a subis",sorcier1_degats,"points de degats et est à",sorcier2.pv,"points de vie")

    sorcier2_degats = sorcier2.attaque()
    sorcier1.pv -= sorcier2_degats

    if sorcier1.pv <=0 :
        sorcier1.pv ==0
        print(sorcier1.nom,"est au tapis")
    else :
        print(sorcier1.nom,"a subis",sorcier2_degats,"points de degats et est à",sorcier1.pv,"points de vie")

