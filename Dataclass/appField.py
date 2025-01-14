from Dataclass.back.apiCompilable import ApiCompilable
from Dataclass.fieldType import FieldType



class ApiField(ApiCompilable):
    """
    Représente un champ d'un modèle, compilable en Prisma et GraphQL.
    """

    def __init__(self, name, field_type, is_nullable=False, is_primary_key=False, is_unique=False, default_value=None):
        if not isinstance(field_type, FieldType):
            raise TypeError("Le type du champ doit être une instance de FieldType.")
        self.name = name
        self.field_type = field_type
        self.is_nullable = is_nullable
        self.is_primary_key = is_primary_key
        self.is_unique = is_unique
        self.default_value = default_value

    def compile_to_prisma(self):
        prisma_parts = [f"{self.name} {self.field_type.compile_to_prisma()}"]
        if self.is_primary_key:
            prisma_parts.append("@id")
        if self.is_unique:
            prisma_parts.append("@unique")
        if self.is_nullable:
            prisma_parts.append("?")
        if self.default_value is not None:
            prisma_parts.append(f"@default({self.default_value})")
        return " ".join(prisma_parts)

    def compile_to_graphql(self):
        graphql_type = self.field_type.compile_to_graphql()
        if self.is_nullable:
            graphql_type = f"{graphql_type}"
        else:
            graphql_type = f"{graphql_type}!"
        return f"{self.name}: {graphql_type}"
