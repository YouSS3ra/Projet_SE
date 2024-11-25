# styles.py

# Palette de couleurs
COLORS = {
    "primary": "#4caf50",
    "secondary": "#388e3c",
    "background": "#2b2b2b",
    "text_light": "#ffffff",
    "text_dark": "#333333",
    "hover": "#81c784",
}

# Thèmes
THEMES = {
    "dark": {
        "bg": COLORS["background"],
        "fg": COLORS["text_light"],
        "hover": COLORS["hover"],
    },
    "light": {
        "bg": "#ffffff",
        "fg": COLORS["text_dark"],
        "hover": "#e0e0e0",
    },
}
