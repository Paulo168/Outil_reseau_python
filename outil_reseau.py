import subprocess
import socket
def afficher_config_ip():
    resultat = subprocess.run(
    ["ipconfig", "/all"],
    capture_output=True, text=True,
    encoding="cp850", errors="replace"
    )
    print(resultat.stdout)


def afficher_wifi():
    resultat = subprocess.run(
        ["netsh", "wlan", "show", "networks", "mode=bssid"],
        capture_output=True, text=True,
        encoding="cp850", errors="replace"
    )
    if resultat.returncode != 0:
        print("Carte réseau désactivée ou non existante.")
    else:
        print(resultat.stdout)


def tester_ping():
    adresse = input("Adresse IP ou nom : ").strip()
    if not adresse:
        print("Adresse vide")
        return
    resultat = subprocess.run(
        ["ping", "-n", "1", "-w", "1500", adresse],
        capture_output=True, text=True,
        encoding="cp850", errors="replace"
    )
    print(resultat.stdout)

def resoudre_nom():
    nom = input("Nom de domaine : ").strip()
    resultats = socket.getaddrinfo(nom, None)
    for ligne in resultats:
        print(ligne[4][0])
    try:
        resultats = socket.getaddrinfo(nom, None)
    except socket.gaierror as erreur:
        print("Résolution impossible :", erreur)
    return

def test_tcp() :
    hote = input("Hôte : ").strip()
    port = int(input("Port TCP : "))
    try:
        with socket.create_connection((hote, port), timeout=2):
            print("Connexion TCP établie")
    except OSError as erreur:
        print("Connexion impossible :", erreur)

while True :
    print("1 - Configuration IP")
    print("2 - Réseaux Wi-fi visibles")
    print("3 - Tester le ping -- ip nécessaire --")
    print("4 - Résoudre nom de domaine")
    print("5 - Tester le service TCP")
    print("0 - Quitter")
    choix = input("Votre choix : ")

    if choix == "1":
        afficher_config_ip()
    elif choix == "2":
        afficher_wifi()
    elif choix == "3":
        tester_ping()
    elif choix == "4":
        resoudre_nom()
    elif choix == "5":
        test_tcp()
    elif choix == "0":
        break
    else:
        print("Veuillez entrer un nombre valable")