# ecrire une fonction qui renvoie le premier mot d'une chaine
def afficher_premier_mot(phrase):
    premier_mots = phrase.split()
    if phrase:
        return premier_mots[0]
    return "Aucun mot trouvé"
phrase = "samedi soir je sors"
print(afficher_premier_mot(phrase)) 