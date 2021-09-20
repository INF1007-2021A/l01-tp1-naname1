def pointDeRencontre(v1, v2, distance):
    if v1+v2==0:
        print("La somme des vitesses ne peut pas être 0.")
        return None

    # TODO faites les calculs intermediaires, vous pouvez initialiser des variables locales.
    # On veut que v1*t=-v2*t+distance (la voiture 2 se déplace dans le sens opposée). C'est le temps de collision
    temps_rencontre = distance/(v1+v2)

    # TODO calculer la position de rencontre, assignez la valeur à la variable "positionRencontre"
    positionRencontre = v1*temps_rencontre

    return positionRencontre

if __name__ == '__main__':
    v1 = int(input("Entrez v1: "))
    v2 = int(input("Entrez v2: "))
    distance = int(input("Entrez la distance: "))
    print(pointDeRencontre(v1, v2, distance))
