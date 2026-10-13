import subprocess
import socket
import ipaddress

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
    try :
        port = int(input("Port TCP : "))
    except ValueError:
        print("\n Entrez un format de port valide. (Nombre entier) \n")
        return
    try:
        with socket.create_connection((hote, port), timeout=2):
           print("Connexion TCP établie")
    except OSError as erreur:
        print("Connexion impossible :", erreur, ", veuillez vérifier que l'adresse et le port correspondent.")

def calcul_reseau() :
    
    try:
        adresse = input("Adresse IPv4 : ").strip()
        masque = input("Masque ou préfixe : ").strip()
        reseau = ipaddress.IPv4Network(adresse + "/" + masque, strict=False)
        print("\n --- Informations réseau ---")
        print("Réseau :", reseau.network_address)
        print("Préfixe :", reseau.prefixlen)
        print("Diffusion :", reseau.broadcast_address)
    
    except (
        ValueError,
        ipaddress.AddressValueError,
        ipaddress.NetmaskValueError,
    ):
        print(
            "\n[Erreur] L'adresse IP ou le masque saisi est invalide. Veuillez"
            " recommencer.\n"
      )


def calculatrice() :
    try:
        choix_operation = input("Quelle opération voulez vous effectuer ? (+ - * /) :")
        if choix_operation == "+":
            nb_add_1 = float(input("\n Entrez le premier nombre de l'addition : "))
            nb_add_2 = float(input("\n Entrez le deuxième nombre de l'addition : "))
            result_addition = nb_add_1 + nb_add_2
            print("Le résultat de l'addition est : ", result_addition)

        elif choix_operation == "-":
            nb_sous_1 = float(input("\n Entrez le premier nombre de la soustraction : "))
            nb_sous_2 = float(input("\n Entrez le deuxième nombre de la soustraction : "))
            result_soustraction = nb_sous_1 - nb_sous_2
            print("\n Le résultat de cette soustraction est : ", result_soustraction, "\n")

        elif choix_operation == "/":
            nb_div_1 = float(input("\n Entrez le premier nombre de la division : "))
            nb_div_2 = float(input("\n Entrez le deuxième nombre de la division : "))
            result_div = nb_div_1 / nb_div_2
            print("\n Le résultat de cette soustraction est : ", result_div, "\n")

        elif choix_operation == "*":
            nb_mult_1 = float(input("\n Entrez le premier nombre de la multiplication : "))
            nb_mult_2 = float(input("\n Entrez le deuxième nombre de la multiplication : "))
            result_mult = nb_mult_1 * nb_mult_2
            print("\n Le résultat de cette soustraction est : ", result_mult, "\n")

    except (
        ValueError,

    ):
        print("\n [Erreur] Entrez des nombres valables. \n"
        )

while True :
    print("1 - Configuration IP")
    print("2 - Réseaux Wi-fi visibles")
    print("3 - Tester le ping -- ip nécessaire --")
    print("4 - Résoudre nom de domaine")
    print("5 - Tester le service TCP")
    print("6 - Calculer les informations d'un réseau IPv4")
    print("7 - Calculatrice primaire")
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
    elif choix == "6":
        calcul_reseau()
    elif choix == "7":
        calculatrice()
    elif choix == "0":
        break
    else:
        print("Veuillez entrer un nombre valable")