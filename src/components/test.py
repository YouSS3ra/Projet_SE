import os
import subprocess
import customtkinter as ctk
from tkinter import messagebox


def create_command_page(parent):
    """
    Crée la page des commandes avec un design moderne et stylisé.
    """
    # Cadre principal pour la page des commandes
    command_frame = ctk.CTkFrame(parent, fg_color="#1E1E2E")

    # Titre de la page
    title = ctk.CTkLabel(
        command_frame,
        text="Page des Commandes",
        font=("Forte", 30,'bold'),
        text_color="#FFFFFF"
    )
    title.pack(pady=(20, 10))

    # Description
    description = ctk.CTkLabel(
        command_frame,
        text="Voici les commandes disponibles :",
        font=("Forte", 16),
        text_color="#A9A9A9"
    )
    description.pack(pady=(0, 20))

    # Simulation de l'exécution des commandes
    def execute_command(command, title):
        """
        Crée une fenêtre pop-up moderne pour afficher les résultats des commandes,
        en incluant la commande concernée.
        """
        popup = ctk.CTkToplevel(parent)
        popup.title(title)
        popup.geometry("500x350")
        popup.transient(parent)
        popup.resizable(False, False)
        popup.configure(fg_color="#1E1E2E", border_width=2, border_color="#5A5A8C")
        popup.focus_force()

        # Titre de la fenêtre
        popup_title = ctk.CTkLabel(
            popup,
            text=title,
            font=("Forte", 20, "bold"),
            text_color="#FFFFFF",
            fg_color="#2E2E4E",
            corner_radius=8,
            height=50,
            width=480,
            anchor="center"
        )
        popup_title.pack(pady=(10, 5), padx=10)

        # Affichage de la commande concernée
        command_label = ctk.CTkLabel(
            popup,
            text=f"Commande exécutée : {command}",
            font=("Forte", 14),
            text_color="#FFD700",
            wraplength=460,
            justify="center"
        )
        command_label.pack(pady=(10, 5))

        # Corps de la fenêtre
        body_frame = ctk.CTkFrame(
            popup,
            fg_color="#2E2E4E",
            border_color="#6A6AFF",
            border_width=2,
            corner_radius=10,
            width=460,
            height=180
        )
        body_frame.pack(pady=10, padx=20, fill="both", expand=True)

        try:
            # Exécution de la commande réelle
            if command == "--start":
                # Commencer une tâche de surveillance (exemple)
                result = "Surveillance démarrée avec succès."
                subprocess.Popen(["gnome-terminal", "-e", "top"])  # Ouvrir un terminal avec 'top'
            elif command == "--stop":
                # Arrêter une tâche de surveillance (exemple)
                result = "Surveillance arrêtée."
                subprocess.call(["pkill", "top"])  # Arrêter le processus 'top'
            elif command == "--list-processes":
                result = "Liste des processus simulée avec succès !"
                subprocess.Popen(["gnome-terminal", "-e", "ps aux"])  # Afficher les processus en cours
            elif command == "--help":
                result = "Voici une aide détaillée sur les commandes disponibles."
            else:
                result = f"Commande '{command}' exécutée avec succès !"

            result_label = ctk.CTkLabel(
                body_frame,
                text=result,
                font=("Helvetica", 14),
                text_color="#FFFFFF",
                wraplength=400,
                anchor="center",
                justify="center"
            )
            result_label.pack(pady=10, padx=10)
        except Exception as e:
            error_label = ctk.CTkLabel(
                body_frame,
                text=f"Erreur : {e}",
                font=("Forte", 14),
                text_color="red",
                wraplength=400,
                anchor="center",
                justify="center"
            )
            error_label.pack(pady=10, padx=10)

        # Bouton Fermer
        close_button = ctk.CTkButton(
            popup,
            text="Fermer",
            font=("Helvetica", 14),
            fg_color="#CC3F3F",
            hover_color="#A32A2A",
            text_color="#FFFFFF",
            corner_radius=10,
            height=40,
            width=200,
            command=popup.destroy
        )
        close_button.pack(pady=10)

        # Animation d'apparition
        popup.attributes("-alpha", 0.0)  # Initialement transparent
        for i in range(1, 11):
            popup.update()
            popup.attributes("-alpha", i / 10)  # Graduellement opaque

    # Liste des commandes disponibles
    commands = [
        ("Démarrer la surveillance", "--start"),
        ("Arrêter la surveillance", "--stop"),
        ("Définir l'intervalle (5s)", "--interval 5"),
        ("Définir le son Critique", "--sound Critique"),
        ("Afficher les processus", "--list-processes"),
        ("Afficher l'aide", "--help"),
    ]

    # Ajout des boutons pour les commandes
    for text, command in commands:
        btn = ctk.CTkButton(
            command_frame,
            text=text,
            command=lambda c=command: execute_command(c, text),
            fg_color="#007ACC",
            hover_color="#005A99",
            text_color="#FFFFFF",
            font=("Helvetica", 14),
            corner_radius=15
        )
        btn.pack(fill="x", pady=10, padx=20)

    # Bouton pour ouvrir le terminal
    def open_cmd():
        """
        Ouvre le terminal CMD (Windows) ou par défaut (Linux).
        """
        try:
            if os.name == 'nt':  # Windows
                os.system('start cmd')
            elif os.name == 'posix':  # Linux
                subprocess.call(['gnome-terminal'])
            else:
                messagebox.showerror("Erreur", "Terminal non pris en charge sur ce système.")
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible d'ouvrir le terminal : {e}")

    cmd_button = ctk.CTkButton(
        command_frame,
        text="Ouvrir Terminal",
        command=open_cmd,
        fg_color="#28A745",
        hover_color="#218838",
        text_color="#FFFFFF",
        font=("Forte", 14),
        corner_radius=15
    )
    cmd_button.pack(pady=20, padx=20)

    return command_frame
