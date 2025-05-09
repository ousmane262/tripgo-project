
readme_content = """# 🌍 TripGo

**TripGo** est une application web de réservation de destinations touristiques et d’événements internationaux. Elle permet à un utilisateur de :
- s’inscrire, se connecter et modifier son profil,
- parcourir des destinations (villes, festivals, événements…),
- réserver un voyage pour une période donnée,
- suivre ses réservations, paiements et avis.

## ✨ Technologies utilisées

- **Backend** : Django 5.x, Python 3.11
- **Frontend** : HTML, Bootstrap 5
- **Base de données** : Postgresql (développement)
- **Authentification** : Django User Model personnalisé
- **Paiement** : (à simuler ou ajouter via Stripe)

## 🚀 Installation rapide

```bash
git clone https://github.com/ousmane262/tripgo.git
cd tripgo
python -m venv env
source env/bin/activate  # ou `env\\Scripts\\activate` sur Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata destinations_fixture.json  # (si fourni)
python manage.py runserver
🛠️ Fonctionnalités
Système d’inscription et de connexion utilisateur

Réservations en ligne d’événements à venir

Paiements et historiques

Dashboard profil dynamique avec animation

Backend sécurisé et extensible

📁 Structure du projet
csharp
Toujours afficher les détails

Copier
tripgo/
├── core/                 # App principale
├── templates/            # Fichiers HTML
├── static/               # Fichiers CSS, images, JS
├── fixtures/             # Données initiales (destinations)
├── manage.py
└── README.md
📌 Auteur
Développé par Ousmane, étudiant en Génie Informatique – Université Ottawa.

🧠 “Le voyage est la seule chose qu’on achète qui nous rend plus riche.”
