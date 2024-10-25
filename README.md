Aquí tienes un README en español para el repositorio de introducción a la visión por computador:

---

# **Introducción a la Visión por Computador**

Este repositorio contiene el código base para una serie de ejercicios de introducción a la visión por computador. Los estudiantes deberán completar las funciones proporcionadas en el archivo `codigo_estudiante.py`, que abordan operaciones básicas de procesamiento de imágenes, como lectura de imágenes, conversión a arreglos de NumPy y cálculo de estadísticas de los píxeles.

## **Estructura del Repositorio**

- **`codigo_estudiante.py`**: Archivo principal donde los estudiantes deben completar las funciones indicadas. Cada función tiene una descripción de los parámetros de entrada y salida, así como los objetivos de la implementación.
- **`tests/`**: Carpeta que contiene los archivos de pruebas automáticas utilizando el paquete `pytest` para evaluar la correcta implementación de las funciones.
- **`.github/workflows/ci.yml`**: Archivo de configuración de GitHub Actions para ejecutar las pruebas automáticamente cuando los estudiantes suban su código al repositorio.
- **`autograding.json`**: Archivo de configuración para GitHub Classroom, que define las pruebas y los puntajes asignados para la evaluación automática.

## **Descripción de las Funciones a Completar**

1. **`leer_imagen(ruta_imagen)`**:
   - Lee una imagen a partir de la ruta proporcionada y retorna un objeto tipo `Image` de la librería PIL.
   - Parámetro de entrada: `ruta_imagen` (str).
   - Retorna: Objeto imagen de PIL.
   
2. **`obtener_info_imagen(img)`**:
   - Recibe una imagen y retorna el número de canales y las dimensiones.
   - Parámetro de entrada: `img` (objeto tipo `Image` de PIL).
   - Retorna: Tupla con el número de canales y dimensiones (ancho, alto).
   
3. **`imagen_a_arreglo(img)`**:
   - Convierte una imagen de tipo PIL a un arreglo de NumPy.
   - Parámetro de entrada: `img` (objeto tipo `Image` de PIL).
   - Retorna: Arreglo de NumPy con los datos de la imagen.
   
4. **`estadisticas_intensidad(arreglo_img)`**:
   - Calcula el promedio y la desviación estándar de las intensidades de los píxeles en la imagen.
   - Parámetro de entrada: `arreglo_img` (arreglo de NumPy).
   - Retorna: Tupla con el promedio y la desviación estándar de las intensidades.
   
5. **`estadisticas_por_canal(arreglo_img)`**:
   - Calcula el promedio y la desviación estándar de las intensidades por canal.
   - Parámetro de entrada: `arreglo_img` (arreglo de NumPy).
   - Retorna: Diccionario con el promedio y la desviación estándar por canal.

## **Instrucciones**

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone <url-del-repositorio>
   ```
2. Abre el archivo `codigo_estudiante.py` y completa cada una de las funciones según las instrucciones proporcionadas.
3. Para verificar tus soluciones localmente, ejecuta:
   ```bash
   pytest
   ```
4. Una vez que completes todas las funciones, sube los cambios al repositorio para que se realice la evaluación automática en GitHub Classroom.

## **Pruebas Automáticas**

El repositorio está configurado con GitHub Actions para ejecutar pruebas automáticas. Cada vez que subas cambios, se ejecutarán las pruebas correspondientes y se te notificará si alguna de ellas falla. Asegúrate de que todas las pruebas pasen antes de la entrega final.

## **Recursos Adicionales**

- [Documentación de NumPy](https://numpy.org/doc/)
- [Documentación de Pillow (PIL)](https://pillow.readthedocs.io/en/stable/)

---

Este README proporciona una guía clara para los estudiantes sobre el propósito del repositorio y cómo abordar los ejercicios de visión por computador. Si necesitas algún ajuste o más información, házmelo saber.