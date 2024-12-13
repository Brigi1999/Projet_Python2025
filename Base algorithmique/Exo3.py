#afficher si le nombre est pair ou impair
nombre = int(input("saisir un nombre: "))
modulo= nombre%2
if modulo== 0 :print("le nombre que vous avez saisi est pair")
else :
    print("le nombre est impair")