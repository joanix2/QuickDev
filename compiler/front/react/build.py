import os

from compiler.env.build import init_front_dotenv
from utils.template import create_file, load_template_from_file

def create_react_server(path, name):
    # Nom du dossier principal
    front_dir = os.path.join(path, f"{name}-front")

    if not os.path.exists(front_dir):
        os.makedirs(front_dir)

    # Create env
    init_front_dotenv(front_dir)