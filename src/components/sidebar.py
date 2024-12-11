import customtkinter as ctk
from tkinter import PhotoImage


def create_sidebar(app, display_section_callback):
    """
    Crée la sidebar avec un titre et des boutons de navigation.
    """
    # Conteneur pour la sidebar
    sidebar_container = ctk.CTkFrame(app, width=250, fg_color="#2b2b2b", corner_radius=0)
    sidebar_container.pack(side="left", fill="y", padx=5, pady=5)

    # Titre dans la sidebar
    title_label = ctk.CTkLabel(
        sidebar_container,
        text="Gestionnaire",
        font=("Forte", 20, "bold"),
        text_color="white"
    )
    title_label.pack(pady=20)

    # Liste des sections avec leurs options
    sections = {
        "Base": ["Temps Réel"],
        "Visualisation": ["Graphiques"],
        "Notifications": ["Alertes"],
        "Rapports": ["Rapports"],
        "Mode Commande": ["Commandes Disponibles"]
    }

    # Fonction appelée lors du clic sur une section
    def on_section_click(section_name):
        display_section_callback(section_name, sections[section_name])

    # Ajouter un bouton pour chaque section
    for section_name in sections:
        section_button = ctk.CTkButton(
            sidebar_container,
            text=section_name,
            width=200,
            height=40,
            corner_radius=15,
            fg_color="#4caf50",
            hover_color="#81c784",
            font=("Arial", 14),
            command=lambda name=section_name: on_section_click(name)
        )
        section_button.pack(side="top", padx=15, pady=10)
