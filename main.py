#!/usr/bin/env python3

from modules.design import afficherLogo, texteRouge, texteVert, texteBleu, texteJaune
from modules.system import effacerTerminal
import time

def main():
    effacerTerminal()
    afficherLogo()
    print("\n\n\n")
    choix = str(input("[*] Choisissez un script\n1 - Checkeur de Ports (machine)\n2 - Checkeur de Ports (cible)\n>> "))
    if choix ==  "1":
        pass
    else:
        effacerTerminal()
        print("Choix impossible !")
        time.sleep(0.75)
        main()

main()