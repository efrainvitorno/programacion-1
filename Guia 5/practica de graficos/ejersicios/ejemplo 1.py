# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 01:49:27 2024

@author: lovito99
"""

from skimage import io
import numpy as np
import matplotlib.pyplot as plt

def imagenSuave(image):
    # Convertir la imagen a flotantes para evitar problemas de tipo de dato
    NuevImagen = np.copy(image).astype(float)
    for i in range(1, image.shape[0] - 1):
        for j in range(1, image.shape[1] - 1):
            # Promediar los valores de los píxeles vecinos ( utilizando solo 4 posiciones)
            NuevImagen[i, j] = (image[i-1, j] + image[i+1, j] + image[i, j-1] + image[i, j+1]) / 4.0
    return NuevImagen

# Leer una imagen en escala de grises
Imagenbn = io.imread(r'C:\Users\lovito99\Desktop\Guia 5\practica de graficos\ejersicios\imagenbn.jpg', as_gray=True)

# Suavizar la imagen
ImagenProcesada = imagenSuave(Imagenbn)

# Visualizar la imagen original y la imagen suavizada
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(Imagenbn, cmap='gray')
axes[0].set_title('Imagen Original')
axes[1].imshow(ImagenProcesada, cmap='gray')
axes[1].set_title('Imagen Suavizada')
plt.show()
