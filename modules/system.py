import os

def effacerTerminal():
    """
    La procédure récupère le type d'os, et exécute la commande associée pour effacer le terminal.
    """
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')