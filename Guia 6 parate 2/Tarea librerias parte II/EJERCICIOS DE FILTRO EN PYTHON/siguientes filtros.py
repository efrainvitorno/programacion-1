from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen
imagen = Image.open(r'C:\Users\lovito99\Downloads\imgen.jpg')

# Convertir la imagen a un arreglo numpy
imagen_np = np.array(imagen)

def AplicarFiltroSepia(imagen_np):
    # Crear una copia de la imagen para no modificar la original
    sepia = np.copy(imagen_np)
    
    # Aplicar las fórmulas para cada canal
    for i in range(imagen_np.shape[0]):
        for j in range(imagen_np.shape[1]):
            rojo = imagen_np[i, j, 0]
            verde = imagen_np[i, j, 1]
            azul = imagen_np[i, j, 2]
            
            sepia[i, j, 0] = min(255, 0.393 * rojo + 0.769 * verde + 0.189 * azul)
            sepia[i, j, 1] = min(255, 0.349 * rojo + 0.686 * verde + 0.168 * azul)
            sepia[i, j, 2] = min(255, 0.272 * rojo + 0.534 * verde + 0.131 * azul)
    
    return sepia

# Función para aplicar el filtro de promedio de vecinos
def PromedioVesinos(imagen_np):
    # Crear una copia de la imagen para no modificar la original
    promedio = np.copy(imagen_np)
    filas, columnas, _ = imagen_np.shape
    
    for i in range(1, filas-1):
        for j in range(1, columnas-1):
            for k in range(3):  # Para cada canal de color
                suma = (imagen_np[i-1:i+2, j-1:j+2, k].sum())
                promedio[i, j, k] = suma // 9
    
    return promedio

# Función para aplicar el filtro de valor central de vecinos
def ValorCentralVesinos(imagen_np):
    # Crear una copia de la imagen para no modificar la original
    central = np.copy(imagen_np)
    filas, columnas, _ = imagen_np.shape
    
    for i in range(1, filas-1):
        for j in range(1, columnas-1):
            for k in range(3):  # Para cada canal de color
                vecinos = imagen_np[i-1:i+2, j-1:j+2, k].flatten()
                vecinos.sort()
                central[i, j, k] = vecinos[len(vecinos) // 2]
    
    return central

# Aplicar el filtro sepia
ImagenSepia = AplicarFiltroSepia(imagen_np)
# Aplicar el filtro de promedio de vecinos
ImagenPromedio = PromedioVesinos(imagen_np)
# Aplicar el filtro de valor central de vecinos
ImagenCentral = ValorCentralVesinos(imagen_np)

# Mostrar la imagen con el promedio de vecinos
plt.imshow(ImagenPromedio)
plt.title("Imagen con Promedio de Vecinos")
plt.axis('off')
plt.show()

# Mostrar la imagen con el filtro sepia
plt.imshow(ImagenSepia)
plt.title("Imagen con Filtro Sepia")
plt.axis('off')
plt.show()

# Mostrar la imagen con el valor central de vecinos
plt.imshow(ImagenCentral)
plt.title("Imagen con Valor Central de Vecinos")
plt.axis('off')
plt.show()

# Conclusión
print("Conclusión:")
print("1. Filtro Sepia: Transforma la imagen original en tonos marrones, creando un efecto vintage.")
print("   Este filtro es útil para dar a las imágenes un aspecto antiguo o nostálgico.")
print("2. Promedio de Vecinos: Suaviza la imagen al reducir el ruido y los detalles finos.")
print("   Es ideal para eliminar pequeñas imperfecciones o ruido, pero puede hacer que la imagen parezca borrosa.")
print("3. Valor Central de Vecinos: Reduce el ruido impulsivo mientras mantiene mejor los bordes y detalles comparado con el filtro de promedio.")
print("   Este filtro es adecuado para eliminar el ruido de las imágenes manteniendo las características importantes.")
