import customtkinter as ctk

def create_sidebar(app, display_section_callback):
    """
    Crée la sidebar avec les sections et affiche les options comme des onglets.
    """
    # Conteneur pour la sidebar
    sidebar_container = ctk.CTkFrame(app, width=250, fg_color="#2b2b2b", corner_radius=0)
    sidebar_container.pack(side="left", fill="y", padx=5, pady=5)

    # Liste des sections avec leurs options
    sections = {
        "Base": ["Temps Réel"],
        "Visualisation": ["Graphiques"],
        "Notifications": ["Alertes"],
        "Rapports": ["Rapports"],
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
        section_button.pack(side="top", padx=15, pady=15)
