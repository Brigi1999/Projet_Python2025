#compter les voyelles
phras= input("veuillez saisir une phrase ")
voyelles= "aeiouyAEIOUY"
compte= 0
for i in phras :
    if i in voyelles :
     compte +=1
print("le nombre de voyelle dans la phrase est :", compte)



