from Dataclass.apiField import ApiField
from Dataclass.compilable import Compilable


class Model(Compilable):
    """
    Représente un modèle compilable en Prisma et GraphQL.
    """

    def __init__(self, name):
        self.name = name
        self.fields = []

    def add_field(self, field):
        if not isinstance(field, ApiField):
            raise TypeError("Le champ doit être une instance de Field.")
        self.fields.append(field)

    def compile_to_prisma(self):
        prisma_fields = "\n".join([field.compile_to_prisma() for field in self.fields])
        return f"model {self.name} {{\n{prisma_fields}\n}}"

    def compile_to_graphql(self):
        graphql_fields = "\n".join([field.compile_to_graphql() for field in self.fields])
        return f"type {self.name} {{\n{graphql_fields}\n}}"
