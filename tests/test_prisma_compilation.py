import unittest
import os
from compiler.parser import parse_xml_to_app
from utils.template import load_file

class TestPrisma(unittest.TestCase):
    """
    Classe de test pour vérifier la compilation d'un fichier XML en schéma Prisma GraphQL.
    """
    
    def test_compilation(self):
        """
        Teste si un fichier XML est correctement compilé en un schéma Prisma GraphQL.
        """
        # Définir les chemins des fichiers nécessaires pour le test
        app_path = os.path.join(os.path.dirname(__file__), "data", "test.xml")
        graphQL_path = os.path.join(os.path.dirname(__file__), "data", "schema.prisma")
        
        try:
            # Charger le fichier XML et le convertir en objet "App"
            app = parse_xml_to_app(load_file(app_path))
            
            # Compiler l'objet "App" en schéma Prisma GraphQL
            compiled_graphql_schema = app.api.compile_to_prisma().strip()

            # Charger le schéma Prisma attendu depuis le fichier
            expected_graphql_schema = load_file(graphQL_path).strip()
            
            # Log des schémas pour débogage en cas d'échec
            print("Compiled GraphQL Schema:\n", compiled_graphql_schema)
            print("Expected GraphQL Schema:\n", expected_graphql_schema)

            # Vérification de l'égalité entre le schéma compilé et celui attendu
            self.assertEqual(compiled_graphql_schema, expected_graphql_schema)
        except FileNotFoundError as e:
            self.fail(f"Fichier manquant : {e}")
        except Exception as e:
            self.fail(f"Erreur inattendue pendant le test : {e}")
            
if __name__ == "__main__":
    unittest.main()