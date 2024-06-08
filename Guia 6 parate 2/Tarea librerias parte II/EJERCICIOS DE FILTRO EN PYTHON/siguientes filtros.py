from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen
imagen = Image.open(r'C:\Users\lovito99\Downloads\imgen.jpg')

# Convertir la imagen a un arreglo numpy
imagen_np = np.array(imagen)

def aplicar_filtro_sepia(imagen_np):
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
#funcion imagen con promedio 
def promedio_vecinos(imagen_np):
    # Crear una copia de la imagen para no modificar la original
    promedio = np.copy(imagen_np)
    filas, columnas, _ = imagen_np.shape
    
    for i in range(1, filas-1):
        for j in range(1, columnas-1):
            for k in range(3):  # Para cada canal de color
                suma = (imagen_np[i-1:i+2, j-1:j+2, k].sum())
                promedio[i, j, k] = suma // 9
    
    return promedio
#funcion valor central 
def valor_central_vecinos(imagen_np):
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
imagen_sepia = aplicar_filtro_sepia(imagen_np)
#aplicar imagen promedio
imagen_promedio = promedio_vecinos(imagen_np)
#aplicar imgen central 
imagen_central = valor_central_vecinos(imagen_np)
#mostrar imagen con promedio 
# Mostrar la imagen con el promedio de vecinos
plt.imshow(imagen_promedio)
plt.title("Imagen con Promedio de Vecinos")
plt.axis('off')
plt.show()

# Mostrar la imagen con el filtro sepia
plt.imshow(imagen_sepia)
plt.title("Imagen con Filtro Sepia")
plt.axis('off')
plt.show()
# mostra imagen central 
# Mostrar la imagen con el valor central de vecinos
plt.imshow(imagen_central)
plt.title("Imagen con Valor Central de Vecinos")
plt.axis('off')
plt.show()