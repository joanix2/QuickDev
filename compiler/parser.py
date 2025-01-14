
import xml.etree.ElementTree as ET

from Dataclass.app import App
from Dataclass.back.api import Api
from Dataclass.appField import ApiField
from Dataclass.fieldType import FieldType
from Dataclass.back.model import Model
from Dataclass.front.front import Front
from Dataclass.front.page import Page

def parse_models(root):
    """Parses models from the XML root."""
    models = []
    for model_elem in root.findall("model"):
        model_name = model_elem.attrib["name"]
        model = Model(model_name)
        model.fields = parse_fields(model_elem)
        models.append(model)
    return models

def parse_fields(model_elem):
    """Parses fields from a model element."""
    fields = []
    for field_elem in model_elem.findall("field"):
        field_name = field_elem.attrib["name"]
        field_type = FieldType[field_elem.attrib["type"].upper()]
        is_nullable = field_elem.attrib.get("nullable", "false").lower() == "true"
        is_primary_key = field_elem.attrib.get("primary", "false").lower() == "true"
        is_unique = field_elem.attrib.get("unique", "false").lower() == "true"
        default_value = field_elem.attrib.get("default")
        fields.append(ApiField(field_name, field_type, is_nullable, is_primary_key, is_unique, default_value))
    return fields

def parse_pages(root):
    """Parses pages from the XML root."""
    pages = []
    for page_elem in root.findall("page"):
        page_name = page_elem.attrib["name"]
        pages.append(Page(page_name))
    return pages

def parse_xml_to_app(xml_string):
    """
    Parse un code XML pour générer une application avec une API et un composant front.

    :param xml_string: Code XML sous forme de chaîne
    :return: Une instance d'Api et de Front
    """
    root = ET.fromstring(xml_string)

    api_elem = root.find("api")
    front_elem = root.find("front")

    api = Api(api_elem.attrib.get("name", "GeneratedApi"))
    api.models = parse_models(api_elem)

    front = Front(front_elem.attrib.get("name", "GeneratedFront"))
    front.pages = parse_pages(front_elem)

    app = App(root.attrib.get("name", "GeneratedApp"), api, front)

    return app
