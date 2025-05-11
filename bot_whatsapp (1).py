from flask import Flask, request  # Importe Flask et request pour gérer l'application web et les requêtes HTTP
from twilio.twiml.messaging_response import MessagingResponse  # Pour construire une réponse WhatsApp compatible avec Twilio
from datetime import datetime  # Pour enregistrer la date et l'heure de chaque message
import os  # Pour récupérer le port depuis les variables d’environnement (Render)

app = Flask(__name__)  # Initialise l'application Flask

# Réponses associées aux options du menu
menu_reponses = {
    "1": "Parfait ! Veuillez envoyer le nom du produit et la quantité souhaitée.",
    "2": "Nos prix varient selon les produits. Veuillez préciser ce que vous recherchez.",
    "3": "Nous sommes là pour vous aider. Posez votre question librement !"
}

# Mots-clés libres associés à des réponses automatiques
reponses = {
    "bonjour": "Bonjour et bienvenue ! Voici nos options :\n1. Passer une commande\n2. Voir les prix\n3. Poser une question",
    "commande": "Pour commander, veuillez taper '1' ou envoyez directement le produit et la quantité.",
    "prix": "Tapez '2' pour consulter les prix selon le produit.",
    "merci": "Avec plaisir ! Nous restons disponibles."
}

@app.route("/webhook", methods=['POST'])  # Route Flask qui sera appelée quand un message arrive
def bot():
    message = request.form.get('Body', '').lower().strip()  # Récupère le message reçu
    numero = request.form.get('From', 'inconnu')  # Récupère le numéro de l’expéditeur
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Date et heure actuelles

    # Réponse par défaut (menu)
    reponse_text = "Bienvenue ! Choisissez une option :\n1. Passer une commande\n2. Voir les prix\n3. Poser une question"

    if message in menu_reponses:
        reponse_text = menu_reponses[message]
    else:
        for mot_cle in reponses:
            if mot_cle in message:
                reponse_text = reponses[mot_cle]
                break

    # Enregistrement dans un fichier CSV local
    with open("messages_log.csv", "a", encoding="utf-8") as f:
        f.write(f"{now},{numero},{message},{reponse_text}\n")

    # Construction de la réponse WhatsApp via Twilio
    reponse = MessagingResponse()
    reponse.message(reponse_text)
    return str(reponse)

# Lancement de l'application Flask sur le bon port
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
