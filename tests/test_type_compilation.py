import unittest
from Dataclass.type import FieldType, ListType, ModelType, PrimitiveType, parse_graphql_type

class TestGraphQLTypeParsing(unittest.TestCase):
    def test_primitive_type(self):
        # Test d'un type primitif nullable
        graphql_type = "String"
        parsed_type = parse_graphql_type(graphql_type)
        self.assertIsInstance(parsed_type, PrimitiveType)
        self.assertEqual(parsed_type.field_type, FieldType.STRING)
        self.assertTrue(parsed_type.nullable)

        # Test d'un type primitif non nullable
        graphql_type = "Int!"
        parsed_type = parse_graphql_type(graphql_type)
        self.assertIsInstance(parsed_type, PrimitiveType)
        self.assertEqual(parsed_type.field_type, FieldType.INT)
        self.assertFalse(parsed_type.nullable)

    def test_model_type(self):
        # Test d'un modèle nullable
        graphql_type = "User"
        parsed_type = parse_graphql_type(graphql_type)
        self.assertIsInstance(parsed_type, ModelType)
        self.assertEqual(parsed_type.model_name, "User")
        self.assertTrue(parsed_type.nullable)

        # Test d'un modèle non nullable
        graphql_type = "User!"
        parsed_type = parse_graphql_type(graphql_type)
        self.assertIsInstance(parsed_type, ModelType)
        self.assertEqual(parsed_type.model_name, "User")
        self.assertFalse(parsed_type.nullable)

    def test_list_type(self):
        # Test d'une liste simple
        graphql_type = "[String]"
        parsed_type = parse_graphql_type(graphql_type)
        self.assertIsInstance(parsed_type, ListType)
        self.assertIsInstance(parsed_type.inner_type, PrimitiveType)
        self.assertEqual(parsed_type.inner_type.field_type, FieldType.STRING)
        self.assertTrue(parsed_type.nullable)

        # Test d'une liste non nullable
        graphql_type = "[Int]!"
        parsed_type = parse_graphql_type(graphql_type)
        self.assertIsInstance(parsed_type, ListType)
        self.assertIsInstance(parsed_type.inner_type, PrimitiveType)
        self.assertEqual(parsed_type.inner_type.field_type, FieldType.INT)
        self.assertFalse(parsed_type.nullable)

    def test_nested_list_type(self):
        # Test d'une liste imbriquée avec un modèle
        graphql_type = "[[User!]!]!"
        parsed_type = parse_graphql_type(graphql_type)
        self.assertIsInstance(parsed_type, ListType)
        self.assertFalse(parsed_type.nullable)
        
        inner_list = parsed_type.inner_type
        self.assertIsInstance(inner_list, ListType)
        self.assertFalse(inner_list.nullable)
        
        inner_model = inner_list.inner_type
        self.assertIsInstance(inner_model, ModelType)
        self.assertFalse(inner_model.nullable)
        self.assertEqual(inner_model.model_name, "User")

    def test_invalid_type(self):
        # Test avec une chaîne invalide
        graphql_type = "InvalidType!"
        parsed_type = parse_graphql_type(graphql_type)
        self.assertIsInstance(parsed_type, ModelType)
        self.assertEqual(parsed_type.model_name, "InvalidType")
        self.assertFalse(parsed_type.nullable)


if __name__ == "__main__":
    unittest.main()
