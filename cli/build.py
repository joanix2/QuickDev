import os
import subprocess
from templates.template import *

def run_command(command, cwd=None):
    """
    Exécute une commande shell et affiche la sortie.
    """
    try:
        subprocess.run(command, shell=True, check=True, cwd=cwd)
        print(f"Command succeeded: {command}")
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {command}")
        print(e)

def init_dotenv(cwd):
    dotenv_path = os.path.join("templates", "env", "dotenv.jinja")
    create_file(cwd, ".env", load_template_from_file(dotenv_path))

def init_apollo(cwd):
    # Initialisation du projet Node.js
    run_command("npm init -y", cwd=cwd)  # Initialise un package.json
    run_command("npm install apollo-server graphql", cwd=cwd)  # Installe Apollo Server

    # Chemins des templates
    index_js_template_path = os.path.join("templates", "api", "index.js.jinja")
    schema_graphql_template_path = os.path.join("templates", "api", "schema.graphql.jinja")

    # Charger et créer les fichiers en utilisant les fonctions utilitaires
    src_dir = os.path.join(cwd, "src")
    create_file(src_dir, "index.js", load_template_from_file(index_js_template_path))
    # create_file(src_dir, "resolvers.js", "module.exports = {};")
    create_file(src_dir, "schema.graphql", load_template_from_file(schema_graphql_template_path))


def init_prisma(cwd):
    run_command("npm install prisma @prisma/client", cwd=cwd)
    run_command("yes | npx prisma init", cwd=cwd)

    prisma_path = os.path.join(cwd, "prisma")
    prisma_template_path = os.path.join("templates", "api", "prisma.jinja")
    create_file(prisma_path, "schema.prisma", load_template_from_file(prisma_template_path))

    run_command("npx prisma generate", cwd=cwd)
    run_command("npx prisma migrate dev --name init", cwd=cwd)

def create_apollo_server(path, name):
    # Nom du dossier principal
    api_dir = os.path.join(path, f"{name}-api")

    if not os.path.exists(api_dir):
        os.makedirs(api_dir)

    init_apollo(api_dir)
    init_prisma(api_dir)

def create_react_server(path, name):
    # Nom du dossier principal
    api_dir = os.path.join(path, f"{name}-front")

    if not os.path.exists(api_dir):
        os.makedirs(api_dir)

def create_env(path):
    init_dotenv(path)

def build_app(name):
    # Nom du dossier principal
    app_dir = os.path.join(os.getcwd(), f"{name}-app")

    if not os.path.exists(app_dir):
        os.makedirs(app_dir)

    # Create env
    create_env(app_dir)

    # Create API
    create_apollo_server(app_dir, name)

    # Create Front
    create_react_server(app_dir, name)

if __name__ == "__main__":
    # Exemple d'utilisation
    build_app("example")

