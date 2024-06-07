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

# Visualizar la imagen
plt.imshow(image)
plt.show()
