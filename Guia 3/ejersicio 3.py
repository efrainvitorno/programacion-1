from pathlib import Path

def ListadeArchivos(RutaCarpeta, extension):
    """
    Lista los archivos y directorios con una extensión específica en la carpeta dada y sus subcarpetas.
    
    Args:
    RutaCarpeta (str): Ruta de la carpeta donde buscar los archivos.
    extension (str): Extensión de los archivos a listar (por ejemplo, ".mp3").
    
    Returns:
    list: Lista de archivos y directorios con la extensión especificada.
    """
    archivos = [archivo for archivo in Path(RutaCarpeta).rglob(f"*{extension}")]
    return archivos

def ImprimirArbol(RutaCarpeta, extension, prefijo=""):
    """
    Imprime el contenido de una carpeta en forma de árbol jerarquizado, filtrando por extensión de archivo.
    
    Args:
    RutaCarpeta (str): Ruta de la carpeta cuya estructura queremos imprimir.
    extension (str): Extensión de los archivos a listar (por ejemplo, ".mp3").
    prefijo (str): Prefijo utilizado para mostrar la estructura jerárquica.
    """
    carpeta = Path(RutaCarpeta)
    contenido = sorted(carpeta.iterdir(), key=lambda x: (x.is_file(), x.name))
    total_elementos = len(contenido)
    
    for indice, elemento in enumerate(contenido):
        es_ultimo = (indice == total_elementos - 1)
        prefijo_actual = prefijo + ("└── " if es_ultimo else "├── ")
        
        if elemento.is_file() and elemento.suffix == extension:
            print(prefijo_actual + elemento.name)
        elif elemento.is_dir():
            print(prefijo_actual + elemento.name)
            prefijo_nuevo = prefijo + ("    " if es_ultimo else "│   ")
            ImprimirArbol(elemento, extension, prefijo_nuevo)

# Ejemplo de uso
RutaCarpeta = Path(r"C:\Users\lovito99\Desktop\programacion 1\Guia 3")
extension = ".mp3"  # Cambia esta extensión según sea necesario
ImprimirArbol(RutaCarpeta, extension)
