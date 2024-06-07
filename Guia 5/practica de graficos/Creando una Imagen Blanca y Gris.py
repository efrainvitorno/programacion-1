# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 01:23:16 2024

@author: lovito99
"""
import numpy as np
import matplotlib.pyplot as plt
# Crear una matriz de 10x10 con todos los valores iguales a 128 (gris medio)
gray_image = np.full((10, 10), 128, dtype=np.uint8)

# Visualizar la imagen
plt.imshow(gray_image, cmap='gray')
plt.show()
