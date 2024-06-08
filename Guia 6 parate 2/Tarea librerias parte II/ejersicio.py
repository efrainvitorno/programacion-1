import cv2  # Importa la librería OpenCV para procesamiento de imágenes
import numpy as np  # Importa NumPy para operaciones matemáticas y manejo de matrices
import matplotlib.pyplot as plt  # Importa Matplotlib para la visualización de imágenes

# Cargar la imagen en escala de grises
# Esta línea carga la imagen desde el disco en modo de escala de grises.
# La ruta especifica la ubicación de la imagen en tu sistema.
imagen_path = 'C:/Users/lovito99/Desktop/Guia 5/practica de graficos/ejersicios/vertical.jpg'
imagen = cv2.imread(imagen_path, cv2.IMREAD_GRAYSCALE)

# Definir los kernels
# Los kernels son matrices que se usan para aplicar diferentes filtros en la imagen.

# Kernel para enfoque: resalta los detalles y hace que los bordes sean más nítidos.
kernelEnfoque = np.array([[ 0, -1,  0], 
                          [-1,  5, -1], 
                          [ 0, -1,  0]])

# Kernel para suavizado (promedio): reduce el ruido al promediar los valores de los píxeles vecinos.
kernelSuavizado = np.ones((3, 3), np.float32) / 9

# Kernel para detección de bordes: resalta los bordes detectando cambios significativos en la intensidad de los píxeles.
kernelBordes = np.array([[-1, -1, -1], 
                         [-1,  8, -1], 
                         [-1, -1, -1]])

# Aplicar los kernels
# Usamos la función cv2.filter2D para aplicar los kernels a la imagen original.

# Aplicar el kernel de enfoque para resaltar detalles.
imagenEnfocada = cv2.filter2D(imagen, -1, kernelEnfoque)

# Aplicar el kernel de suavizado para reducir el ruido.
imagenSuavizada = cv2.filter2D(imagen, -1, kernelSuavizado)

# Aplicar el kernel de detección de bordes para resaltar los contornos.
imagenBordes = cv2.filter2D(imagen, -1, kernelBordes)

# Mostrar los resultados
# Usamos Matplotlib para mostrar la imagen original y las imágenes procesadas con los diferentes kernels.

plt.figure(figsize=(12, 6))  # Define el tamaño de la figura para la visualización

# Mostrar la imagen original
plt.subplot(2, 2, 1)  # Añade una subtrama en la posición 1 del layout 2x2
plt.imshow(imagen, cmap='gray')  # Muestra la imagen en escala de grises
plt.title('Imagen Original')  # Título de la subtrama
plt.axis('off')  # Desactiva los ejes para una visualización más clara

# Mostrar la imagen después de aplicar el kernel de enfoque
plt.subplot(2, 2, 2)  # Añade una subtrama en la posición 2 del layout 2x2
plt.imshow(imagenEnfocada, cmap='gray')  # Muestra la imagen enfocada
plt.title('Imagen Enfocada')  # Título de la subtrama
plt.axis('off')  # Desactiva los ejes

# Mostrar la imagen después de aplicar el kernel de suavizado
plt.subplot(2, 2, 3)  # Añade una subtrama en la posición 3 del layout 2x2
plt.imshow(imagenSuavizada, cmap='gray')  # Muestra la imagen suavizada
plt.title('Imagen Suavizada')  # Título de la subtrama
plt.axis('off')  # Desactiva los ejes

# Mostrar la imagen después de aplicar el kernel de detección de bordes
plt.subplot(2, 2, 4)  # Añade una subtrama en la posición 4 del layout 2x2
plt.imshow(imagenBordes, cmap='gray')  # Muestra la imagen con bordes detectados
plt.title('Detección de Bordes')  # Título de la subtrama
plt.axis('off')  # Desactiva los ejes

# Muestra todas las subtramas en la figura
plt.show()
