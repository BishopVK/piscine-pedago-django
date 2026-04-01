"""
Características clave de pathlib: 
    Creación de rutas: p = Path('carpeta/archivo.txt')
    Obtener directorio actual: Path.cwd()
    Manipulación: .name (nombre del archivo), .stem (nombre sin extensión), .suffix (extensión), .parent (directorio padre).
    Verificación: .exists(), .is_file(), .is_dir().
    Operaciones: .mkdir(), .rename(), .unlink() (eliminar).

Ejemplo de uso:
    from pathlib import Path

    # Crear una ruta
    ruta = Path("documentos/informe.pdf")

    print(f"Nombre: {ruta.name}")       # informe.pdf
    print(f"Extensión: {ruta.suffix}")  # .pdf
    print(f"Padre: {ruta.parent}")      # documentos
"""

from pathlib import Path

# Crear una ruta
ruta = Path("documentos/informe.pdf")

print(f"Nombre: {ruta.name}")       # informe.pdf
print(f"Extensión: {ruta.suffix}")  # .pdf
print(f"Padre: {ruta.parent}")      # documentos