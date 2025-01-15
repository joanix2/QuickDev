
from Dataclass.back.apiCompilable import ApiCompilable
from Dataclass.back.model import Model


class Api(ApiCompilable):
    """
    Représente une API contenant un nom et une liste de modèles.
    """

    def __init__(self, name):
        self.name = name
        self.models = []

    def add_model(self, model):
        if not isinstance(model, Model):
            raise TypeError("Le modèle doit être une instance de Model.")
        self.models.append(model)

    def compile_to_prisma(self):
        prisma_models = "\n\n".join([model.compile_to_prisma() for model in self.models])
        return f"// API: {self.name}\n\n{prisma_models}"

    def compile_to_graphql(self):
        # Générer les types des modèles
        graphql_models = "\n\n".join([model.compile_to_graphql() for model in self.models])

        # Générer les queries et mutations
        graphql_queries = self._generate_queries()
        graphql_mutations = self._generate_mutations()

        return (
            f"# API: {self.name}\n\n"
            f"{graphql_models}\n\n"
            f"type Query {{\n{graphql_queries}\n}}\n\n"
            f"type Mutation {{\n{graphql_mutations}\n}}"
        )

    def _generate_queries(self):
        """
        Génère les queries pour tous les modèles.
        """
        queries = []
        for model in self.models:
            # Générer les requêtes de base pour chaque modèle
            queries.append(f"\tget{model.name}ById(id: ID!): {model.name}")
            queries.append(f"\tlist{model.name}s: [{model.name}]")
        return "\n".join(queries)

    def _generate_mutations(self):
        """
        Génère les mutations pour tous les modèles.
        """
        mutations = []
        for model in self.models:
            # Générer les mutations de base pour chaque modèle
            mutations.append(f"\tcreate{model.name}(input: {model.name}!): {model.name}")
            mutations.append(f"\tupdate{model.name}(id: ID!, input: {model.name}!): {model.name}")
            mutations.append(f"\tdelete{model.name}(id: ID!): Boolean")
        return "\n".join(mutations)