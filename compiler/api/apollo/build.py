import os
from Dataclass.back.api import Api
from compiler.env.build import init_api_dotenv
from utils.command import run_command
from utils.template import create_file, load_template_from_file

def init_apollo(cwd, schema):
    # Initialisation du projet Node.js
    run_command("npm init -y", cwd=cwd)  # Initialise un package.json
    run_command("npm install apollo-server graphql", cwd=cwd)  # Installe Apollo Server

    # Chemins des templates
    index_js_template_path = os.path.join(os.path.dirname(__file__), "templates", "index.js.jinja")
    # schema_graphql_template_path = os.path.join("templates", "api", "schema.graphql.jinja")

    # Charger et créer les fichiers en utilisant les fonctions utilitaires
    src_dir = os.path.join(cwd, "src")
    create_file(src_dir, "index.js", load_template_from_file(index_js_template_path))
    # create_file(src_dir, "resolvers.js", "module.exports = {};")
    create_file(src_dir, "schema.graphql", schema)

def init_prisma(cwd):
    run_command("npm install prisma @prisma/client", cwd=cwd)
    run_command("yes | npx prisma init", cwd=cwd)

    prisma_path = os.path.join(cwd, "prisma")
    prisma_template_path = os.path.join(os.path.dirname(__file__), "templates", "prisma.jinja")
    create_file(prisma_path, "schema.prisma", load_template_from_file(prisma_template_path))

    run_command("yes | npx prisma generate", cwd=cwd)
    run_command("yes | npx prisma migrate dev --name init", cwd=cwd)

def create_apollo_server(path, api: Api):
    # Nom du dossier principal
    api_dir = os.path.join(path, f"{api.name}-api")

    if not os.path.exists(api_dir):
        os.makedirs(api_dir)

    # Create env
    init_api_dotenv(api_dir)

    init_apollo(cwd=api_dir, schema=api.compile_to_graphql())
    init_prisma(api_dir)