import os
from Dataclass.app import App
from Dataclass.back.api import Api
from compiler.env.build import create_env
from compiler.api.apollo.build import create_apollo_server
from compiler.front.react.build import create_react_server


def build_app(path, app: App):
    # Nom du dossier principal
    app_dir = os.path.join(path, f"{app.name}-app")

    if not os.path.exists(app_dir):
        os.makedirs(app_dir)

    # Create env
    create_env(app_dir)

    # Create API
    create_apollo_server(app_dir, app.api)

    # Create Front
    create_react_server(app_dir, app.front)

if __name__ == "__main__":
    # Exemple d'utilisation
    build_app("example")

