#palindrome
mot = input("veuillez saisir un mot ")
inverse=mot[::-1]
if mot== inverse :
    print("ce mot que vous avez saisi est un palindrome")
else :
    print("ce mot n'est pas un palindrome")
