# analyse de logs d'accès Web
import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "C:/Users/Houéfa/Documents/Code python/mini projet/web_access_logs.csv"
logs = pd.read_csv(file_path)


# Identifier les requêtes vers /login
login_attempts = logs[logs['url'].str.contains('/login', na=False)]
# Compter les tentatives par IP
login_attempts_by_ip = login_attempts.groupby('ip_address').size().reset_index(name='attempts')

# Identifier les IP suspectes 
suspect_ips = login_attempts_by_ip[login_attempts_by_ip['attempts'] > 10]

# Visualiser les IP les plus fréquentes
ip_counts = logs['ip_address'].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=ip_counts.values, y=ip_counts.index, palette="viridis")
plt.title("Top 10 des IP les plus fréquentes")
plt.xlabel("Nombre de requêtes")
plt.ylabel("Adresse IP")
plt.show()

#  Générer un rapport
suspect_ips.to_csv("suspect_ips_report.csv", index=False)
print("Rapport généré : suspect_ips_report.csv")