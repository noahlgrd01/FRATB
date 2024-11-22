#!/usr/bin/env python3

import sys
import time
from modules.design import afficherLogo, texteRouge, texteVert, texteBleu, texteJaune, texteBlanc, texteMagenta, separateur
from modules.system import effacerTerminal

def help():
    effacerTerminal()
    print("Ensemble des commandes : \n\n")

def main():
    effacerTerminal()
    afficherLogo()
    separateur()
    print(texteMagenta("[*]   Choisissez un script\n\n[1] - Checkeur de Ports (machine)\n[2] - Checkeur de Ports (cible)\n"))
    choix = str(input(">> "))
    if choix ==  "1":
        pass
    elif choix == "2":
        pass
    else:
        effacerTerminal()
        print("Choix impossible !")
        time.sleep(0.75)
        main()

if len(sys.argv) > 1 and sys.argv[1] in ["-help", "--help", "-h", "--h"]:
    help()
elif len(sys.argv) > 1 and sys.argv[1] == "-c":
    main()