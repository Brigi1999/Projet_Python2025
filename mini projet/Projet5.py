import itertools
import time
import matplotlib.pyplot as plt

# Simuler un service avec un mot de passe défini
CORRECT_PASSWORD = "1234"

# Liste des mots de passe courants
password_list = ["123", "password", "1234", "qwerty", "admin", "letmein"]

# Variables pour enregistrer les résultats
successful_attempts = []
failed_attempts = []

# Fonction de brute force
def brute_force_attack(password_list, correct_password):
    for password in password_list:
        time.sleep(0.1)  # Simule un délai entre les tentatives
        if password == correct_password:
            successful_attempts.append(password)
            print(f"Succès : Mot de passe trouvé - {password}")
            break
        else:
            failed_attempts.append(password)
            print(f"Échec : {password} n'est pas correct.")

# Lancer l'attaque
print("Lancement de l'attaque par force brute...")
brute_force_attack(password_list, CORRECT_PASSWORD)

# Visualisation des résultats
labels = ['Échecs', 'Réussites']
values = [len(failed_attempts), len(successful_attempts)]

plt.bar(labels, values, color=['red', 'green'])
plt.title('Tentatives de brute-force')
plt.ylabel('Nombre de tentatives')
plt.show()