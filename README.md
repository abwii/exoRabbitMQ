# 🐇 exoRabbitMQ

Ce projet est un exercice pédagogique illustrant l'utilisation de RabbitMQ avec Python. Il met en œuvre un producteur, un consommateur et un worker pour traiter des messages asynchrones via une interface web Flask.

## 🛠 Prérequis

- Python 3.7 ou supérieur
- Docker et Docker Compose
- pip (pour installer les dépendances)
- RabbitMQ (lancé via Docker)

## 🚀 Installation

1. **Cloner le dépôt**

```bash
git clone https://github.com/abwii/exoRabbitMQ.git
cd exoRabbitMQ
```

2. **Installer les dépendances**

```bash
pip install -r requirements.txt
```

4. **Lancer RabbitMQ via Docker**

```bash
docker-compose up -d
```

6. **Démarrer l'application flask**

```bash
python app.py
```

L’interface sera accessible à l’adresse : http://localhost:5000


📬 Envoi et traitement des messages

Ouvrir 3 terminaux séparés et exécuter :

    Producteur : python producer.py

    Consommateur : python consumer.py

    Worker : python worker.py

🧪 Exemple d'utilisation

    Accédez à l'application Flask.

    Envoyez un message via le formulaire web.

    Le producteur l’envoie à RabbitMQ.

    Le consommateur lit le message.

    Le worker le traite et affiche le résultat.

📚 Ressources

    RabbitMQ

    Pika (client Python)

    Flask
