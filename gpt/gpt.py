import os
import json
from gpt.ask import poser_question
from openai import OpenAI
from dotenv import load_dotenv
from templates.template import load_template_from_file

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

# Fonction pour appeler l'API OpenAI avec ou sans function calling
def call_openai(messages, model="gpt-4o", tools=None):
    """
    Appelle l'API OpenAI pour une conversation ou un function calling.

    :param messages: Liste des messages pour le modèle.
    :param model: Nom du modèle à utiliser (par défaut "gpt-4o").
    :param tools: Liste des outils ou None si pas de function calling.
    :return: Réponse textuelle ou résultats du function calling sous forme d'objet JSON.
    """
    try:
        # Créer un client OpenAI
        client = OpenAI()
        client.api_key = os.getenv("OPENAI_API_KEY") # Récupérer la clé API à partir des variables d'environnement

        # Préparer les outils (vide si None)
        tools = tools or []

        # Appeler l'API OpenAI
        completion = client.chat.completions.create(
            model=model,
            messages=messages,
            tools=tools
        )

        # print(completion.choices[0])

        return completion.choices[0].message

    except Exception as e:
        print(f"Une erreur est survenue : {e}")
        return None


# Fonction pour sauvegarder les fichiers générés dans le dossier de destination
def save_generated_file(destination_dir, file_name, content):
    # Assurez-vous que le répertoire de destination existe
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    
    # Créer le chemin complet du fichier
    file_path = os.path.join(destination_dir, file_name)

    # Sauvegarder le fichier
    with open(file_path, "w") as file:
        file.write(content)
    print(f"Fichier '{file_name}' généré et sauvegardé dans '{destination_dir}'.")

    return destination_dir

def create_file(path, messages, name=None, model="gpt-4"):
    """
    Crée un fichier en générant son contenu à l'aide d'une fonction OpenAI.

    :param path: Chemin du répertoire où le fichier sera sauvegardé.
    :param messages: Liste des messages pour le modèle.
    :param name: Nom optionnel du fichier (généré si None).
    :param model: Nom du modèle à utiliser (par défaut "gpt-4").
    """
    try:
        is_created = False

        # Charger la fonction de création de fichier depuis un template
        template_path = os.path.join("templates", "gpt", "create_file_function.json")
        template = str(load_template_from_file(template_path))
        function_data = json.loads(template)

        # Préparer les outils pour l'appel OpenAI
        tools = [function_data]

        # Appeler OpenAI pour générer les arguments du fichier
        message = call_openai(messages, model=model, tools=tools)

        # Retourner les appels d'outils si présents
        tool_calls = message.tool_calls
        if tool_calls:
            args = eval(tool_calls[0].function.arguments)

            # Sauvegarder le contenu généré dans le fichier
            save_generated_file(path, name, args.get("content"))

            is_created = True

        return is_created, message.content

    except Exception as e:
        print(f"Erreur lors de la création du fichier : {e}")


def create_graphql_schema(path = os.getcwd(), model = "gpt-4"):

    sys_prompt_path = os.path.join("templates", "gpt", "create_schema_sys_prompt.jinja")
    system = load_template_from_file(sys_prompt_path)

    new_message = "Veuillez décrire votre application : (objets métiers et leurs interactions)"

    # Construire le message de base
    messages = [
        {"role": "system", "content": system},
    ]

    is_created = False

    while not is_created :
        messages.append({"role": "assistant", "content": new_message})
        prompt = poser_question(new_message, default_value=None)
        messages.append({"role": "user", "content": prompt})

        is_created, new_message = create_file(path, messages, name = "schema.graphql", model = model)

    if new_message : print(new_message)