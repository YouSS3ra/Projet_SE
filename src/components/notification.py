import time
import psutil
from winotify import Notification, audio
import threading
import tkinter.messagebox as messagebox
import customtkinter as ctk
from tkinter import PhotoImage  # Utiliser PhotoImage de tkinter

# Seuils de surveillance
INACTIVE_THRESHOLD = 300  # Temps d'inactivité en secondes (5 minutes)
CPU_USAGE_THRESHOLD = 5  # Pourcentage d'utilisation CPU
MEMORY_USAGE_THRESHOLD = 50  # Mémoire utilisée en Mo

# Variables globales
is_monitoring = False
MONITORING_INTERVAL = 10  # Intervalle par défaut en secondes
ALERT_SOUND = audio.Default  # Son d'alerte par défaut

def notify_user(process_name, pid):
    """
    Envoie une notification système pour un processus inactif avec un son personnalisé.
    """
    try:
        toast = Notification(
            app_id="Surveillance Processus",
            title="Alerte : Processus Inactif",
            msg=f"Le processus '{process_name}' (PID: {pid}) est inactif et consomme des ressources.",
            duration="long"
        )
        toast.set_audio(ALERT_SOUND, loop=False)
        toast.show()
    except Exception as e:
        print(f"Erreur lors de l'envoi de la notification pour le processus {pid}: {e}")

def stop_process(pid):
    """
    Tente d'arrêter le processus donné.
    """
    try:
        process = psutil.Process(pid)
        if process.username() != "root":  # Vérification pour éviter les processus système critiques
            process.terminate()
            print(f"Processus {pid} arrêté avec succès.")
        else:
            print(f"Impossible d'arrêter le processus {pid} (droits root nécessaires).")
    except psutil.NoSuchProcess:
        print(f"Processus {pid} introuvable.")
    except Exception as e:
        print(f"Erreur lors de l'arrêt du processus {pid} : {e}")

def monitor_processes():
    """
    Surveille les processus actifs pour identifier ceux qui sont inactifs.
    """
    global is_monitoring
    print("Démarrage de la surveillance des processus...")
    while is_monitoring:
        for process in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info', 'create_time']):
            try:
                # Récupération des informations du processus
                pid = process.info['pid']
                name = process.info['name']
                cpu_percent = process.info['cpu_percent']
                memory_used = process.info['memory_info'].rss / (1024 * 1024)  # Convertir en Mo
                create_time = process.info['create_time']

                # Temps depuis la création du processus
                elapsed_time = time.time() - create_time

                # Vérification des critères d'inactivité
                if elapsed_time > INACTIVE_THRESHOLD and cpu_percent < CPU_USAGE_THRESHOLD and memory_used > MEMORY_USAGE_THRESHOLD:
                    print(f"Processus '{name}' (PID: {pid}) identifié comme inactif.")
                    notify_user(name, pid)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

        # Pause entre les cycles de surveillance
        time.sleep(MONITORING_INTERVAL)

    print("Surveillance arrêtée.")

def set_monitoring_interval(interval):
    """
    Change l'intervalle de surveillance.
    """
    global MONITORING_INTERVAL
    try:
        MONITORING_INTERVAL = max(1, int(interval))  # Minimum 1 seconde
        print(f"Intervalle de surveillance mis à jour à {MONITORING_INTERVAL} secondes.")
    except ValueError:
        print("Erreur : Intervalle invalide. Veuillez entrer un nombre entier.")

def set_alert_sound(sound_choice):
    """
    Change le son des notifications en fonction du choix.
    """
    global ALERT_SOUND
    if sound_choice == "Par défaut":
        ALERT_SOUND = audio.Default
    elif sound_choice == "Critique":
        ALERT_SOUND = audio.Critical
    elif sound_choice == "Rappel":
        ALERT_SOUND = audio.Reminder
    else:
        print("Choix de son invalide. Son par défaut sélectionné.")
        ALERT_SOUND = audio.Default
    print(f"Son de notification mis à jour à {ALERT_SOUND}.")

def start_monitoring():
    """
    Démarre la surveillance dans un thread séparé.
    """
    global is_monitoring
    if not is_monitoring:
        is_monitoring = True
        monitoring_thread = threading.Thread(target=monitor_processes, daemon=True)
        monitoring_thread.start()
        messagebox.showinfo("Surveillance", "La surveillance des processus a démarré.")
    else:
        messagebox.showinfo("Surveillance", "La surveillance est déjà en cours.")

def stop_monitoring():
    """
    Arrête la surveillance.
    """
    global is_monitoring
    if is_monitoring:
        is_monitoring = False
        messagebox.showinfo("Surveillance", "La surveillance des processus a été arrêtée.")
    else:
        messagebox.showinfo("Surveillance", "La surveillance n'est pas en cours.")


import platform
import subprocess

def notify_user(process_name, pid):
    os_name = platform.system()
    message = f"Le processus '{process_name}' (PID: {pid}) est inactif et consomme des ressources."
    if os_name == "Windows":
        # Windows : utiliser winotify
        try:
            toast = Notification(
                app_id="Surveillance Processus",
                title="Alerte : Processus Inactif",
                msg=message,
                duration="long"
            )
            toast.set_audio(ALERT_SOUND, loop=False)
            toast.show()
        except Exception as e:
            print(f"Erreur de notification sur Windows : {e}")
    elif os_name == "Linux":
        # Linux : utiliser notify-send
        try:
            subprocess.run(["notify-send", "Alerte : Processus Inactif", message])
        except Exception as e:
            print(f"Erreur de notification sur Linux : {e}")
    else:
        print("Système non supporté pour les notifications.")

def stop_process(pid):
    try:
        process = psutil.Process(pid)
        if process.username() != "root":  # Vérification pour éviter les processus système critiques
            process.terminate()
            print(f"Processus {pid} arrêté avec succès.")
        else:
            print(f"Impossible d'arrêter le processus {pid} (droits root nécessaires).")
    except psutil.NoSuchProcess:
        print(f"Processus {pid} introuvable.")
    except Exception as e:
        print(f"Erreur lors de l'arrêt du processus {pid} : {e}")

def monitor_processes():
    global is_monitoring
    print("Démarrage de la surveillance des processus...")
    while is_monitoring:
        for process in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info', 'create_time']):
            try:
                pid = process.info['pid']
                name = process.info['name']
                cpu_percent = process.info['cpu_percent']
                memory_used = process.info['memory_info'].rss / (1024 * 1024)  # Convertir en Mo
                create_time = process.info['create_time']
                elapsed_time = time.time() - create_time

                if elapsed_time > INACTIVE_THRESHOLD and cpu_percent < CPU_USAGE_THRESHOLD and memory_used > MEMORY_USAGE_THRESHOLD:
                    print(f"Processus '{name}' (PID: {pid}) identifié comme inactif.")
                    notify_user(name, pid)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        time.sleep(MONITORING_INTERVAL)
    print("Surveillance arrêtée.")

def set_monitoring_interval(interval):
    global MONITORING_INTERVAL
    try:
        MONITORING_INTERVAL = max(1, int(interval))  # Minimum 1 seconde
        print(f"Intervalle de surveillance mis à jour à {MONITORING_INTERVAL} secondes.")
    except ValueError:
        print("Erreur : Intervalle invalide. Veuillez entrer un nombre entier.")

def set_alert_sound(sound_choice):
    global ALERT_SOUND
    if sound_choice == "Par défaut":
        ALERT_SOUND = audio.Default
    elif sound_choice == "Critique":
        ALERT_SOUND = audio.Critical
    elif sound_choice == "Rappel":
        ALERT_SOUND = audio.Reminder
    else:
        print("Choix de son invalide. Son par défaut sélectionné.")
        ALERT_SOUND = audio.Default
    print(f"Son de notification mis à jour à {ALERT_SOUND}.")

def start_monitoring():
    global is_monitoring
    if not is_monitoring:
        is_monitoring = True
        monitoring_thread = threading.Thread(target=monitor_processes, daemon=True)
        monitoring_thread.start()
        messagebox.showinfo("Surveillance", "La surveillance des processus a démarré.")
    else:
        messagebox.showinfo("Surveillance", "La surveillance est déjà en cours.")

def stop_monitoring():
    global is_monitoring
    if is_monitoring:
        is_monitoring = False
        messagebox.showinfo("Surveillance", "La surveillance des processus a été arrêtée.")
    else:
        messagebox.showinfo("Surveillance", "La surveillance n'est pas en cours.")

def create_notification_page(parent_frame):
    # Page principale
    notification_frame = ctk.CTkFrame(parent_frame, corner_radius=15, fg_color="#1C1C1C", width=600, height=450)

    # Titre de la page
    title_label = ctk.CTkLabel(
        notification_frame,
        text="Gestion des Notifications",
        font=("Forte", 36, "bold"),
        text_color="#ECF0F1"
    )
    title_label.grid(row=0, column=0, columnspan=2, pady=(20, 10))

    # Frame centrale
    central_frame = ctk.CTkFrame(notification_frame, fg_color="#2B2B2B")
    central_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

    # Boutons et champs dans le central_frame
    start_button = ctk.CTkButton(central_frame, text="Démarrer la Surveillance", command=start_monitoring, fg_color="#387F39")
    start_button.grid(row=0, column=0, padx=15, pady=10)

    stop_button = ctk.CTkButton(central_frame, text="Arrêter la Surveillance", command=stop_monitoring, fg_color="#AF1740")
    stop_button.grid(row=0, column=1, padx=15, pady=10)

    interval_label = ctk.CTkLabel(central_frame, text="Intervalle de Surveillance:", text_color="white")
    interval_label.grid(row=1, column=0, padx=10, pady=5)

    interval_entry = ctk.CTkEntry(central_frame, width=150)
    interval_entry.insert(0, "5")  # Valeur par défaut
    interval_entry.grid(row=1, column=1, padx=10, pady=5)

    sound_label = ctk.CTkLabel(central_frame, text="Son des Notifications:", text_color="white")
    sound_label.grid(row=2, column=0, padx=10, pady=5)

    sound_options = ["Par défaut", "Critique", "Rappel"]
    sound_combobox = ctk.CTkComboBox(central_frame, values=sound_options, state="readonly", width=150)
    sound_combobox.set("Par défaut")
    sound_combobox.grid(row=2, column=1, padx=10, pady=5)

    update_interval_button = ctk.CTkButton(
        central_frame,
        text="Mettre à jour l'Intervalle",
        command=lambda: set_monitoring_interval(interval_entry.get()),
        fg_color="blue"
    )
    update_interval_button.grid(row=3, column=0, padx=10, pady=10)

    update_sound_button = ctk.CTkButton(
        central_frame,
        text="Mettre à jour le Son",
        command=lambda: set_alert_sound(sound_combobox.get()),
        fg_color="blue"
    )
    update_sound_button.grid(row=3, column=1, padx=10, pady=10)

    # Ajout de l'image dans la frame centrale
    image_path = "C:/Users/ELITEBOOK/Desktop/ProjetLinux/assets/images/micro.png"  # Chemin vers l'image
    try:
        photo = PhotoImage(file=image_path)
        image_label = ctk.CTkLabel(central_frame, image=photo, text="")
        image_label.image = photo  # Référence pour éviter le garbage collection
        image_label.grid(row=4, column=0, columnspan=2, pady=(10, 0))
    except Exception as e:
        print(f"Erreur lors du chargement de l'image : {e}")

    # Frame droite pour les remarques
    right_frame = ctk.CTkFrame(notification_frame, width=250, height=300, fg_color="#2B2B2B")
    right_frame.grid(row=1, column=1, padx=20, pady=20)

    # Titre des remarques
    remark_title = ctk.CTkLabel(
        right_frame,
        text="Remarque :",
        font=("Forte", 30, "bold"),
        text_color="#F5B041"
    )
    remark_title.pack(pady=(10, 5))

    # Liste des warnings avec valeur par défaut ajoutée
    warnings = [
        "Choisissez un **intervalle raisonnable** pour éviter une surcharge CPU.",
        "Des valeurs trop basses peuvent **ralentir** le système.",
        "Assurez-vous que les notifications sont **activées** dans votre système.",
        "Utilisez un **seuil mémoire** adapté à vos besoins.",
        "La surveillance excessive peut **affecter** les performances.",
        "Vérifiez les **droits d'administrateur** si nécessaire.",
        "**Valeur par défaut de l'intervalle** : 5 secondes (modifiable dans l'entrée)."
    ]

    for warning in warnings:
        warning_frame = ctk.CTkFrame(right_frame, fg_color="#1C1C1C", corner_radius=10)
        warning_frame.pack(pady=5, padx=10, fill="x")
        bullet_label = ctk.CTkLabel(warning_frame, text="⚠️", font=("Arial", 16), text_color="#F5B041")
        bullet_label.pack(side="left", padx=5)
        warning_label = ctk.CTkLabel(
            warning_frame,
            text=warning,
            font=("Arial", 12),
            text_color="white",
            anchor="w"
        )
        warning_label.pack(side="left", padx=5, expand=True, fill="x")

    return notification_frame
