#!/usr/bin/env python3

import sys
import time
from modules.Ports import Ports
from modules.design import afficherLogo, texteRouge, texteVert, texteBleu, texteJaune, texteBlanc, texteMagenta, separateur
from modules.system import effacerTerminal

def help():
    effacerTerminal()
    print("Ensemble des commandes : \n\n")

def main():
    effacerTerminal()
    afficherLogo()
    separateur()
    print(texteJaune("[*]   Choisissez un script\n"))
    print(texteMagenta("[1] - Checkeur de Ports\n[2] - Rubber Ducky\n"))
    choix = str(input(">> "))
    if choix ==  "1":
        del choix
        effacerTerminal()
        print(texteMagenta("[*]   Type\n\n[1] - Machine\n[2] - Cible\n"))
        choix = str(input(">> "))
        if choix == "1":
            del choix
            effacerTerminal()
            ports = Ports('127.0.0.1')
            ports.checkFamousPorts()
            print("\nQ - Quitter\nM - Menu")
            choix = str(input(">> "))
            if choix.upper() == "M":
                main()
        elif choix == "2":
            del choix
            effacerTerminal()
            choix = str(input("[*] Entrez l'IP cible\n\n>> "))
            ports = Ports(choix)
            effacerTerminal()
            ports.checkFamousPorts()
            del choix
            print("\nQ - Quitter\nM - Menu")
            choix = str(input(">> "))
            if choix.upper() == "M":
                main()
    elif choix == "2":
        del choix
        effacerTerminal()
        print(texteMagenta("[*]   Type\n\n[1] - Lister répertoires machines\n[2] - BLABLABLA\n"))
        choix = str(input(">> "))
        if choix ==  "1":
            del choix
            effacerTerminal()
    else:
        del choix
        effacerTerminal()
        print("Choix impossible !")
        time.sleep(0.75)
        main()

if len(sys.argv) > 1 and sys.argv[1] in ["-help", "--help", "-h", "--h"]:
    help()
elif len(sys.argv) > 1 and sys.argv[1] == "-c":
    main()