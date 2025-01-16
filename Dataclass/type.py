from enum import Enum

class FieldType(Enum):
    """
    Enum pour représenter les types primitifs.
    """
    STRING = "String"
    INT = "Int"
    FLOAT = "Float"
    BOOLEAN = "Boolean"
    ID = "ID"


class BaseType:
    """
    Classe de base pour tous les types.
    """
    def __init__(self, nullable: bool = True):
        self.nullable = nullable

    def compile_to_graphql(self):
        raise NotImplementedError

    def compile_to_prisma(self):
        raise NotImplementedError


class PrimitiveType(BaseType):
    """
    Représente un type primitif comme String, Int, etc.
    """
    def __init__(self, field_type: FieldType, nullable: bool = True):
        super().__init__(nullable)
        self.field_type = field_type

    def compile_to_graphql(self):
        return self.field_type.value

    def compile_to_prisma(self):
        return self.field_type.value

class ModelType(BaseType):
    """
    Représente un type qui fait référence à un modèle.
    """
    def __init__(self, model_name: str, nullable: bool = True):
        super().__init__(nullable)
        self.model_name = model_name

    def compile_to_graphql(self):
        return self.model_name

    def compile_to_prisma(self):
        return self.model_name

class ListType(BaseType):
    """
    Représente un type liste.
    """
    def __init__(self, inner_type: BaseType, nullable: bool = True):
        super().__init__(nullable)
        self.inner_type = inner_type

    def compile_to_graphql(self):
        return f"[{self.inner_type.compile_to_graphql()}]"

    def compile_to_prisma(self):
        return f"{self.inner_type.compile_to_prisma()}[]"
    

def parse_graphql_type(type_string: str) -> BaseType:
    """
    Parse une chaîne de type GraphQL en un objet BaseType.
    Exemple :
      - `[Link!]!` -> ListType(ModelType("Link", nullable=False), nullable=False)
      - `String!` -> PrimitiveType(FieldType.STRING, nullable=False)
    """
    # Supprimer les espaces inutiles
    type_string = type_string.strip()

    # Vérifier si le type est une liste : [Type]
    if type_string.startswith('[') and type_string.endswith(']'):
        inner_type_string = type_string[1:-1]  # Retirer les crochets
        nullable = not type_string.endswith(']!')  # Vérifie si le type liste est nullable
        inner_type = parse_graphql_type(inner_type_string)  # Appel récursif
        return ListType(inner_type, nullable=nullable)

    # Vérifier si le type est non nullable : Type!
    if type_string.endswith('!'):
        inner_type_string = type_string[:-1]  # Retirer le point d'exclamation
        inner_type = parse_graphql_type(inner_type_string)  # Appel récursif
        inner_type.nullable = False
        return inner_type

    # Sinon, c'est un type primitif ou un modèle
    # Vérifier s'il s'agit d'un type primitif connu
    for field_type in FieldType:
        if type_string == field_type.value:
            return PrimitiveType(field_type, nullable=True)

    # Si ce n'est pas un type primitif, on suppose que c'est un modèle
    return ModelType(type_string, nullable=True)
