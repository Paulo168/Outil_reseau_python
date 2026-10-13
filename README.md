# Outil Réseau Python

## Introduction

Ce programme possède plusieurs outils qui permettent d'effectuer des tests réseaux que je vais détailler.

## Fonctionnement

Lors du lancement du programme, nous devons saisir le numéro (faire attention à ne bien saisir QUE le numéro de la fonction que l'on veut lancer) de la foncion que nous devons exécuter :

### 1 - Configuration IP

Cette fonction sert à afficher toutes les cartes réseaux de l'ordinateur, physiques comme virtuelles. Ceci contient exactement les mêmes informations qu'un ipconfig sur windows ou un ip a sur linux.

![alt text](https://github.com/Paulo168/Outil_reseau_python/blob/main/Images/Config_IP.png "Config_IP")

### 2 - Réseaux Wifi disponnibles 

Cette fonction scanne le wlan et nous rapporte les réseaux wi-fi à proximité, et nous dit même si on a pas de carte réseau au lieu de renvoyer une erreur illisible.

![alt text](https://github.com/Paulo168/Outil_reseau_python/blob/main/Images/Réseau_Wifi.png "Scan de la carte réseau Wlan")

### 3 - Test du ping

Cette fonction est simple mais très importante : il suffit d'entrer l'adresse ip de la machine ou du serveur que l'on veut ping afin d'effectuer un ping. Si besoin on peut modifier dans le code le nombre de pings effectués.

![alt text](https://github.com/Paulo168/Outil_reseau_python/blob/main/Images/Ping.png "Ping")

### 4 - Résoudre nom de domaine

Cette fonction permet de traduire un nom de domaine en adresse IP.

![alt text](https://github.com/Paulo168/Outil_reseau_python/blob/main/Images/Traduction_nom_de_domaine.png "Traduction nom de domaine")

### 5 - Test TCP

Cette fonction permet d'effectuer des tests TCP, tout d'abord en prenant l'IP de l'appareil auquel on veut envoyer une requête puis en prenant le code TCP (ex : port 22 pour le SSH ou port 80 pour le port http).

![alt text](https://github.com/Paulo168/Outil_reseau_python/blob/main/Images/Test_TCP_concluant.png "Test TCP concluant")

![alt text](https://github.com/Paulo168/Outil_reseau_python/blob/main/Images/Test_TCP_non_concluant.png "Test TCP non concluant")

### 6 - Calcul Réseau

Cet outil sert, à partir d'une adresse IP et d'un masque de sous-réseau, à calculer les informations du réseau, du préfixe et de l'adresse de diffusion de cette IP.

![alt text](https://github.com/Paulo168/Outil_reseau_python/blob/main/Images/Calcul_infos_reseau.png "Calcul Réseau")

### 7 - Calculatrice

Cet outil est une calculatrice capable d'effectuer des opérations simples comme la division, l'addition, la multiplication et la soustraction.

![alt text](https://github.com/Paulo168/Outil_reseau_python/blob/main/Images/Exemple_calculatrice.png "Exemple d'utilisation de la calculatrice")

### 8 - Traceroute

L'outil traceroute permet de déterminer le chemin de routeurs que l'on emprunte.

![alt text](https://github.com/Paulo168/Outil_reseau_python/blob/main/Images/Exemple_traceroute.png "Exemple de traceroute")

## Conseils d'utilisation

Faites bien attention à rentrer les bons formats comme l'adresse IP en format 255.255.255.255 ou encore les noms de domaines, les erreurs peuvent venir de domaines mal orthographiés.