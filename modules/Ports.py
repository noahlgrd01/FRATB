import socket
from modules.design import texteVert, texteRouge, texteJaune

class Ports:
    def __init__(self, cible):
        self.ip_cible = cible

    def checkFamousPorts(self):
        famous_ports = {
            20: "FTP (Data)",
            21: "FTP (Control)",
            22: "SSH",
            23: "Telnet",
            25: "SMTP",
            53: "DNS",
            67: "DHCP (Server)",
            68: "DHCP (Client)",
            80: "HTTP",
            110: "POP3",
            119: "NNTP",
            123: "NTP",
            143: "IMAP",
            161: "SNMP",
            162: "SNMP",
            443: "HTTPS",
            3306: "MySQL",
            5000: "Flask",
            5432: "PostgreSQL",
            5900: "VNC",
            6379: "Redis",
            8080: "HTTP (Alt.)",
        }

        print(texteVert("Vert = ouvert\n") + texteRouge("Rouge = fermé\n"))
        for port, protocol in famous_ports.items():
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((self.ip_cible, port))
            if result == 0:
                print(texteJaune("[*] ") + texteVert(f"{port} {protocol}"))
            else:
                print(texteJaune("[*] ") + texteRouge(f"{port} {protocol}"))
            sock.close()

    def everyPorts(self):
        pass

#Ne pas oublier le effacerTerminal et d'afficher une indication de couleur 
# ex : Vert = ouvert, Rouge = fermé
ports = Ports('127.0.0.1')
ports.checkFamousPorts()