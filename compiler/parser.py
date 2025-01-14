
import xml.etree.ElementTree as ET

from Dataclass.back.api import Api
from Dataclass.appField import ApiField
from Dataclass.fieldType import FieldType
from Dataclass.back.model import Model

def parse_xml_to_api(xml_string):
    """
    Parse un code XML pour générer une API avec des modèles et des champs.

    :param xml_string: Code XML sous forme de chaîne
    :return: Une instance d'Api
    """
    root = ET.fromstring(xml_string)
    api_name = root.attrib.get("name", "GeneratedApi")
    api = Api(api_name)

    for model_elem in root.findall("model"):
        model_name = model_elem.attrib["name"]
        model = Model(model_name)

        for field_elem in model_elem.findall("field"):
            field_name = field_elem.attrib["name"]
            field_type = FieldType[field_elem.attrib["type"].upper()]
            is_nullable = field_elem.attrib.get("nullable", "false").lower() == "true"
            is_primary_key = field_elem.attrib.get("primary", "false").lower() == "true"
            is_unique = field_elem.attrib.get("unique", "false").lower() == "true"
            default_value = field_elem.attrib.get("default")

            field = ApiField(
                field_name, field_type, is_nullable, is_primary_key, is_unique, default_value
            )
            model.add_field(field)

        api.add_model(model)

    return api
