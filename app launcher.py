import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import subprocess
import platform

# Detectar sistema operativo
is_windows = platform.system() == "Windows"
is_linux = platform.system() == "Linux"
is_mac = platform.system() == "Darwin"

# Colores y fuente
BG_COLOR = "#f8f9fa"
CARD_COLOR = "#ffffff"
TEXT_COLOR = "#343a40"
HIGHLIGHT = "#6c63ff"
FONT = ("Segoe UI", 10, "bold")  # puedes cambiar a "Helvetica Neue" o "Poppins" si lo tienes instalado

# Función para abrir apps
def open_app(command):
    try:
        if is_windows:
            os.startfile(command)
        elif is_mac:
            subprocess.Popen(["open", command])
        elif is_linux:
            subprocess.Popen([command])
        else:
            raise OSError("Sistema no compatible")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo abrir la aplicación:\n{e}")

# Botón con ícono y texto
def create_icon_button(parent, icon_path, text, command_path):
    img = Image.open(icon_path).resize((64, 64), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(img)

    btn = tk.Button(
        parent,
        image=photo,
        text=text,
        compound="top",
        command=lambda: open_app(command_path),
        font=FONT,
        bg=CARD_COLOR,
        fg=TEXT_COLOR,
        activebackground="#e9ecef",
        bd=1,
        relief="flat",
        width=100,
        height=100,
        highlightthickness=0
    )
    btn.image = photo  # prevenir garbage collection
    return btn

# Crear ventana
root = tk.Tk()
root.title("🚀 Lanzador de Aplicaciones")
root.configure(bg=BG_COLOR)

# Centrar ventana
window_width = 590
window_height = 260
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Título
title = tk.Label(
    root,
    text="Lanzador de Aplicaciones",
    font=("Segoe UI", 16, "bold"),
    bg=BG_COLOR,
    fg=HIGHLIGHT
)
title.pack(pady=10)

# Contenedor tipo "card"
card = tk.Frame(root, bg=CARD_COLOR, bd=1, relief="solid")
card.pack(padx=20, pady=10)

# Lista de apps
apps = [
    ("Bloc de notas", "icons/notepad.png", "notepad" if is_windows else "gedit"),
    ("Calculadora", "icons/calculator.png", "calc" if is_windows else "gnome-calculator"),
    ("Navegador", "icons/chrome.png", "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" if is_windows else "google-chrome"),
    ("Terminal", "icons/terminal.png", "cmd" if is_windows else "gnome-terminal"),
]

# Crear botones
for i, (label, icon, cmd) in enumerate(apps):
    btn = create_icon_button(card, icon, label, cmd)
    btn.grid(row=0, column=i, padx=15, pady=15)

root.mainloop()
