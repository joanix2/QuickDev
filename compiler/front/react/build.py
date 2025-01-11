import os
from compiler.env.build import init_front_dotenv
from utils.command import run_command


def create_react_server(path, name):
    # Définition du chemin du dossier principal du projet frontend
    front_dir = os.path.join(path, f"{name}-front")

    # Création du répertoire s'il n'existe pas
    if not os.path.exists(front_dir):
        os.makedirs(front_dir)

    # Exécution de la commande pour créer un projet React avec Vite dans le répertoire créé
    run_command("npm create vite@latest . -- --template react", cwd=front_dir)
    run_command("npm install", cwd=front_dir)

    # Initialisation du fichier .env dans le répertoire frontend
    init_front_dotenv(front_dir)
