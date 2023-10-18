import random as rd
class Sorcier : 
    """
    Attributs d'instance :
        nom : chaine de caractere, nom du Sorcier
        pv : entier positif ou nul, points de vie du Sorcier
        degats : entier>0 degats maximum du Sorcier
    Methodes :
        init() : constructeur de la classe Sorcier
        attaque () : renvoie les degats faits à l'adversaire 
        nombre aleatoire compris avec 1 et degats avec randit()
    """
    # Constructeur
    def __init__(self, param_nom, param_pv= 500, param_degats =50):
        self.nom = param_nom
        self.pv = param_pv
        self.degats = param_degats
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
    
class Sort :
    """
    Attributs d'instances :
        nom : chaine de caractère, nom du sort
        cible : chaine de caractère, nom de la cible du sort lancé
        degats : entier >0, degats maximum du sort
    Methodes :
        init(): constructeur de la classe Sort
        attaque_sort(): renvoie les degats du sort 1 faits à l'adversaire
        nombre entier positif 
        attaque_sort2(): renvoie les degats du sort 2 fait à l'adversaire
        nombre entier positif
    """
    #Constructeur
    def __init__(self, paramnom, paramcible, paramdegats=0):
        self.nom = paramnom
        self.degats_sort = paramdegats
        self.__cible = paramcible
    #Methode
    def attaque_sort(self):
        attaque_degats_sort = sortilege1.degats_sort
        self.__cible == sorcier2
        return attaque_degats_sort
    
    def attaque_sort2(self):
        attaque_degats_sort2 = sortilege2.degats_sort
        self.__cible == sorcier1
        return attaque_degats_sort2

sortilege1 = Sort("Avada Kedavra",sorcier2,90)
sortilege2 = Sort("Bombarda",sorcier1,70)
sorcier1 = Sorcier("Harry Potter",500)
sorcier2 = Sorcier("Voldemort",500)
print(sorcier1.nom,"pv:",sorcier1.pv,"degats:",sortilege1.degats_sort)
print(sorcier2.nom,"pv:",sorcier2.pv,"degats:",sortilege2.degats_sort)

while sorcier1.pv>0 and sorcier2.pv>0 :
    sortilege1_degats_sort = sortilege1.attaque_sort()
    sorcier2.pv -= sortilege1_degats_sort
    
    if sorcier2.pv <=0 :
        sorcier2.pv ==0
        print(sorcier2.nom,"est au tapis")   
    else :
        print(sorcier1.nom,"a lancé",sortilege1.nom,"et",sorcier2.nom,"a subis",sortilege1_degats_sort,"points de degats et est a",sorcier2.pv,"ponits de vie")
    
    sortilege2_degats_sort2 = sortilege2.attaque_sort2()
    sorcier1.pv -= sortilege2_degats_sort2
    
    if sorcier1.pv <=0 :
        sorcier1.pv ==0
        print(sorcier1.nom,"est au tapis")
    else : 
        print(sorcier2.nom,"a lancé",sortilege2.nom,"et",sorcier1.nom,"a subis",sortilege2_degats_sort2,"points de degats et est a",sorcier1.pv,"points de vie")
