import sys
import os
import re
import settings # Importamos nuestro archivo de variables

def render():
    # 1. Gestión de errores de argumentos
    if len(sys.argv) != 2:
        print("Error: El programa necesita exactamente un argumento.")
        exit(1)

    template_name = sys.argv[1]

    # 2. Gestión de error: Extensión incorrecta
    if not template_name.endswith(".template"):
        print("Error: El archivo debe tener la extensión '.template'")
        exit(1)

    # 3. Gestión de error: Archivo no existe
    if not os.path.exists(template_name):
        print(f"Error: El archivo '{template_name}' no existe.")
        exit(1)

    try:
        # 4. Leer el contenido de la plantilla
        with open(template_name, "r") as f:
            content = f.read()

        # 5. Lógica de reemplazo (Keyword expansion)
        # Buscamos patrones como {name} y los reemplazamos por el valor en settings.py
        for key in dir(settings):
            if not key.startswith("__"): # Ignoramos variables internas de Python
                value = str(getattr(settings, key))
                content = content.replace("{" + key + "}", value)

        # 6. Escribir el resultado en un .html
        output_name = template_name.replace(".template", ".html")
        with open(output_name, "w") as f:
            f.write(content)

    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == '__main__':
    render()