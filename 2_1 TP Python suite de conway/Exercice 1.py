#1a creer la variable chaine
chaine = "il fait beau aujourd'hui. Je veux en profiter. "

#1b modifier les points de la phrase par !
modifie_chaine = chaine.replace(".","!")
print(modifie_chaine)

#1c  mettre toute la chaine en minuscule
minuscule = chaine.lower()
print(minuscule)

#1d mettre toute la chaine en majuscule
majuscule = chaine.upper()
print(majuscule)

#1e donner l'indice du caractère 'b'
indice = chaine.index("b")
print(f"l'indice de b dans la chaine est: {indice}")