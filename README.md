# Chatbot-Whatsapp
# Bot WhatsApp pour Commerce (Projet d'étude évolutif)

Ce projet est un **bot WhatsApp intelligent** développé avec Flask et Twilio, qui répond automatiquement aux messages et enregistre les échanges dans un fichier CSV.

## Fonctionnalités
- Réponses automatiques aux messages WhatsApp
- Menu interactif (commande, prix, questions)
- Journalisation des conversations dans un fichier `messages_log.csv`
- Déployable gratuitement sur Render

## Structure du code
- `bot_whatsapp.py` : code principal du bot avec Flask et Twilio
- `requirements.txt` : dépendances nécessaires (Flask, Twilio)
- `messages_log.csv` : fichier local contenant l’historique des messages

## Utilité pour un Data Scientist
- **Collecte de données conversationnelles** : précieuse pour entraîner des modèles de NLP.
- **Automatisation client** : comprendre les habitudes et demandes des clients.
- **Statistiques commerciales** : analyser les volumes de commandes, les mots-clés les plus fréquents, etc.
- **Développement de solutions IA personnalisées** : chatbot intelligent, système de recommandation, etc.

## Comment l'utiliser
1. Installer les dépendances : `pip install -r requirements.txt`
2. Lancer le bot : `python bot_whatsapp.py`
3. Connecter Twilio à l'URL `/webhook` du serveur déployé
4. Tester en envoyant des messages à votre numéro WhatsApp Twilio

## Déploiement sur Render
- Pousser le projet sur GitHub
- Créer un Web Service sur [https://render.com](https://render.com)
- Utiliser la commande de démarrage : `python bot_whatsapp.py`

## Auteur
Bonaventure Besebese — Projet d’étude avec vocation professionnelle.
##Etudiant à L'université de Kinshasa 
## Faculté des sciences et technologies 
## Département de mathématiques & Statistiques et informatiques
