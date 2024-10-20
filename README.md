# Application Flask - Gestion d'utilisateurs

## Description du projet

Ce projet est une application simple développée avec Flask qui permet de :

1. Ajouter des utilisateurs via une interface graphique.
2. Lister les utilisateurs ajoutés via une page dédiée.
3. Tester l'API via Postman et l'extension REST Client dans VSCode.

### Fonctionnalités

- Interface utilisateur pour l'ajout d'utilisateurs.
- API REST avec deux routes :
  - **GET** `/users` : Récupère la liste des utilisateurs.
  - **POST** `/users` : Ajoute un nouvel utilisateur à la liste.

---

## Installation

### Prérequis

1. Python 3.x doit être installé sur votre machine.
2. Flask doit être installé dans votre environnement Python.
3. Un environnement virtuel Python est recommandé.

### Étapes

1. Clonez le dépôt du projet sur votre machine :

```bash
git clone https://votre-depot.git
```

2. Accédez au dossier du projet :

```bash
cd Prise-en-Main-de-Flask
```

3. Créez et activez un environnement virtuel :

```bash
python3 -m venv .venv
source .venv/bin/activate  # Sur macOS ou Linux
```

4. Installez les dépendances requises :

```bash
pip install -r requirements.txt
```

5. Lancez l'application :

```bash
python3 run.py
```

L'application sera accessible sur `http://127.0.0.1:5000`.

---

## Utilisation

### Interface graphique

1. Pour ajouter un utilisateur, rendez-vous sur la page d'accueil de l'application via `http://127.0.0.1:5000`.

![Page d'ajout d'utilisateur](docs/images-read-me/un.png)

2. Remplissez le formulaire avec le nom et l'email de l'utilisateur puis cliquez sur "Ajouter". Vous serez redirigé vers la liste des utilisateurs.

![Liste des utilisateurs](docs/images-read-me/deux.png)

3. La liste des utilisateurs peut également être consultée à l'adresse `http://127.0.0.1:5000/users`.

---

### API REST

#### Tester avec Postman

1. **GET** `/users` : Pour récupérer la liste des utilisateurs.

![GET Request in Postman](docs/images-read-me/trois.png)

2. **POST** `/users` : Pour ajouter un utilisateur via l'API.

![POST Request in Postman](docs/images-read-me/quatre.png)

3. **GET** `/users` après ajout : Pour vérifier que l'utilisateur a bien été ajouté.

![GET Request after POST](docs/images-read-me/cinq.png)

#### Tester avec REST Client dans VSCode

1. **GET** `/users` : Récupérer la liste des utilisateurs.

```http
GET http://127.0.0.1:5000/users
```

2. **POST** `/users` : Ajouter un utilisateur.

```http
POST http://127.0.0.1:5000/users
Content-Type: application/json

{
  "name": "Jean Aimare",
  "email": "jeanaimare@example.com"
}
```

---

## Structure du projet

```plaintext
Prise-en-Main-de-Flask/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│
├── static/
│   └── css/
│       └── style.css
│
├── templates/
│   ├── index.html
│   └── list_users.html
│
├── data/
│   └── users.json
│
├── config.py
├── run.py
├── requirements.txt
└── README.md
```

---

## Auteurs

- **Romuald CROCHAT** - Développeur IA en formation

---

## License

Ce projet est sous licence MIT.
