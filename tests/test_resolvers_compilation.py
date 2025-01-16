import unittest
import os
from Dataclass.back.model import Model
from compiler.parser import parse_xml_to_app
from utils.template import load_file

class TestResolversCompilation(unittest.TestCase):
    """
    Classe de test pour vérifier que la compilation de chaque modèle (resolver) génère le schéma attendu.
    """

    def test_resolvers_compilation(self):
        """
        Teste la compilation de chaque modèle de l'API en resolvers GraphQL et compare le résultat attendu.
        """
        # Définir les chemins des fichiers nécessaires pour le test
        app_path = os.path.join(os.path.dirname(__file__), "data", "test.xml")
        resolvers_path = os.path.join(os.path.dirname(__file__), "data", "resolvers")

        try:
            # Charger le fichier XML et le convertir en objet "App"
            app = parse_xml_to_app(load_file(app_path))

            # Vérifier si l'objet "App" a des modèles
            if not hasattr(app.api, "models") or not app.api.models:
                self.fail("Aucun modèle trouvé dans l'objet API chargé depuis le fichier XML.")

            # Parcourir chaque modèle défini dans l'API
            for model in app.api.models:
                # Vérifier que chaque modèle est une instance de Model
                self.assertIsInstance(
                    model,
                    Model,
                    f"L'objet {model} dans app.api.models n'est pas une instance de Model."
                )
                
                # Compiler le resolver à partir du modèle
                compiled_resolver_from_model = model.compile_to_prisma_resolver().strip()

                # Générer le chemin du fichier attendu
                target_file = os.path.join(resolvers_path, f"{model.name}.js")

                # Charger le resolver attendu depuis le fichier correspondant
                if not os.path.isfile(target_file):
                    self.fail(f"Le fichier attendu pour le modèle {model.name} est introuvable : {target_file}")

                expected_resolver = load_file(target_file).strip()

                # Logs pour débogage en cas d'échec
                print(f"\nModèle testé : {model.name}")
                print("Resolver compilé :\n", compiled_resolver_from_model)
                print("Resolver attendu :\n", expected_resolver)

                # Vérifier que le resolver compilé correspond au resolver attendu
                self.assertEqual(
                    compiled_resolver_from_model,
                    expected_resolver,
                    f"Le resolver compilé pour le modèle {model.name} ne correspond pas au fichier attendu."
                )
        except FileNotFoundError as e:
            self.fail(f"Fichier manquant : {e}")
        except Exception as e:
            self.fail(f"Erreur inattendue pendant le test : {e}")

if __name__ == "__main__":
    unittest.main()
