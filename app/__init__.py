import os
from flask import Flask


# Spécifier les chemins pour le dossier 'static' et 'templates'
app = Flask(__name__,
            static_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), '../static'),
            template_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), '../templates'))

# Définir une clé secrète pour les sessions
app.config['SECRET_KEY'] = 'd9911e61d2ae79f90b5c3d82ea63d2d706dda7940e5c0022'  # Remplace par une clé unique et secrète

# Importer les routes après la création de l'application
from app import routes







