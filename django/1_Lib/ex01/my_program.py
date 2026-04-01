from path import Path

def create_and_display():
    # Definimos la ruta de la carpeta y el archivo
    folder = Path("folder")

    # Creamos la carpeta si no existe
    if not folder.exists():
        folder.mkdir()

    # Definimos el archivo dentro de la carpeta
    filename = folder / "file.txt"

    # Escribimos contenido
    filename.write_text("En un lugar de la mancha, de cuyo nombre no quiero acordarme... 😉")

    # Leemos y mostramos el contenido
    content = filename.read_text()
    print(content)

def cleanup():
    """
    Limpia el entorno tras la defensa eliminando archivos y carpetas.
    """
    targets = [
        Path("local_lib"),
        Path("folder"),
        Path("install.log")
    ]

    for item in targets:
        if item.exists():
            if item.is_dir():
                item.rmtree_p()
            else:
                item.remove_p()
            print(f"Eliminado: {item}")

if __name__ == "__main__":
    create_and_display()

    # Descomenta la siguiente línea tras la defensa:
    # cleanup()