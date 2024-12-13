import os
import subprocess

def get_app_dir(app_suffix) :
    # Trouver le répertoire courant qui se termine par -api
    current_dir = os.getcwd()
    for item in os.listdir(current_dir):
        item_path = os.path.join(current_dir, item)
        if os.path.isdir(item_path) and item.endswith(app_suffix):
            return item_path
        
def get_api_dir(app_suffix, api_suffix):
    # Récupérer le répertoire de l'application
    app_dir = get_app_dir(app_suffix)  # Fonction à définir séparément

    # Récupérer le dernier dossier (nom du dossier)
    last_folder = os.path.basename(app_dir)
    suffix = last_folder[-len(app_suffix):]

    # Vérifier si le dernier dossier correspond à app_suffix
    if suffix != app_suffix:
        raise ValueError(f"Le dernier dossier ({last_folder}) ne correspond pas au suffixe spécifié ({app_suffix}).")

    # Remplacer le dernier dossier par api_suffix
    api_folder = last_folder[:-len(app_suffix)] + api_suffix  # Récupère le chemin parent de app_dir
    api_dir = os.path.join(app_dir, api_folder)  # Ajouter le suffixe API

    return api_dir

def run_api_directories(app_suffix, api_suffix):
    current_dir = get_api_dir(app_suffix, api_suffix)
    if current_dir:
        print("Starting Apollo Server...")
        subprocess.run(["node", "src/index.js"], cwd=current_dir)
    else:
        print("Current directory does not end with -api. Please navigate to the appropriate directory.")

def run_app(app_suffix="-app", api_suffix="-api"):
    run_api_directories(app_suffix, api_suffix)

if __name__ == "__main__":
    run_app()