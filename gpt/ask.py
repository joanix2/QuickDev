def poser_question(question, default_value=None):
    reponse = None
    # Boucle tant qu'il n'y a pas de réponse valide ou si la réponse est vide
    while not reponse or reponse.strip() == "":
        if default_value is not None:
            reponse = input(f"{question} [par défaut : {default_value}] : ").strip()
            # Utiliser la valeur par défaut si l'utilisateur ne fournit pas de réponse
            reponse = reponse if reponse else default_value
        else:
            reponse = input(question + "\n> ").strip()
    return reponse