
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
        graphql_models = "\n\n".join([model.compile_to_graphql() for model in self.models])
        return f"# API: {self.name}\n\n{graphql_models}"