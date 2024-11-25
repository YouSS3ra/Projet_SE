import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import psutil
import threading
import time
import csv
from tkinter import PhotoImage
from tkinter.messagebox import showinfo

def create_visualisation_page(parent):
    """
    Crée une page Visualisation modernisée avec des graphiques, stats et options avancées.
    """
    visualisation_frame = ctk.CTkFrame(parent, corner_radius=15)

    # Titre de la page
    header_frame = ctk.CTkFrame(visualisation_frame, height=80, fg_color="#444444")
    header_frame.pack(fill="x", padx=10, pady=10)

    header_label = ctk.CTkLabel(
        header_frame,
        text="Visualisation Avancée",
        font=("Forte", 35, "bold"),
        text_color="white"
    )
    header_label.pack(pady=10, padx=10)

    # Section principale
    main_frame = ctk.CTkFrame(visualisation_frame, fg_color="#333333", corner_radius=15)
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Widgets modernes : Progress bars circulaires pour CPU et RAM
    progress_frame = ctk.CTkFrame(main_frame, fg_color="#2b2b2b", corner_radius=15)
    progress_frame.pack(fill="x", pady=10)

    cpu_progress = ctk.CTkProgressBar(progress_frame, orientation="vertical", width=20, height=150)
    cpu_progress.set(0)
    cpu_progress.pack(side="left", padx=20, pady=10)

    ram_progress = ctk.CTkProgressBar(progress_frame, orientation="vertical", width=20, height=150, progress_color="green")
    ram_progress.set(0)
    ram_progress.pack(side="left", padx=20, pady=10)

    cpu_label = ctk.CTkLabel(progress_frame, text="CPU Usage", font=("Arial", 14))
    cpu_label.pack(side="left", padx=10)

    ram_label = ctk.CTkLabel(progress_frame, text="RAM Usage", font=("Arial", 14))
    ram_label.pack(side="left", padx=10)

    # Ajouter une icône d'horloge pour afficher le temps de fonctionnement
    
    clock_icon = PhotoImage(file="C:/Users/ELITEBOOK/Desktop/ProjetLinux/assets/icones/clock.png")  
    clock_label = ctk.CTkLabel(progress_frame, text="00:00:00", font=("Arial", 14), image=clock_icon, compound="left", text_color="white")
    clock_label.pack(side="left", padx=20)

    # Statistiques rapides
    stats_frame = ctk.CTkFrame(main_frame, fg_color="#2b2b2b", corner_radius=15)
    stats_frame.pack(fill="x", pady=10)

    cpu_max_label = ctk.CTkLabel(stats_frame, text="Max CPU: 0%", font=("Arial", 14, "bold"))
    cpu_max_label.pack(side="left", padx=20, pady=10)

    ram_max_label = ctk.CTkLabel(stats_frame, text="Max RAM: 0%", font=("Arial", 14, "bold"))
    ram_max_label.pack(side="left", padx=20, pady=10)

    process_count_label = ctk.CTkLabel(stats_frame, text="Active Processes: 0", font=("Arial", 14, "bold"))
    process_count_label.pack(side="left", padx=20, pady=10)

    # Graphiques interactifs
    graph_frame = ctk.CTkFrame(main_frame, fg_color="#333333")
    graph_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Créer un graphique avec un fond personnalisé
    fig, (cpu_ax, ram_ax) = plt.subplots(2, 1, figsize=(8, 6))
    fig.tight_layout(pad=3)

    # Changer la couleur du fond
    fig.patch.set_facecolor('#2b2b2b')  # Fond de la figure
    cpu_ax.set_facecolor('#2b2b2b')  # Fond de l'axe CPU
    ram_ax.set_facecolor('#2b2b2b')  # Fond de l'axe RAM

    cpu_ax.set_title("Utilisation de la CPU (%)", fontsize=12, color='white')
    cpu_ax.set_xlim(0, 50)
    cpu_ax.set_ylim(0, 100)
    cpu_line, = cpu_ax.plot([], [], label="CPU", color="#ff6347")  # Changer couleur en rouge
    cpu_ax.legend(loc='upper left', fontsize=10, facecolor='white')

    ram_ax.set_title("Utilisation de la RAM (%)", fontsize=12, color='white')
    ram_ax.set_xlim(0, 50)
    ram_ax.set_ylim(0, 100)
    ram_line, = ram_ax.plot([], [], label="RAM", color="#1e90ff")  # Changer couleur en bleu
    ram_ax.legend(loc='upper left', fontsize=10, facecolor='white')

    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.get_tk_widget().pack(fill="both", expand=True)

    # Données en temps réel
    cpu_data = []
    ram_data = []
    time_data = []
    max_cpu = 0
    max_ram = 0
    start_time = time.time()  # Temps de début de la session

   

    def update_time():
        """Met à jour le temps écoulé depuis le début de la session."""
        while True:
            elapsed_time = time.time() - start_time
            hours, remainder = divmod(int(elapsed_time), 3600)
            minutes, seconds = divmod(remainder, 60)
            formatted_time = f"{hours:02}:{minutes:02}:{seconds:02}"
            clock_label.configure(text=formatted_time)
            time.sleep(1)

    def update_graph():
        nonlocal max_cpu, max_ram
        x = 0
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            ram_usage = psutil.virtual_memory().percent
            active_processes = len(psutil.pids())

            cpu_data.append(cpu_usage)
            ram_data.append(ram_usage)
            time_data.append(x)

            max_cpu = max(max_cpu, cpu_usage)
            max_ram = max(max_ram, ram_usage)

            # Mise à jour des widgets
            cpu_progress.set(cpu_usage / 100)
            ram_progress.set(ram_usage / 100)
            cpu_max_label.configure(text=f"Max CPU: {max_cpu}%")
            ram_max_label.configure(text=f"Max RAM: {max_ram}%")
            process_count_label.configure(text=f"Active Processes: {active_processes}")

            # Mise à jour des graphiques
            if len(time_data) > 50:
                time_data.pop(0)
                cpu_data.pop(0)
                ram_data.pop(0)

            cpu_line.set_data(time_data, cpu_data)
            ram_line.set_data(time_data, ram_data)

            cpu_ax.set_xlim(max(0, x - 50), x)
            ram_ax.set_xlim(max(0, x - 50), x)

            canvas.draw()
            x += 1

    threading.Thread(target=update_time, daemon=True).start()
    threading.Thread(target=update_graph, daemon=True).start()
    
    # Bouton pour exporter les données
    export_button = ctk.CTkButton(
        main_frame,
        text="Exporter les Données",
        command=lambda: export_to_csv(cpu_data, ram_data, time_data),
        fg_color="#4caf50",
        hover_color="#81c784",
        font=("Arial", 14)
    )
    export_button.pack(pady=10)
    
    return visualisation_frame
"""
def export_to_csv(cpu_data, ram_data, time_data):
    
    #Exporte les données des graphiques vers un fichier CSV.
    
    filename = "data_export.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Time", "CPU Usage (%)", "RAM Usage (%)"])
        for t, cpu, ram in zip(time_data, cpu_data, ram_data):
            writer.writerow([t, cpu, ram])
"""


def export_to_csv(cpu_data, ram_data, time_data):
    """
    Exporte les données des graphiques vers un fichier CSV et affiche un message de confirmation.
    """
    filename = "data_export.csv"
    if cpu_data and ram_data and time_data:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Time", "CPU Usage (%)", "RAM Usage (%)"])
            for t, cpu, ram in zip(time_data, cpu_data, ram_data):
                writer.writerow([t, cpu, ram])
        showinfo("Exportation Réussie", f"Données exportées vers {filename}.")
    else:
        showinfo("Exportation Échouée", "Aucune donnée à exporter.")


