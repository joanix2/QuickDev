import os
from Dataclass.front.front import Front
from compiler.env.build import init_front_dotenv
from utils.command import run_command
from utils.format_text import to_snake_case


def create_react_server(path, front : Front):
    # Définition du chemin du dossier principal du projet frontend
    front_snake_case_name = to_snake_case(front.name)
    front_dir = os.path.join(path, front_snake_case_name)

    # Création du répertoire s'il n'existe pas
    if not os.path.exists(front_dir):
        os.makedirs(front_dir)

    # Exécution de la commande pour créer un projet React avec Vite dans le répertoire créé
    run_command("npm create vite@latest . -- --template react", cwd=front_dir)
    run_command("npm install", cwd=front_dir)

    # Initialisation du fichier .env dans le répertoire frontend
    init_front_dotenv(front_dir)
