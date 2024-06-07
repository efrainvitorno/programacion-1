# -*- coding: utf-8 -*-
"""

"""
import numpy as np
import matplotlib.pyplot as plt

#leer la imagen
imagen = plt.imread(r"C:\Users\lovito99\Desktop\Guia 5\practica de graficos\ejersicios\vertical.jpg")/255

#escala de grises
alto,ancho,_=imagen.shape
imagenG=np.zeros((alto,ancho))
for i in range(alto):
    for j in range(ancho):
       pix=(imagen[i,j,0]+imagen[i,j,0]+imagen[i,j,0])/3 
       imagenG[i,j]=pix
       
#escala de grises
alto,ancho,columna=imagen.shape
imagenI=np.zeros((alto,ancho,columna))
for i in range(alto):
    for j in range(ancho):
       imagenI[i,j,0]=1-imagen[i,j,0] 
       imagenI[i,j,1]=1-imagen[i,j,1]  
       imagenI[i,j,2]=1-imagen[i,j,2]  
       
#escala de brillos

imagenB=np.zeros((alto,ancho,columna))
for i in range(alto):
    for j in range(ancho):
        imagenB[i,j]=imagen[i,j]-0.5
#mostrar la imagen
plt.imshow(imagenB,cmap="gray")
plt.axis("off")