# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 01:21:00 2024

@author: lovito99
"""

import numpy as np
import matplotlib.pyplot as plt

# Crear una matriz de 10x10 con valores de 0 a 255
gray_image = np.array([[i * j for j in range(10)] for i in range(10)], dtype=np.uint8)

# Visualizar la imagen
plt.imshow(gray_image, cmap='gray')
plt.show()