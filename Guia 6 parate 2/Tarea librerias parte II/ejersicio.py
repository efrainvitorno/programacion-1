# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 15:08:27 2024

@author: lovito99
"""

import cv2
import numpy as np

def aplicar_kernel(imagen_path, kernel):
    # Cargar la imagen en escala de grises
    imagen = cv2.imread(imagen_path, cv2.IMREAD_GRAYSCALE)
    
    # Verificar si la imagen se cargó correctamente
    if imagen is None:
        print(f"Error al cargar la imagen: {imagen_path}")
        return
    
    # Aplicar el kernel a la imagen
    imagen_procesada = cv2.filter2D(imagen, -1, kernel)
    
    # Mostrar la imagen original y la imagen procesada
    cv2.imshow('Imagen Original', imagen)
    cv2.imshow('Imagen Procesada', imagen_procesada)
    
    # Guardar la imagen procesada
    cv2.imwrite('imagen_procesada.png', imagen_procesada)
    
    # Esperar a que se presione una tecla y luego cerrar las ventanas
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Definir un núcleo de ejemplo (enfoque 3x3)
kernel_enfoque = np.array([[0, -1, 0], 
                           [-1, 5, -1], 
                           [0, -1, 0]])

# Ruta de la imagen a procesar
ruta_imagen = r'C:\Users\lovito99\Desktop\Guia 5\practica de graficos\ejersicios\vertical.jpg'

# Aplicar el kernel a la imagen
aplicar_kernel(ruta_imagen, kernel_enfoque)
