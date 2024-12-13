# script qui affiche les 20 premiers termes de la suite
def image(mot):
    # Initialisation du résultat
    resultat = ""  
    i = 0  
    # Parcourir chaque caractère de la chaîne
    while i < len(mot): 
        # Compte le nombre d'occurrences consécutives
        count = 1  
        # Tant que les chiffres consécutifs sont identiques
        while i + 1 < len(mot) and mot[i] == mot[i + 1]:  
            # Augmenter le compteur
            count += 1 
            # Passe au chiffre suivant 
            i += 1 
        # Ajouter le nombre de répétitions suivi du chiffre lui-même au résultat
        resultat += str(count) + mot[i]
        # Passer au chiffre suivant dans la chaîne
        i += 1  
    return resultat 
suite= 20
print(image(suite))