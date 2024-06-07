"""
Created on Fri Jun  7 02:46:19 2024

@author: lovito99
"""
from skimage import io
import numpy as np
import matplotlib.pyplot as plt

def ImengenReflejada(image):
    # Rotar la imagen 90 grados en sentido antihorario
    return np.rot90(image)

def RotarImagen(image):
    # Rotar la imagen 90 grados en sentido horario
    return np.rot90(image, k=3)

# Leer una imagen a color
Imagen = io.imread(r'C:\Users\lovito99\Desktop\Guia 5\practica de graficos\ejersicios\imagenbn.jpg')

# Rotar la imagen 90 grados
Rotar = ImengenReflejada(Imagen)
# Para rotar 90 grados en sentido horario, usa la siguiente línea en su lugar:

# Visualizar la imagen original y la imagen rotada
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(Imagen)
axes[0].set_title('Imagen Original')
axes[1].imshow(Rotar)
axes[1].set_title('Imagen Rotada verticalmente')
plt.show()
