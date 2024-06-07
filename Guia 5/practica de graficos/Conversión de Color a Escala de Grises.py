# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 01:28:12 2024

@author: lovito99
"""
import numpy as np
import matplotlib.pyplot as plt

from skimage import io

# Leer una imagen desde un archivo
image = io.imread(r'C:\Users\lovito99\Desktop\Guia 5\practica de graficos\imagen.jpg')
# Convertir una imagen a escala de grises
gray_image = np.mean(image, axis=2).astype(np.uint8)

# Visualizar la imagen en escala de grises
plt.imshow(gray_image, cmap='gray')
plt.show()

