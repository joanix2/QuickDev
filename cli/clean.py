import os
from utils.command import run_command

def clean_api_directories(sufix):
    """Supprime tous les dossiers qui se terminent par -api dans le répertoire courant."""
    current_dir = os.getcwd()
    for item in os.listdir(current_dir):
        item_path = os.path.join(current_dir, item)
        if os.path.isdir(item_path) and item.endswith(sufix):
            print(f"Removing directory: {item_path}")
            run_command(f"rm -rf {item_path}")

def delete_schema(name = "schema.graphql"):
    if os.path.exists(os.path.join(os.getcwd(), name)):
        run_command(f"rm {name}")

def clean_app(sufix="_app"):
    clean_api_directories(sufix)
    delete_schema()

if __name__ == "__main__":
    clean_app()