import sys
import time
import psutil
import threading
import platform
from notification import start_monitoring, stop_monitoring, set_monitoring_interval, set_alert_sound

def display_help():
    """
    Affiche l'aide pour la ligne de commande.
    """
    print("Commande de surveillance des processus")
    print("Options disponibles:")
    print("--start          Démarrer la surveillance des processus.")
    print("--stop           Arrêter la surveillance des processus.")
    print("--interval <sec> Définir l'intervalle de surveillance en secondes.")
    print("--sound <sound>  Définir le son des notifications. Options: [Par défaut, Critique, Rappel].")
    print("--help           Afficher cette aide.")

def check_os():
    """
    Vérifie le système d'exploitation et adapte le comportement en fonction de Windows ou Linux.
    """
    current_os = platform.system()
    if current_os == 'Windows':
        print("Système Windows détecté.")
        # je vais ajouter des commandes spécifiques à Windows ici si nécessaire, au besoin
    elif current_os == 'Linux':
        print("Système Linux détecté.")
        # je vais ajouter des commandes spécifiques à Linux ici si nécessaire, au besoin
    else:
        print(f"Système {current_os} détecté. Certaines fonctionnalités peuvent ne pas être disponibles.")

def process_commands():
    """
    Traite les commandes passées en ligne de commande.
    """
    if len(sys.argv) < 2:
        print("Erreur: Aucune commande spécifiée.")
        display_help()
        return

    command = sys.argv[1]

    if command == "--start":
        print("Démarrage de la surveillance des processus...")
        start_monitoring()
    elif command == "--stop":
        print("Arrêt de la surveillance des processus...")
        stop_monitoring()
    elif command == "--interval":
        if len(sys.argv) > 2:
            try:
                interval = int(sys.argv[2])
                set_monitoring_interval(interval)
            except ValueError:
                print("Erreur: L'intervalle doit être un nombre entier.")
        else:
            print("Erreur: Veuillez spécifier l'intervalle de surveillance.")
    elif command == "--sound":
        if len(sys.argv) > 2:
            sound_choice = sys.argv[2]
            if sound_choice in ["Par défaut", "Critique", "Rappel"]:
                set_alert_sound(sound_choice)
            else:
                print("Erreur: Le son spécifié n'est pas valide. Options possibles: [Par défaut, Critique, Rappel].")
        else:
            print("Erreur: Veuillez spécifier le son des notifications.")
    elif command == "--help":
        display_help()
    else:
        print("Commande inconnue.")
        display_help()

if __name__ == "__main__":
    check_os()
    process_commands()
