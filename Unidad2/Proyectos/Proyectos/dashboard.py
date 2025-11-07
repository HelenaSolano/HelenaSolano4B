import tkinter as tk
from tkinter import messagebox
from user_view import UserApp
from products_view import ProductosApp

class DashboardApp:
    def __init__(self, username):
        self.username = username
        self.root = tk.Tk()
        self.root.title(f"Panel principal - Bienvenido {username}")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        tk.Label(self.root, text=f"Hola, {username}", font=("Arial", 18, "bold")).pack(pady=20)
        tk.Label(self.root, text="Selecciona un módulo para continuar:", font=("Arial", 12)).pack(pady=10)

        tk.Button(self.root, text="Gestión de Usuarios", width=25, command=self.abrir_usuarios).pack(pady=10)
        tk.Button(self.root, text="Gestión de Productos", width=25, command=self.abrir_productos).pack(pady=10)
        tk.Button(self.root, text="Cerrar sesión", width=25, command=self.cerrar_sesion).pack(pady=20)

        self.root.mainloop()

    def abrir_usuarios(self):
        self.root.withdraw()
        UserApp(self.username)
        self.root.deiconify()

    def abrir_productos(self):
        self.root.withdraw()
        ProductosApp(self.username)
        self.root.deiconify()

    def cerrar_sesion(self):
        if messagebox.askyesno("Cerrar sesión", "¿Deseas cerrar sesión?"):
            self.root.destroy()
