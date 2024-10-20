from flask import render_template, request, redirect, url_for
from app import app

# Liste d'utilisateurs
users = []

# Route pour la page d'accueil (index.html) avec le formulaire d'ajout
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Récupérer les données du formulaire
        name = request.form['name']
        email = request.form['email']
        # Ajouter l'utilisateur à la liste
        users.append({'name': name, 'email': email})
        return redirect(url_for('list_users'))  # Rediriger vers la liste après l'ajout
    return render_template('index.html')  # Charger index.html comme page d'accueil

# Route pour afficher la liste des utilisateurs
@app.route('/users', methods=['GET'])
def list_users():
    return render_template('list_users.html', users=users)
