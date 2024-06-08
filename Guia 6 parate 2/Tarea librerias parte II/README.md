### Efrain Vitorino Marin Cod: **160337**
## Implementación de un Algoritmo para Aplicar Kernels en una Imagen

- **En este ejemplo, implementaremos un algoritmo en Python para aplicar núcleos (kernels) a una imagen. Utilizaremos la librería OpenCV para manejar las imágenes. El algoritmo se puede personalizar para aplicar diferentes tipos de kernels, como enfoque, desenfoque y realce de bordes.**
-  ### ¿Qué es un Kernel?:
   * Un kernel es una matriz pequeña (generalmente de tamaño 3x3, 5x5, etc.) que se utiliza para transformar una imagen mediante una operación llamada convolución. En el contexto de imágenes, un kernel se mueve a través de cada píxel de la imagen y realiza operaciones basadas en los valores de los píxeles dentro de su vecindad definida por el tamaño del kernel.
 * Aplicación:
Este kernel aplica una fuerte ponderación positiva al píxel central y ponderaciones negativas a sus vecinos inmediatos, lo que resulta en una imagen más nítida.
* Conclucion:
Mejora la nitidez de la imagen y realza los bordes.

---------------
Visualización:

Supongamos que aplicamos este kernel a una imagen:


Imagen Original: La imagen tal cual se carga.
Imagen Procesada: Después de aplicar el kernel de enfoque, los bordes y detalles se vuelven más prominentes.

## Ejemplo 
imagen de ejemplo
```
1 2 3
4 5 6
7 8 9
```
Kernel de Enfoque 3x3
```  
 0 -1  0
-1  5 -1
 0 -1  0
 ```
* Multiplicamos cada valor del kernel por el valor correspondiente del píxel:
```
 0*1 + (-1)*2 +  0*3 +
(-1)*4 +  5*5 + (-1)*6 +
 0*7 + (-1)*8 +  0*9
```
 _______________________
  - Requisitos Previos
  #### Antes de comenzar, asegúrate de tener instaladas las librerías ``numpy`` y ``opencv-python`` Puedes instalarlas usando pip:

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
# Explicacion del codigo 🖥️
- **1. Empesamos con la importacion de los modulos**
 ```
 import cv2
import numpy as np
```
Es el módulo de **OpenCV**, una biblioteca muy popular para el procesamiento de imágenes.
- **numpy:** 
     #Es una biblioteca fundamental para el cálculo numérico en Python, utilizada aquí para manejar matrices (o arrays).
- **2.**  **Definición de la Función AplicarKernel**
Esta función toma como entrada la ruta de una imagen (imagen_path) y un filtro de procesamiento (o kernel) (kernel).

``` python
def AplicarKernel(imagen_path, kernel):
```
- **3.** **Cargar la Imagen en Escala de Grises:**
  - `cv2.imread`: Carga la imagen desde la ruta especificada.
  - `cv2.IMREAD_GRAYSCALE`: Lee la imagen en modo escala de grises.
```
  imagen = cv2.imread(imagen_path, cv2.IMREAD_GRAYSCALE)
```

