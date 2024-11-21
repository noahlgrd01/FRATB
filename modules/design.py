from colorama import Fore

def afficherLogo():
    """
    La procédure affiche le drapeau français dans le terminal
    """
    schema = "###############"
    for i in range(15):
        print(Fore.BLUE + schema + Fore.WHITE + schema + Fore.RED + schema + Fore.RESET)

def separateur():
    """
    La procédure affiche une ligne afin de séparer l'affichage dans le terminal
    """
    print("\n" + Fore.GREEN + "---------------------------------------------" + Fore.RESET + "\n")

def texteRouge(texte : str):
    """
    La fonction renvoie un texte de couleur rouge
    """
    return Fore.RED + texte + Fore.RESET

def texteVert(texte : str):
    """
    La fonction renvoie un texte de couleur verte
    """
    return Fore.GREEN + texte + Fore.RESET

def texteBleu(texte : str):
    """
    La fonction renvoie un texte de couleur bleue
    """
    return Fore.BLUE + texte + Fore.RESET

def texteJaune(texte : str):
    """
    La fonction renvoie un texte de couleur jaune
    """
    return Fore.YELLOW + texte + Fore.RESET

def texteMagenta(texte : str):
    """
    La fonction renvoie un texte de couleur magenta (rose)
    """
    return Fore.MAGENTA + texte + Fore.RESET

def texteCyan(texte : str):
    """
    La fonction renvoie un texte de couleur cyan (bleu clair)
    """
    return Fore.CYAN + texte + Fore.RESET

def texteBlanc(texte : str):
    """
    La fonction renvoie un texte de couleur blanc
    """
    return Fore.WHITE + texte + Fore.RESET