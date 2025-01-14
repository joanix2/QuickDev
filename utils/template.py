import os
from jinja2 import Template

def load_file(file_path):
    """
    Charge le contenu d'un fichier donné et le retourne.

    :param file_path: str, chemin vers le fichier à charger
    :return: str, contenu du fichier
    :raises FileNotFoundError: si le fichier n'existe pas
    :raises IOError: si une erreur d'entrée/sortie se produit
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        raise FileNotFoundError(f"Le fichier spécifié n'existe pas : {file_path}")
    except IOError as e:
        raise IOError(f"Une erreur s'est produite lors de la lecture du fichier : {e}")

def load_template_from_file(template_path, params=None):
    """Charge un template à partir d'un fichier et remplace les variables avec les paramètres donnés."""
    params = params or {}
    with open(template_path, 'r') as file:
        template_content = file.read()
    template = Template(template_content)
    return template.render(**params)

def create_file(path, filename, content):
    """Crée un fichier avec le contenu donné au chemin spécifié."""
    os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, filename), "w") as file:
        file.write(content)
