import os
import shutil
import logging

# Configuration des logs
logging.basicConfig(filename='classification.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def classifier_dossiers(repertoire_source):
    try:
        # Vérification de l'existence du répertoire
        if not os.path.exists(repertoire_source):
            logging.error(f"Le répertoire {repertoire_source} n'existe pas.")
            return
        
        # Parcours des fichiers dans le répertoire
        for fichier in os.listdir(repertoire_source):
            chemin_complet = os.path.join(repertoire_source, fichier)
            
            # Vérifier si c'est un fichier
            if os.path.isfile(chemin_complet):
                # Récupérer l'extension
                extension = os.path.splitext(fichier)[1][1:]  # Ex: 'txt'
                
                if not extension:  # Fichiers sans extension
                    extension = "SansExtension"
                
                # Créer un sous-dossier pour cette extension s'il n'existe pas
                dossier_extension = os.path.join(repertoire_source, extension)
                if not os.path.exists(dossier_extension):
                    os.makedirs(dossier_extension)
                    logging.info(f"Sous-dossier créé : {dossier_extension}")
                
                # Déplacer le fichier
                shutil.move(chemin_complet, os.path.join(dossier_extension, fichier))
                logging.info(f"Fichier déplacé : {fichier} -> {dossier_extension}")
    except Exception as e:
        logging.error(f"Erreur rencontrée : {str(e)}")

# Exemple d'utilisation
repertoire = input("Entrez le chemin du répertoire source : ")
classifier_dossiers(repertoire)