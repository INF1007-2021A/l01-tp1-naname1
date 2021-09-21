
def decomposer(secondes):
    secondes_dans_annes = 60*60*24*365
    # TODO: Assigner à la variable "annees" le nombre d'années
    annees = secondes // secondes_dans_annes

    restant_seconde_dans_annes = secondes % secondes_dans_annes
    # TODO: Assigner à la variable "semaines" le nombre de semaines restantes
    secondes_dans_semaine = 60*60*24*7
    semaines = restant_seconde_dans_annes // secondes_dans_semaine

    restant_seconde_dans_semaine = restant_seconde_dans_annes % secondes_dans_semaine
    # TODO: Assigner à la variable "jours" le nombre de jours restants
    secondes_dans_jours = 60*60*24
    jours = restant_seconde_dans_semaine // secondes_dans_jours

    restant_seconde_dans_jours = restant_seconde_dans_semaine % secondes_dans_jours
    # TODO: Assigner à la variable "heures" le nombre d'heures restantes
    secondes_dans_heures = 60*60
    heures = restant_seconde_dans_jours // secondes_dans_heures

    restant_seconde_dans_heures = restant_seconde_dans_jours % secondes_dans_heures
    # TODO: Assigner à la variable "minute" le nombre de minutes restantes
    secondes_dans_minutes = 60
    minutes = restant_seconde_dans_heures // secondes_dans_minutes

    # TODO: Assigner à la variable "secondes" le nombre de secondes restantes
    secondes = restant_seconde_dans_heures %secondes_dans_minutes

    # TODO: Afficher le nombres d'années, semaines, jours, heures, minutes et secondes
    print(annees ,semaines ,jours ,heures ,minutes ,secondes)

    return (annees ,semaines ,jours ,heures ,minutes ,secondes)

if __name__ == '__main__':
    secondes = int(input("Entrer les secondes: "))
    print(decomposer(secondes))
