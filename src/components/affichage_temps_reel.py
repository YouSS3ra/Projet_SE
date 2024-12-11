import customtkinter as ctk
from tkinter import ttk
import psutil
import threading
import time

def create_real_time_process_display(parent):
    # Conteneur principal
    process_frame = ctk.CTkFrame(parent, fg_color="#2b2b2b", corner_radius=10)
    process_frame.pack(fill="both", expand=True, padx=10, pady=10)

    # Table des processus
    columns = ["ID", "Nom", "CPU (%)", "RAM (%)"]
    process_table = ttk.Treeview(process_frame, columns=columns, show="headings", height=15)
    process_table.pack(fill="both", expand=True, padx=10, pady=50)

    # Style pour améliorer l'apparence
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview", background="#333333", foreground="white", fieldbackground="#333333", rowheight=25)
    style.configure("Treeview.Heading", background="#444444", foreground="white", font=("Arial", 12, "bold"))

    # Définir les colonnes
    for col in columns:
        process_table.heading(col, text=col)
        process_table.column(col, anchor="center", stretch=True)

    # Fonction pour mettre à jour les processus
    def update_process_table():
        while True:
            # Effacer l'ancien contenu
            for row in process_table.get_children():
                process_table.delete(row)

            # Récupérer les processus   "liste par compréhension"
            processes = [                                       
                (
                    proc.pid,
                    proc.info.get("name", "N/A"),
                    f"{proc.info['cpu_percent']:.1f}",
                    f"{proc.info['memory_percent']:.1f}"
                )
                for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent'])
            ]

            # Ajouter les processus à la table
            for proc in processes:
                process_table.insert("", "end", values=proc)

            time.sleep(1)

    # Thread pour la mise à jour des données
    threading.Thread(target=update_process_table, daemon=True).start()

    # Cadres CPU et RAM
    stats_frame = ctk.CTkFrame(process_frame, fg_color="#444444", corner_radius=10)
    stats_frame.pack(fill="x", pady=20)

    # CPU Frame
    cpu_frame = ctk.CTkFrame(stats_frame, width=400, height=100, fg_color="#222222", corner_radius=10)
    cpu_frame.pack(side="left", padx=20, pady=10)

    cpu_label = ctk.CTkLabel(cpu_frame, text="Consommation CPU", font=("Arial", 12, "bold"))
    cpu_label.pack(side="bottom", pady=5)

    cpu_usage_label = ctk.CTkLabel(cpu_frame, text="0%", font=("Forte", 25, "bold"), text_color="#41C8FF")
    cpu_usage_label.pack(expand=True)

    # RAM Frame
    ram_frame = ctk.CTkFrame(stats_frame, width=400, height=100, fg_color="#222222", corner_radius=10)
    ram_frame.pack(side="left", padx=20, pady=10)

    ram_label = ctk.CTkLabel(ram_frame, text="Consommation RAM", font=("Arial", 12, "bold"))
    ram_label.pack(side="bottom", pady=5)

    ram_usage_label = ctk.CTkLabel(ram_frame, text="0%", font=("Forte", 25, "bold"), text_color="#58F0F9")
    ram_usage_label.pack(expand=True)

    # Fonction pour mettre à jour les statistiques CPU/RAM
    def update_stats():
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            ram_usage = psutil.virtual_memory().percent

            cpu_usage_label.configure(text=f"{cpu_usage}%")
            ram_usage_label.configure(text=f"{ram_usage}%")

    # Thread pour la mise à jour des stats
    threading.Thread(target=update_stats, daemon=True).start()