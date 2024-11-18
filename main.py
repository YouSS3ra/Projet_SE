'''
import subprocess
# Exécuter la commande 'ls' sur Linux
result = subprocess.run(['ls', '-l'], capture_output=True, text=True)

# Afficher le résultat
print(result.stdout)
'''

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
