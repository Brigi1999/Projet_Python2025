#factorielle
nbre= int(input("veuillez saisir un nombre nnn "))
def factorielle(nbre) :
  if nbre< 0 :
     return "veuillez saisir un nombre positif"
  if nbre== 0 or nbre== 1 :
     return 1
  return nbre* factorielle(nbre-1)

