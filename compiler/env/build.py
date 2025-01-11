import os
from utils.command import run_command
from utils.template import create_file, load_template_from_file

def init_dotenv(cwd, env_type):
    """
    Initialise un fichier .env dans le répertoire spécifié en utilisant le template correspondant.

    :param cwd: Répertoire cible pour créer le fichier .env.
    :param env_type: Type d'environnement ('front', 'api', 'app', etc.) pour sélectionner le template.
    """
    template_file = f"{env_type}-dotenv.jinja"
    template_path = os.path.join(os.path.dirname(__file__), "templates", template_file)
    create_file(cwd, ".env", load_template_from_file(template_path))

def init_front_dotenv(cwd):
    """Initialise un fichier .env pour l'environnement frontend."""
    init_dotenv(cwd, "front")

def init_api_dotenv(cwd):
    """Initialise un fichier .env pour l'environnement API."""
    init_dotenv(cwd, "api")

def init_app_dotenv(cwd):
    """Initialise un fichier .env pour l'environnement d'application."""
    init_dotenv(cwd, "app")

def create_env(cwd):
    """
    Crée un fichier .env dans le répertoire spécifié en utilisant le template d'application.
    """
    run_command("nvm install --lts", cwd=cwd)
    run_command("nvm use --lts", cwd=cwd)
    
    init_app_dotenv(cwd)
