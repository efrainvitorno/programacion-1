# Trabajo de bonificacion 
## Nombre: Efrain Vitorino marin Codigo: 160337
- # 👀 Implementar los siguientes filtros📷 
  * Modificando los valores de los canales de cada pixel y si es necesario
redondear los valores resultantes aplicar la siguiente fórmula
 * condicion

     ![condicion](Ejfiltr.png)
- **introduccion**  para el caso **(A)**
      - El filtro sepia convierte una imagen de color a tonos sepia, que son tonos marrones claros que imitan las fotografías antiguas. Este filtro se logra mediante una transformación lineal de los valores de los canales de color **(rojo, verde y azul)**.
     * Las fórmulas para convertir un píxel de RGB a sepia son
       ```
       R' = 0.393 * R + 0.769 * G + 0.189 * B
       G' = 0.349 * R + 0.686 * G + 0.168 * B
       B' = 0.272 * R + 0.534 * G + 0.131 * B
    
       ```
     * R,G,B son los valores originales de los canales rojo, verde y azul.
     * 𝑅′,𝐺′,𝐵′ son los nuevos valores de estos canales, después de aplicar el filtro.
     * Esta transformación asegura que los tonos de la imagen se ajusten para obtener el efecto sepia, que es característico de las fotografías antiguas.
- Fundamento
<p> El filtro sepia se basa en una transformación lineal que combina los canales de color de una manera específica para lograr una apariencia vintage. La transformación se aplica a cada píxel individualmente. <p>

### Ejemplo:
Si un píxel tiene los valores R = 100, G = 150, B = 200, los nuevos valores después de aplicar el filtro sepia serían:
   ```
   R' = 0.393 * 100 + 0.769 * 150 + 0.189 * 200 = 173.85
   G' = 0.349 * 100 + 0.686 * 150 + 0.168 * 200 = 154.7
   B' = 0.272 * 100 + 0.534 * 150 + 0.131 * 200 = 120.9
   ```
   Estos valores se redondean y se limitan al rango de 0 a 255.
   ## Código Aplicado:
   **python**
   ```python
   def aplicar_filtro_sepia(imagen_np):
    sepia = np.copy(imagen_np)
    for i in range(imagen_np.shape[0]):
        for j in range(imagen_np.shape[1]):
            rojo = imagen_np[i, j, 0]
            verde = imagen_np[i, j, 1]
            azul = imagen_np[i, j, 2]
            
            sepia[i, j, 0] = min(255, 0.393 * rojo + 0.769 * verde + 0.189 * azul)
            sepia[i, j, 1] = min(255, 0.349 * rojo + 0.686 * verde + 0.168 * azul)
            sepia[i, j, 2] = min(255, 0.272 * rojo + 0.534 * verde + 0.131 * azul)
    
    return sepia
```

