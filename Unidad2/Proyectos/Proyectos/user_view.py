import tkinter as tk
from tkinter import messagebox, ttk
from user_controller import agregar_usuarios, ver_usuarios, actualizar_usuarios, eliminar_usuarios

class UserApp:
    def __init__(self, username):
        self.username = username 
        self.root = tk.Tk()
        self.root.title(f"Gestión de Usuarios - Bienvenido {username}")
        self.root.geometry("900x600")

        self.crear_elementos()
        self.ver_usuarios()
        self.root.mainloop()

    def crear_elementos(self):
        tk.Label(self.root, text=f"Hola, {self.username}", font=("Arial", 22, "bold")).pack(pady=10)

        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        tk.Button(frame, text="Agregar usuario", command=self.agregar_usuario).grid(row=0, column=0, padx=10)
        tk.Button(frame, text="Actualizar usuario", command=self.actualizar_usuario).grid(row=0, column=1, padx=10)
        tk.Button(frame, text="Eliminar usuario", command=self.eliminar_usuario).grid(row=0, column=2, padx=10)
        tk.Button(frame, text="Cerrar", command=self.root.destroy).grid(row=0, column=3, padx=10)

        self.tree = ttk.Treeview(self.root, columns=("ID", "Usuario"), show="headings", height=15)
        self.tree.heading("ID", text="ID")
        self.tree.heading("Usuario", text="Usuario")
        self.tree.pack(fill="both", expand=True)

    def ver_usuarios(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for u in ver_usuarios():
            self.tree.insert("", tk.END, values=u)

    def agregar_usuario(self):
        def guardar():
            u, p = entry_user.get().strip(), entry_pass.get().strip()
            if not u or not p:
                messagebox.showwarning("Campos vacíos", "Ingrese usuario y contraseña.")
                return
            if agregar_usuarios(u, p):
                messagebox.showinfo("Éxito", f"Usuario '{u}' agregado.")
                ventana.destroy()
                self.root.after(100, self.ver_usuarios)
            else:
                messagebox.showerror("Error", "No se pudo crear el usuario.")

        ventana = tk.Toplevel(self.root)
        ventana.title("Agregar usuario")
        tk.Label(ventana, text="Usuario:").pack(pady=5)
        entry_user = tk.Entry(ventana)
        entry_user.pack()
        tk.Label(ventana, text="Contraseña:").pack(pady=5)
        entry_pass = tk.Entry(ventana, show="*")
        entry_pass.pack()
        tk.Button(ventana, text="Guardar", command=guardar).pack(pady=10)

    def actualizar_usuario(self):
        sel = self.tree.focus()
        if not sel:
            messagebox.showwarning("Atención", "Seleccione un usuario.")
            return
        id_usuario, user_actual = self.tree.item(sel, "values")

        def guardar():
            nuevo_u, nuevo_p = entry_user.get().strip(), entry_pass.get().strip()
            if not nuevo_u or not nuevo_p:
                messagebox.showwarning("Campos vacíos", "Debe llenar todos los campos.")
                return
            if actualizar_usuarios(id_usuario, nuevo_u, nuevo_p):
                messagebox.showinfo("Éxito", "Usuario actualizado.")
                ventana.destroy()
                self.root.after(100, self.ver_usuarios)
            else:
                messagebox.showerror("Error", "No se pudo actualizar.")

        ventana = tk.Toplevel(self.root)
        ventana.title("Actualizar usuario")
        tk.Label(ventana, text="Nuevo usuario:").pack(pady=5)
        entry_user = tk.Entry(ventana)
        entry_user.insert(0, user_actual)
        entry_user.pack()
        tk.Label(ventana, text="Nueva contraseña:").pack(pady=5)
        entry_pass = tk.Entry(ventana, show="*")
        entry_pass.pack()
        tk.Button(ventana, text="Guardar cambios", command=guardar).pack(pady=10)

    def eliminar_usuario(self):
        sel = self.tree.focus()
        if not sel:
            messagebox.showwarning("Atención", "Seleccione un usuario.")
            return
        id_usuario, username = self.tree.item(sel, "values")
        if messagebox.askyesno("Confirmar", f"¿Eliminar al usuario '{username}'?"):
            if eliminar_usuarios(id_usuario):
                messagebox.showinfo("Éxito", "Usuario eliminado.")
                self.root.after(100, self.ver_usuarios)
            else:
                messagebox.showerror("Error", "No se pudo eliminar.")
