# Afficher les tables de multiplication de 1 à 10
for i in range(1, 11):  
    print(f"table de {i} : ")
    for j in range(1, 11):  
        print(f"{i} x {j} = {i * j}")  
    print("-" * 20)  