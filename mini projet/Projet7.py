import ssl
import socket
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Étape 1 : Extraire les informations SSL d'un site
def get_ssl_expiration(hostname, port=443):
    """
    Récupère les informations SSL d'un site web et renvoie la date d'expiration.
    """
    context = ssl.create_default_context()
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            ssl_info = ssock.getpeercert()
    # Extraire la date d'expiration
    expiry_date = datetime.strptime(ssl_info['notAfter'], "%b %d %H:%M:%S %Y %Z")
    return expiry_date

# Étape 2 : Vérifier l'état des certificats
def check_ssl_sites(sites):
    """
    Vérifie la validité des certificats SSL pour une liste de sites.
    """
    results = {"Site": [], "Valid": [], "Days Left": []}
    today = datetime.utcnow()
    
    for site in sites:
        try:
            expiry_date = get_ssl_expiration(site)
            days_left = (expiry_date - today).days
            results["Site"].append(site)
            results["Valid"].append(days_left > 0)
            results["Days Left"].append(days_left)
            print(f"{site} : Expiration dans {days_left} jours (Expire le {expiry_date})")
        except Exception as e:
            results["Site"].append(site)
            results["Valid"].append(False)
            results["Days Left"].append(-1)
            print(f"{site} : Erreur lors de la vérification ({e})")
    
    return results

# Étape 3 : Visualiser les résultats
def visualize_ssl_results(results):
    """
    Affiche un graphique des certificats valides et expirés.
    """
    valid_count = sum(results["Valid"])
    expired_count = len(results["Valid"]) - valid_count
    
    # Diagramme circulaire
    labels = ['Valides', 'Expirés']
    sizes = [valid_count, expired_count]
    colors = ['#66b3ff', '#ff6666']
    
    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.title("État des certificats SSL")
    plt.show()

# Étape 4 : Exemple d'utilisation
if __name__ == "__main__" :
    # Liste de sites à vérifier
    sites_to_check = [
        "google.com", 
        "expired.badssl.com", 
        "github.com", 
        "facebook.com", 
        "example.com"
    ]
    
    # Vérifier les certificats SSL
    ssl_results = check_ssl_sites(sites_to_check)
    
    # Visualiser les résultats
    visualize_ssl_results(ssl_results)