import json
import os
import tkinter as tk


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