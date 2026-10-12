import subprocess

def afficher_config_ip():
    resultat = subprocess.run(
    ["ipconfig", "/all"],
    capture_output=True, text=True,
    encoding="cp850", errors="replace"
    )
    print(resultat.stdout)


def afficher_wifi():
    print("J'ai pas de wifi disponible sur ce pc je fais comment pour développer cette fonctionnalité je suis pas Chuck Norris")

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

while True :
    print("1 - Configuration IP")
    print("2 - Réseaux Wi-fi visibles")
    print("3 - Tester le ping -- ip nécessaire --")
    print("0 - Quitter")
    choix = input("Votre choix : ")

    if choix == "1":
        afficher_config_ip()
    elif choix == "2":
        afficher_wifi()
    elif choix == "3":
        tester_ping()
    elif choix == "0":
        break
    else:
        print("Veuillez entrer un nombre valable")