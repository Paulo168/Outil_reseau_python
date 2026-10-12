import subprocess

def afficher_config_ip():
    resultat = subprocess.run(
    ["ipconfig", "/all"],
    capture_output=True, text=True,
    encoding="cp850", errors="replace"
    )
    print(resultat.stdout)



while True :
    print("1 - Configuration IP")
    print("2 - Réseaux Wi-fi visibles")
    print("0 - Quitter")
    choix = input("Votre choix : ")

    if choix == "1":
        afficher_config_ip()
    elif choix == "2":
        print("Fonction pas encore développée")
    elif choix == "0":
        break
    else:
        print("Veuillez entrer un nombre valable")