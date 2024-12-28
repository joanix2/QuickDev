import os
import yaml
import warnings

DATABASE = 'database'
API = 'api'
FRONT = 'front'

def parse_yaml_with_checks(file_path):
    """
    Parse un fichier YAML, retourne un dictionnaire avec les chemins absolus
    et génère des avertissements si des éléments sont manquants.

    Args:
        file_path (str): Chemin vers le fichier YAML à parser.

    Returns:
        dict: Un dictionnaire avec les chemins absolus et les warnings si nécessaire.
    """
    # Charger le fichier YAML
    try:
        with open(file_path, 'r') as file:
            config = yaml.safe_load(file)
    except Exception as e:
        raise RuntimeError(f"Erreur lors du chargement du fichier YAML : {e}")

    # Clés essentielles attendues
    required_keys = [DATABASE, API, FRONT]

    # Liste des types de bases de données valides
    valid_database_types = ['mongo', 'postgres']
    
    api = {}
    front = {}

    # Vérification et conversion en chemins absolus
    for key in required_keys:
        if key not in config:
            warnings.warn(f"Clé manquante dans le fichier YAML : {key}")
        else:
            if key == DATABASE:
                db_type = config[DATABASE].get('type', 'inconnu')
                if db_type not in valid_database_types:
                    raise ValueError(f"Type de base de données invalide ou inconnu : {db_type}. Types valides : {valid_database_types}")
                db = db_type
            elif key == API:
                schema_path = config[API].get('schema')
                if schema_path:
                    api = os.path.abspath(schema_path)
                else:
                    warnings.warn("Clé 'schema' manquante sous 'api'")
            elif key == FRONT:
                for sub_key, sub_value in config[FRONT].items():
                    front[sub_key] = os.path.abspath(sub_value)

    return db , api , front
