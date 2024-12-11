import argparse
import time
from notification import set_monitoring_interval,set_alert_sound,start_monitoring,stop_monitoring

# Définir les méthodes pour chaque fonctionnalité
"""def start_monitoring():
    print("Démarrage de la surveillance...")

def stop_monitoring():
    print("Arrêt de la surveillance...")

def set_interval(interval):
    print(f"Intervalle défini sur {interval} secondes.")
    return interval

def play_sound(sound):
    print(f"Lecture du son : {sound}")
"""
def main():
    # Configuration de l'analyseur d'arguments
    parser = argparse.ArgumentParser(description="Outil de surveillance des performances")     #return objet
    
    # Ajouter les arguments de ligne de commande
    parser.add_argument('--start', action='store_true', help="Démarrer la surveillance")
    parser.add_argument('--stop', action='store_true', help="Arrêter la surveillance")
    parser.add_argument('--interval', type=int, help="Définir l'intervalle de surveillance en secondes")
    parser.add_argument('--sound', type=str, help="Définir le son à jouer")
    
    
    # Analyser les arguments de la ligne de commande
    args = parser.parse_args()       # analyse les arguments de la ligne de commande fournis par l'utilisateur.
    
    # Appeler les méthodes en fonction des arguments fournis
    if args.start:
        start_monitoring()
    
    if args.stop:
        stop_monitoring()
    
    if args.interval:
        set_monitoring_interval(args.interval)
        print("Surveillance en cours...")         
    
    if args.sound:
        set_alert_sound(args.sound)

if __name__ == "__main__":            #cette partie du code sera exécutée uniquement lorsque le fichier est exécuté directement
    main()
