import os
from jinja2 import Template

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
