### Efrain Vitorino Marin Cod: **160337**
## Implementación de un Algoritmo para Aplicar Kernels en una Imagen

- **En este ejemplo, implementaremos un algoritmo en Python para aplicar núcleos (kernels) a una imagen. Utilizaremos la librería OpenCV para manejar las imágenes. El algoritmo se puede personalizar para aplicar diferentes tipos de kernels, como enfoque, desenfoque y realce de bordes.**
  - Requisitos Previos
  Antes de comenzar, asegúrate de tener instaladas las librerías ``numpy`` y ``opencv-python`` Puedes instalarlas usando pip:

  ```bash
  pip install numpy opencv-python
  ```
- **instalacion**

 ![instalacion de opencv](instalacion.png)
 #### en caso de no funcionar 😪
 Utilizando **Anaconda**  se proce a realizar las modificaciones 
 - Busca la variable Path en la sección Variables del sistema y edítala.

Agrega las siguientes rutas, si no están ya presentes:
```
C:\Users\lovito99\anaconda3
C:\Users\lovito99\anaconda3\Scripts
C:\Users\lovito99\anaconda3\Library\bin
conda install matplotlib
```
# Explicacion del codigo
- 1. Empesamos con la importacion de los modulos 
 ```
 import cv2
import numpy as np
```
Es el módulo de **OpenCV**, una biblioteca muy popular para el procesamiento de imágenes.
    **numpy:** 
     Es una biblioteca fundamental para el cálculo numérico en Python, utilizada aquí para manejar matrices (o arrays).