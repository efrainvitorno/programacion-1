"""
Created on Fri Jun  7 02:46:19 2024

@author: lovito99
"""
from skimage import io
import numpy as np
import matplotlib.pyplot as plt

def ImagenVolteada(image):
    # Girar la imagen 90 grados en sentido antihorario
    Rotarimagen = np.rot90(image)
    # Reflejar la imagen verticalmente
    return np.flipud(Rotarimagen)

# Leer una imagen a color
Imagen = io.imread(r'C:\Users\lovito99\Desktop\Guia 5\practica de graficos\ejersicios\vertical.jpg')

# Voltear la imagen horizontalmente
Volteada = ImagenVolteada(Imagen)

# Visualizar la imagen original y la imagen volteada horizontalmente
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(Imagen)
axes[0].set_title('Imagen Original')
axes[1].imshow(Volteada)
axes[1].set_title('Imagen Volteada Horizontalmente')
plt.show()
