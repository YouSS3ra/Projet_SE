import tkinter as tk
import customtkinter as ctk
import os
import subprocess

def create_report_page(parent):
    """
    Crée une page rapport avec une image et un bouton dans une frame centralisée
    à droite de la barre latérale, et un pied de page stylisé.
    """
    # Cadre principal (page complète)
    report_frame = ctk.CTkFrame(parent, corner_radius=15, fg_color="#2E2E2E")

    # En-tête
    header_frame = ctk.CTkFrame(report_frame, height=80, fg_color="#3C3F41", corner_radius=15)
    header_frame.pack(fill="x", padx=20, pady=20)

    header_label = ctk.CTkLabel(
        header_frame,
        text="Rapport d'Utilisation",
        font=("Forte", 30, "bold"),
        text_color="#FFFFFF"
    )
    header_label.pack(pady=10, padx=10)

    # Séparateur décoratif
    separator = ctk.CTkFrame(report_frame, height=2, fg_color="#4caf50", corner_radius=0)
    separator.pack(fill="x", padx=20)

    # Section principale (frame contenant image + bouton)
    main_content_frame = ctk.CTkFrame(report_frame, fg_color="#2E2E2E")
    main_content_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Cadre centré dans la frame principale
    central_frame = ctk.CTkFrame(main_content_frame, corner_radius=10, fg_color="#3C3F41")
    central_frame.pack(expand=True)

    # Ajout de l'image
    image_path = "C:/Users/ELITEBOOK/Desktop/ProjetLinux/assets/images/excel2.png"  # Chemin vers l'image
    try:
        photo = tk.PhotoImage(file=image_path)
        image_label = ctk.CTkLabel(central_frame, image=photo, text="")
        image_label.image = photo  # Référence pour éviter le garbage collection
        image_label.pack(pady=(20, 10))  # Ajout d'un padding
    except Exception as e:
        print(f"Erreur lors du chargement de l'image : {e}")

    # Bouton sous l'image
    open_csv_button = ctk.CTkButton(
        central_frame,
        text="Ouvrir Rapport CSV",
        command=open_csv_file,
        fg_color="#4caf50",
        hover_color="#81c784",
        text_color="#FFFFFF",
        font=("Arial", 14, "bold"),
        corner_radius=10,
        height=50,
        width=200
    )
    open_csv_button.pack(pady=(10, 20))

    # Pied de page en bas de la page
    footer_frame = ctk.CTkFrame(report_frame, height=50, fg_color="#3C3F41")
    footer_frame.pack(side="bottom", fill="x")

    footer_label = ctk.CTkLabel(
        footer_frame,
        text="© 2024 - Monitoring System",
        font=("Arial", 12, "italic"),
        text_color="#A9A9A9"
    )
    footer_label.pack(side="right", padx=10, pady=10)

    return report_frame


def open_csv_file():
    """
    Ouvre le fichier CSV dans une application comme Excel.
    """
    filename = "data_export.csv"
    if os.path.exists(f"C:/Users/ELITEBOOK/Desktop/ProjetLinux/{filename}"):
        if os.name == 'nt':  # Windows
            subprocess.run(["start", "excel", filename], shell=True)
        elif os.name == 'posix':  # Linux / macOS
            subprocess.run(["xdg-open", filename])
    else:
        print(f"Le fichier {filename} n'existe pas.")
