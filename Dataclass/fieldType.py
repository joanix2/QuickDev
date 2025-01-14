from enum import Enum

class FieldType(Enum):
    """
    Enum pour représenter les types de champs.
    """
    STRING = "String"
    INT = "Int"
    FLOAT = "Float"
    BOOLEAN = "Boolean"
    ID = "ID"

    def compile_to_prisma(self):
        return self.value

    def compile_to_graphql(self):
        return self.value