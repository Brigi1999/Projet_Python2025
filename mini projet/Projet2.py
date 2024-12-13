# scanner de port simple
import socket
import matplotlib.pyplot as plt

def scan_ports(ip, ports):
    open_ports = []
    
    # Teste chaque port
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Temps d'attente avant timeout
        sock.settimeout(2)  
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)  
        sock.close()
    
    return open_ports

def visualize_ports(open_ports):
    # Création du graphique des ports ouverts
    plt.bar(open_ports, [1] * len(open_ports), color='#87CEEB')
    plt.xlabel('Port')
    plt.ylabel('État')
    plt.title('Ports ouverts')
    plt.show()

if __name__ == "__main__":
    ip_cible = input("Entrez l'adresse IP cible: ")
    ports = [22, 80, 443, 8080, 3306, 53, 21, 25, 110]  
    

    print(f"Scanning des ports sur {ip_cible}...")
    open_ports = scan_ports(ip_cible, ports)
    
    if open_ports:
        print(f"Ports ouverts: {open_ports}")
        visualize_ports(open_ports)
    else:
        print("Aucun port ouvert trouvé.")
