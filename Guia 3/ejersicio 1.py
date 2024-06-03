from pathlib import Path

def ListadeArchivos(RutaCarpeta, extension):
    """
    Lista los archivos con una extensión específica en la carpeta dada.
    
    Args:
    RutaCarpeta (str): Ruta de la carpeta donde buscar los archivos.
    extension (str): Extensión de los archivos a listar (por ejemplo, ".mp3").
    
    Returns:
    list: Lista de archivos con la extensión especificada.
    """
    # Obtener todos los archivos en la carpeta dada
    archivos = [archivo for archivo in Path(RutaCarpeta).iterdir() if archivo.is_file()]
    # Filtrar archivos por la extensión dada usando una expresión lambda
    ArchivosFiltrados = list(filter(lambda archivo: archivo.suffix == extension, archivos))
    return ArchivosFiltrados

# Ejemplo de uso
RutaCarpeta = Path(r"C:\Users\lovito99\Desktop\programacion 1\Guia 3")  
extension = ".mp3"  # Cambia esta extensión según sea necesario
archivos = ListadeArchivos(RutaCarpeta, extension)

print(f"Archivos con extensión {extension} en la carpeta {RutaCarpeta}:")
for archivo in archivos:
    print("- " + archivo.name)
