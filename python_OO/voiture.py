

class voiture:


    def __init__(self,nbr_porte,marque,couleur):
        
        
        self.nbr_portes = nbr_porte
        self.marque = marque
        self.couleur = couleur
        self.vitesse = 0

    def klaxonner(self):
        return "bip bip"    

    def accelerer(self,speed):
        self.vitesse += speed
