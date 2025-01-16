import unittest
import os
from compiler.parser import parse_xml_to_app
from utils.template import load_file

class TestGraphQL(unittest.TestCase):
    """
    Classe de test pour vérifier la compilation d'un fichier XML en schéma GraphQL.
    """

    def test_compilation(self):
        """
        Teste si un fichier XML est correctement compilé en un schéma GraphQL attendu.
        """
        # Définir les chemins des fichiers nécessaires
        app_path = os.path.join(os.path.dirname(__file__), "data", "test.xml")
        graphql_path = os.path.join(os.path.dirname(__file__), "data", "schema.graphql")
        
        try:
            # Charger le fichier XML et le convertir en objet "App"
            app = parse_xml_to_app(load_file(app_path))
            
            # Compiler l'objet "App" en schéma GraphQL
            compiled_graphql_schema = app.api.compile_to_graphql().strip()
            
            # Charger le schéma GraphQL attendu depuis le fichier
            expected_graphql_schema = load_file(graphql_path).strip()

            # Log des schémas pour débogage en cas d'échec
            print("Compiled GraphQL Schema:\n", compiled_graphql_schema)
            print("Expected GraphQL Schema:\n", expected_graphql_schema)

            # Vérifier l'égalité entre le schéma compilé et celui attendu
            self.assertEqual(compiled_graphql_schema, expected_graphql_schema)
        except FileNotFoundError as e:
            self.fail(f"Fichier introuvable : {e}")
        except Exception as e:
            self.fail(f"Erreur inattendue lors de la compilation : {e}")

if __name__ == "__main__":
    unittest.main()
