import json
from flask import render_template, request, redirect, url_for
from app import app

# Fichier où les utilisateurs seront stockés
USER_FILE = 'data/users.json'

# Charger les utilisateurs depuis un fichier JSON
def load_users():
    try:
        with open(USER_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Sauvegarder les utilisateurs dans un fichier JSON
def save_users(users):
    with open(USER_FILE, 'w') as file:
        json.dump(users, file, indent=4)

# Charger les utilisateurs au démarrage de l'application
users = load_users()

# Route pour afficher la page d'ajout d'utilisateur (index.html)
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Route pour afficher la liste des utilisateurs et ajouter un utilisateur
@app.route('/users', methods=['GET', 'POST'])
def list_users():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        # Ajouter l'utilisateur à la liste
        users.append({'name': name, 'email': email})
        # Sauvegarder dans le fichier JSON
        save_users(users)
        # Rediriger vers la liste des utilisateurs après l'ajout
        return redirect(url_for('list_users'))
    
    # Si méthode GET, afficher la liste des utilisateurs
    return render_template('list_users.html', users=users)
