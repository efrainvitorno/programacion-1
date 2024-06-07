# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 01:27:02 2024

@author: lovito99
"""
import numpy as np
import matplotlib.pyplot as plt

# Crear una imagen aleatoria de 10x10
random_image = np.random.randint(0, 256, (10, 10), dtype=np.uint8)

# Visualizar la imagen
plt.imshow(random_image, cmap='gray')
plt.show()
