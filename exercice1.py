def fizzBuzz(n):
    # TODO imprimer la chaine de caractère appropriée avec la fonction print().
    #  Assigne""r ensuite la valeur à la variable resultat
    resultat = ""
    if n % 3 == 0:
        resultat = "fizz"
    if n % 5 == 0:
        resultat += "buzz"

    print(resultat)
    return resultat

if __name__ == '__main__':
    n = int(input("indiquez le nombre: "))
    print(fizzBuzz(n))
