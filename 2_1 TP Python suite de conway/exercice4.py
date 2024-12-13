# programme qui retourne une phrase
def inverser_phrase(phrase) :
    #ceci permet de séparer les mots
    mots = phrase.split() 
    # inverser l'ordre des mots dans la phrase
    inverser = mots[::-1] 
    # reconstituer la phrase
    return " ". join(inverser) 
chaine = "je suis la"
print(inverser_phrase(chaine))