import math


def calculerPosition(positionInitiale, vitesseInitiale, duree, vitesseFinale):
    if duree <= 0:
        print("La durée doit être strictement positive.")
        return None

    #Conversion en m/s
    vitesseFinale *= 3600/1000
    vitesseInitiale *= 3600/1000
    # TODO faites les calculs intermediaires, vous pouvez initialiser des variables locales.
    acceleration = (vitesseFinale-vitesseInitiale)/duree

    # TODO calculer la position finale, assigner la valeur à la variable "positionFinale"
    positionFinale = vitesseInitiale*duree+1/2*acceleration*(duree)**2+positionInitiale

    return positionFinale

if __name__ == '__main__':
    positionInitiale = int(input("Entrez la position initiale en mètre: "))
    vitesseInitiale = int(input("Entrez la vitesse initiale en km/h: "))
    duree = int(input("Entrez la duree en secondes: "))
    vitesseFinale = int(input("Entrez la vitesseFinale en km/h: "))
    print(calculerPosition(positionInitiale, vitesseInitiale, duree, vitesseFinale))
