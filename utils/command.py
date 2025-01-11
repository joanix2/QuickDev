import subprocess

def run_command(command, cwd=None):
    """
    Exécute une commande shell et affiche la sortie.
    """
    try:
        subprocess.run(command, shell=True, check=True, cwd=cwd)
        print(f"Command succeeded: {command}")
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {command}")
        print(e)