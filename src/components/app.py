import customtkinter as ctk
from affichage_temps_reel import create_real_time_process_display
from sidebar import create_sidebar
from graph import create_visualisation_page
from notification import create_notification_page
from rapport import create_report_page
from PIL import Image

# Initialisation de l'application
app = ctk.CTk()
app.geometry("1200x800")
app.title("Gestionnaire des Processus Linux")

# Apparence
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Conteneur pour les frames dynamiques
frames = {}

def show_frame(frame_name):
    """
    Affiche uniquement la frame spécifiée et cache les autres.
    """
    for frame in frames.values():
        frame.pack_forget()  # Cache toutes les frames
    if frame_name in frames:
        frames[frame_name].pack(fill="both", expand=True, padx=10, pady=10)
    else:
        print(f"Erreur : la frame '{frame_name}' n'existe pas.")

def display_section_callback(section_name, options=None):
    """
    Callback pour afficher une section en fonction du nom sélectionné.
    """
    if section_name == "Base":
        show_frame("base")
    elif section_name == "Visualisation":
        show_frame("visualisation")
    elif section_name == "Notifications":
        show_frame("notifications")
    elif section_name == "Rapports":
        show_frame("rapport")
    else:
        print(f"Erreur : section '{section_name}' inconnue.")

# Création de la sidebar
create_sidebar(app, display_section_callback)

# Frame principale
main_frame = ctk.CTkFrame(app, corner_radius=15)
main_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Frame pour la page "Base"
base_frame = ctk.CTkFrame(main_frame, corner_radius=15)
frames["base"] = base_frame

# Ajouter le titre dans la page Base
title_label = ctk.CTkLabel(
    base_frame,
    text="Gestionnaire des Processus",
    font=("Forte", 30, "bold"),
    text_color="white"
)
title_label.pack(pady=20)  # Espace autour du titre

# Contenu de la page Base
create_real_time_process_display(base_frame)

# Frame pour la page "Visualisation"
visualisation_frame = create_visualisation_page(main_frame)
frames["visualisation"] = visualisation_frame

# Frame pour la page "Notifications"
notification_frame = create_notification_page(main_frame)
frames["notifications"] = notification_frame

# Frame pour la page "Rapports"
rapport_frame = create_report_page(main_frame)
frames["rapport"] = rapport_frame

# Afficher la page "Base" par défaut
show_frame("base")

# Lancer l'application
app.mainloop()
