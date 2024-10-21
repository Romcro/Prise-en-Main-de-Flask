import os
from flask import Flask
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier `.env`
load_dotenv()

# Créer l'objet Flask `app`
app = Flask(__name__,
            static_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), '../static'),
            template_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), '../templates'))

# Charger la clé secrète depuis les variables d'environnement
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Importer les routes après la création de l'application
from app import routes
