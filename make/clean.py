import os
import subprocess

def clean_api_directories(sufix):
    """Supprime tous les dossiers qui se terminent par -api dans le répertoire courant."""
    current_dir = os.getcwd()
    for item in os.listdir(current_dir):
        item_path = os.path.join(current_dir, item)
        if os.path.isdir(item_path) and item.endswith(sufix):
            print(f"Removing directory: {item_path}")
            subprocess.run(["rm", "-rf", item_path])

def clean_app(sufix="-app"):
    clean_api_directories(sufix)

if __name__ == "__main__":
    clean_app()