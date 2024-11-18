'''
import subprocess
# Exécuter la commande 'ls' sur Linux
result = subprocess.run(['ls', '-l'], capture_output=True, text=True)

# Afficher le résultat
print(result.stdout)


import customtkinter as ctk

# Créer une fenêtre principale
app = ctk.CTk()

# Définir les dimensions et le titre de la fenêtre
app.geometry("400x300")
app.title("Application Linux")

# Ajouter un label
label = ctk.CTkLabel(app, text="Bienvenue sur mon Application", font=("Arial", 20))
label.pack(pady=20)

# Ajouter un bouton qui affiche un message
def on_button_click():
    label.configure(text="Vous avez cliqué sur le bouton!")

button = ctk.CTkButton(app, text="Cliquez ici", command=on_button_click)
button.pack(pady=20)


app.configure(bg_color="gray")
button = ctk.CTkButton(app, text="Cliquez ici", command=on_button_click, fg_color="blue", hover_color="lightblue")


# Lancer l'application
app.mainloop()
'''

import customtkinter as ctk

# Initialiser l'application
app = ctk.CTk()
app.geometry("1000x600")
app.title("Mon Application Linux")

# Palette de couleurs (mode sombre par défaut)
ctk.set_appearance_mode("dark")  # "dark" ou "light"
ctk.set_default_color_theme("blue")  # "blue", "green", ou "dark-blue"

# Barre latérale (Sidebar)
sidebar = ctk.CTkFrame(app, width=200, corner_radius=0)
sidebar.pack(side="left", fill="y")

# Ajouter des boutons à la sidebar
button1 = ctk.CTkButton(sidebar, text="Processus", command=lambda: change_page("processus"))
button1.pack(pady=20, padx=10)
button2 = ctk.CTkButton(sidebar, text="Graphiques", command=lambda: change_page("graphiques"))
button2.pack(pady=20, padx=10)
button3 = ctk.CTkButton(sidebar, text="Historique", command=lambda: change_page("historique"))
button3.pack(pady=20, padx=10)

# Contenu principal (Main Content)
content_frame = ctk.CTkFrame(app, corner_radius=10)
content_frame.pack(side="right", fill="both", expand=True)

# Fonction pour changer de page
def change_page(page):
    for widget in content_frame.winfo_children():
        widget.destroy()  # Efface le contenu précédent

    if page == "processus":
        label = ctk.CTkLabel(content_frame, text="Page des Processus", font=("Arial", 20))
        label.pack(pady=20)
    elif page == "graphiques":
        label = ctk.CTkLabel(content_frame, text="Page des Graphiques", font=("Arial", 20))
        label.pack(pady=20)
    elif page == "historique":
        label = ctk.CTkLabel(content_frame, text="Page de l'Historique", font=("Arial", 20))
        label.pack(pady=20)

# Lancer l'application
app.mainloop()
