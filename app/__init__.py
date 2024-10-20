import os
from flask import Flask

# Spécifier les chemins pour le dossier 'static' et 'templates'
app = Flask(__name__,
            static_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), '../static'),
            template_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), '../templates'))

from app import routes



