from app import app  # Importer `app` défini dans __init__.py
import json
from flask import render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash

# Charger les utilisateurs depuis un fichier JSON
def load_users():
    try:
        with open('data/users.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Sauvegarder les utilisateurs dans un fichier JSON
def save_users(users):
    with open('data/users.json', 'w') as file:
        json.dump(users, file, indent=4)

# Chargement des utilisateurs
users = load_users()

# Route pour la page d'accueil
@app.route('/')
def index():
    return render_template('index.html')

# Route pour l'inscription des utilisateurs
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']  # Le mot de passe entré par l'utilisateur

        # Hashage du mot de passe
        hashed_password = generate_password_hash(password)

        # Vérifier si l'email existe déjà
        user = next((u for u in users if u['email'] == email), None)
        if user:
            flash('Un compte avec cet email existe déjà.', 'error')
            return redirect(url_for('register'))

        # Ajouter l'utilisateur avec le mot de passe hashé
        users.append({'name': name, 'email': email, 'password': hashed_password})
        save_users(users)

        # Connexion automatique après l'inscription
        session['user'] = name  # Définir l'utilisateur dans la session
        print(f"Utilisateur connecté après inscription : {session['user']}")  # Débogage
        flash('Inscription réussie !', 'success')

        return redirect(url_for('dashboard'))  # Rediriger vers le tableau de bord

    return render_template('register.html')

# Route pour la connexion des utilisateurs
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Rechercher l'utilisateur par email
        user = next((u for u in users if u['email'] == email), None)

        # Vérifier que l'utilisateur existe et a un mot de passe
        if user and 'password' in user:
            # Si l'utilisateur a un mot de passe, vérifier qu'il est correct
            if check_password_hash(user['password'], password):
                # Stocker le nom d'utilisateur dans la session pour reconnaître l'utilisateur connecté
                session['user'] = user['name']
                print(f"Utilisateur connecté après connexion : {session['user']}")  # Débogage
                flash(f'Bienvenue {user["name"]} !', 'success')
                return redirect(url_for('dashboard'))  # Rediriger vers le tableau de bord
            else:
                flash('Mot de passe incorrect.', 'error')
        else:
            flash('Email ou mot de passe incorrect.', 'error')

        # Rediriger vers la page de connexion en cas d'échec
        return redirect(url_for('login'))

    return render_template('login.html')

# Route pour le tableau de bord (disponible uniquement si l'utilisateur est connecté)
@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        # Afficher le tableau de bord pour l'utilisateur connecté
        print(f"Accès au tableau de bord pour : {session['user']}")  # Débogage
        return render_template('dashboard.html', user=session['user'], users=users)
    
    # Si l'utilisateur n'est pas connecté, afficher un message d'erreur et rediriger vers la page de connexion
    flash('Veuillez vous connecter pour accéder à cette page.', 'error')
    return redirect(url_for('login'))

# Route pour déconnexion
@app.route('/logout')
def logout():
    if 'user' in session:
        print(f"Déconnexion de : {session['user']}")  # Débogage
    session.pop('user', None)  # Supprimer l'utilisateur de la session
    flash('Vous avez été déconnecté.', 'info')
    return redirect(url_for('login'))
