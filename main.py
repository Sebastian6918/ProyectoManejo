import json
import os
import tkinter as tk
from tkinter import colorchooser, filedialog, messagebox


def cargar_config():
    archivo = "config.json"
    valores_defecto = {
        "nombre_usuario": "Sebastián",
        "tema_interfaz": "oscuro",
        "idioma": "es-ES",
        "tamano_fuente": 12,
        "color_barra_menu": "#333333",
        "color_letra": "#FFFFFF",
        "foto_perfil": ""
    }
    if not os.path.exists(archivo):
        guardar_config(valores_defecto)
        return valores_defecto
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return valores_defecto


def guardar_config(config):
    archivo_temp = "config.tmp"
    archivo_final = "config.json"
    with open(archivo_temp, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4, ensure_ascii=False)
    if os.path.exists(archivo_final):
        os.replace(archivo_final, "config.bak")
    os.replace(archivo_temp, archivo_final)


def abrir_settings(root, config):
    vent = tk.Toplevel(root)
    vent.title("Settings")
    vent.geometry("300x350")

    tk.Label(vent, text="Nombre Usuario:").pack(pady=2)
    ent_nombre = tk.Entry(vent)
    ent_nombre.insert(0, config.get("nombre_usuario", ""))
    ent_nombre.pack()

    tk.Label(vent, text="Idioma:").pack(pady=2)
    var_idioma = tk.StringVar(value=config.get("idioma", "es-ES"))
    tk.OptionMenu(vent, var_idioma, "es-ES", "en-US").pack()

    tk.Label(vent, text="Tema:").pack(pady=2)
    var_tema = tk.StringVar(value=config.get("tema_interfaz", "oscuro"))
    tk.OptionMenu(vent, var_tema, "claro", "oscuro").pack()

    tk.Label(vent, text="Tamaño Fuente:").pack(pady=2)
    ent_fuente = tk.Entry(vent)
    ent_fuente.insert(0, str(config.get("tamano_fuente", 12)))
    ent_fuente.pack()

    color_barra = [config.get("color_barra_menu", "#333333")]

    def elegir_color_barra():
        color = colorchooser.askcolor()[1]
        if color:
            color_barra[0] = color

    tk.Button(vent, text="Elegir Color Menú", command=elegir_color_barra).pack(pady=5)

    color_letra = [config.get("color_letra", "#FFFFFF")]

    def elegir_color_letra():
        color = colorchooser.askcolor()[1]
        if color:
            color_letra[0] = color

    tk.Button(vent, text="Elegir Color Letra", command=elegir_color_letra).pack(pady=5)

    foto = [config.get("foto_perfil", "")]

    def elegir_foto():
        ruta = filedialog.askopenfilename(filetypes=[("Imagenes", "*.png *.jpg *.jpeg")])
        if ruta:
            foto[0] = ruta

    tk.Button(vent, text="Elegir Foto Perfil", command=elegir_foto).pack(pady=5)

    def guardar():
        try:
            nueva_config = {
                "nombre_usuario": ent_nombre.get(),
                "tema_interfaz": var_tema.get(),
                "idioma": var_idioma.get(),
                "tamano_fuente": int(ent_fuente.get()),
                "color_barra_menu": color_barra[0],
                "color_letra": color_letra[0],
                "foto_perfil": foto[0]
            }
            guardar_config(nueva_config)
            messagebox.showinfo("Guardado", "Configuración actualizada con éxito.")
            vent.destroy()
        except ValueError:
            messagebox.showerror("Error", "El tamaño de la fuente debe ser un número entero.")

    tk.Button(vent, text="Guardar Configuración", command=guardar).pack(pady=15)


def main():
    config = cargar_config()
    root = tk.Tk()
    root.title("App Manejo de Archivos")
    root.geometry("600x400")

    root.configure(bg=config.get("color_barra_menu", "#333333"))

    barra_menu = tk.Menu(root)

    menu_archivo = tk.Menu(barra_menu, tearoff=0)
    menu_archivo.add_command(label="Simulado")
    barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

    menu_edicion = tk.Menu(barra_menu, tearoff=0)
    menu_edicion.add_command(label="Simulado")
    barra_menu.add_cascade(label="Edición", menu=menu_edicion)

    menu_ver = tk.Menu(barra_menu, tearoff=0)
    menu_ver.add_command(label="Simulado")
    barra_menu.add_cascade(label="Ver", menu=menu_ver)

    menu_settings = tk.Menu(barra_menu, tearoff=0)
    menu_settings.add_command(label="Configuración", command=lambda: abrir_settings(root, config))
    barra_menu.add_cascade(label="Settings", menu=menu_settings)

    root.config(menu=barra_menu)

    saludo = f"Hola {config.get('nombre_usuario', '')}"
    lbl = tk.Label(root, text=saludo, fg=config.get("color_letra", "#FFFFFF"),
                   bg=config.get("color_barra_menu", "#333333"), font=("Arial", config.get("tamano_fuente", 12)))
    lbl.pack(expand=True)

    root.mainloop()


if __name__ == "__main__":
    main()