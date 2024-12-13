import os
import json
import openai
from dotenv import load_dotenv

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

# Récupérer la clé API à partir des variables d'environnement
openai_api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = openai_api_key

# Fonction pour appeler l'API OpenAI avec ou sans function calling
def call_openai(messages, model = "gpt-4", functions = None, function_call = None):
    try:
        # Appeler l'API pour une completion classique
        completion = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            functions = functions,
            function_call = function_call
        )

        if len(functions) == 0 or functions == None :
            # Retourner la réponse simple
            return completion.choices[0].message['content']
        else :
            # Récupérer les arguments de la fonction appelée (nom du fichier et contenu)
            response_message = completion.choices[0].message['function_call']['arguments']
            return json.loads(response_message)

    except Exception as e:
        print(f"Une erreur est survenue : {e}")
        return None


# Fonction pour sauvegarder les fichiers générés dans le dossier de destination
def save_generated_file(file_name, content, destination_dir):
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


def create_file(path, messages, name = None, model = "gpt-4"):

    functions=[{
        "name": "create_file",
        "description": "Generate multiple files with names and content based on the user's request.",
        "parameters": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "file_name": {"type": "string"},
                    "content": {"type": "string"}
                },
                "required": ["file_name", "content"]
            }
        }
    }],
    function_call={"name": "create_file", "arguments": json.dumps(function_args)}
                
    file_args = call_openai(messages, model = model, functions = functions, function_call = function_call)
    file_name = name if name != None else file_args['file_name']
    save_generated_file(file_name, file_args['content'], path)


def create_graphql_schema(prompt, path = os.getcwd(), model = "gpt-4"):
    # Construire le message de base
    messages = [
        {"role": "system", "content": system},
        {"role": "user", "content": prompt}
    ]

    create_file(path, messages, name = "schema.graphql", model = model)