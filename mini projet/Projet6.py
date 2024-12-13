# analyse des logs de sécurité windows
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Importer les logs de sécurité Windows
def load_logs(file_path):
    try:
        logs = pd.read_csv(file_path)
        print("Logs chargés avec succès.")
        return logs
    except Exception as e:
        print(f"Erreur lors du chargement des logs : {e}")
        return None

# Identifier les connexions échouées
def filter_failed_logins(logs, event_id=4625):
    """
    Filtrer les événements de connexion échouée (ID 4625 dans les logs Windows).
    """
    failed_logins = logs[logs['EventID'] == event_id]
    return failed_logins

#  Visualiser les types d'événements
def plot_event_frequency(logs):
    event_counts = logs['EventID'].value_counts()
    plt.figure(figsize=(10, 6))
    sns.barplot(x=event_counts.index, y=event_counts.values, palette="viridis")
    plt.title("Fréquence des événements par type (EventID)")
    plt.xlabel("EventID")
    plt.ylabel("Nombre d'événements")
    plt.show()

#  Générer un rapport des activités suspectes
def generate_report(failed_logins, output_file="rapport_suspect.txt"):
    """
    Générer un rapport texte des connexions échouées.
    """
    with open(output_file, "w") as file:
        file.write("-- Rapport des connexions échouées --\n")
        file.write(f"Nombre total de connexions échouées : {len(failed_logins)}\n\n")
        file.write("Détails des connexions échouées :\n")
        file.write(failed_logins.to_string(index=False))
    print(f"Rapport généré : {output_file}")

# Exemple d'utilisation
if __name__ == "__main__" :
    # Chemin vers le fichier CSV
    file_path = "C:/Users/Houéfa/Documents/Code python/mini projet/logs_securite_windows.csv" 
    logs = load_logs(file_path)
    
    if logs is not None:
        # Filtrer les connexions échouées
        failed_logins = filter_failed_logins(logs)
        print(f"Nombre de connexions échouées : {len(failed_logins)}")

        # Visualiser la fréquence des événements
        plot_event_frequency(logs)

        # Générer un rapport des activités suspectes
        generate_report(failed_logins)