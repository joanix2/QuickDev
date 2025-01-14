def init_app_xml():
    """
    Génère un fichier app.xml avec un contenu par défaut.

    :raises IOError: si une erreur d'entrée/sortie se produit lors de l'écriture
    """
    content = """<?xml version=\"1.0\" encoding=\"UTF-8\"?>
    <application>
        <name>MyApp</name>
        <version>1.0</version>
        <description>Application description here</description>
    </application>
    """
    try:
        with open("app.xml", 'w', encoding='utf-8') as file:
            file.write(content)
        print("Fichier app.xml généré avec succès.")
    except IOError as e:
        raise IOError(f"Une erreur s'est produite lors de la création du fichier app.xml : {e}")
    
def init_app():
    init_app_xml()