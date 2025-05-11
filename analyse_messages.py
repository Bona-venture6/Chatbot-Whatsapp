import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# Charger les données
df = pd.read_csv("messages_log.csv", names=["Date", "Numero", "Message", "Reponse"])

# Convertir les dates
df["Date"] = pd.to_datetime(df["Date"])
df["Jour"] = df["Date"].dt.date

# Afficher le nombre total de messages
print(f"Nombre total de messages reçus : {len(df)}")

# Analyse des mots les plus fréquents
mots = " ".join(df["Message"].dropna()).lower().split()
compteur = Counter(mots)
print("\nMots les plus fréquents :")
for mot, freq in compteur.most_common(10):
    print(f"{mot} : {freq}")

# Messages par jour
freq_jour = df.groupby("Jour").size()

# Afficher un graphique
plt.figure(figsize=(10, 5))
freq_jour.plot(kind='bar', color='skyblue')
plt.title("Nombre de messages par jour")
plt.xlabel("Date")
plt.ylabel("Nombre de messages")
plt.tight_layout()
plt.savefig("stats_messages.png")
plt.show()
