# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 17:00:25 2024

@author: jfrui
"""

# Completa las funciones de abajo

# Ejercicio 1: Completa la función de abajo de acuerdo a la descripción de los parámetros de entrada y salida

import numpy as np
from PIL import Image

def leer_imagen(ruta_imagen):
    """
    Lee una imagen a partir de una ruta y retorna el objeto imagen usando la librería PIL.
    
    Parámetros:
    ruta_imagen (str): Ruta de la imagen a leer.
    
    Retorna:
    img: objeto tipo Image de PIL
    """
    # Abrir la imagen
    img = Image.open(ruta_imagen)
        
    return img

def obtener_info_imagen(img):
    """
    Recibe una imagen y retorna el número de canales y las dimensiones.
    
    Parámetros:
    img: objeto tipo Image de PIL
    
    Retorna:
    tuple: (num_canales, dimensiones) donde:
        - num_canales es el número de canales (1 para escala de grises, 3 para RGB, 4 para RGBA)
        - dimensiones es una tupla con las dimensiones (ancho, alto) de la imagen
    """
    
    # Obtener el número de canales
    modo = img.mode
    if modo == 'L':  # Escala de grises
        num_canales = 1 # Ingresa valor aquí
    elif modo == 'RGB':  # Imagen RGB
        num_canales = 3 # Ingresa valor aquí
    elif modo == 'RGBA':  # Imagen RGBA
        num_canales = 4 # Ingresa valor aquí
    else:
        num_canales = len(modo)  # Otros modos de imagen
    
    # Obtener las dimensiones de la imagen
    dimensiones = img.size  # Ingresa valor aquí para obtener (ancho, alto)
    
    return num_canales, dimensiones

def imagen_a_arreglo(img):
    """
    Convierte una imagen de tipo PIL a un arreglo de NumPy.
    
    Parámetros:
    img (PIL.Image): Imagen a convertir.
    
    Retorna:
    np.ndarray: Arreglo de NumPy con los datos de la imagen.
    """
    # Convertir la imagen a un arreglo de NumPy
    arreglo = np.array(img)
    return arreglo

def estadisticas_intensidad(arreglo_img):
    """
    Calcula el promedio y la desviación estándar de las intensidades de los píxeles
    en una imagen representada como un arreglo de NumPy.
    
    Parámetros:
    arreglo_img (np.ndarray): Imagen representada como arreglo de NumPy.
    
    Retorna:
    tuple: (promedio, desviación_estándar) de las intensidades de los píxeles.
    """
    # Calcular el promedio y la desviación estándar
    promedio = np.mean(arreglo_img)
    desviacion_estandar = np.std(arreglo_img)
    
    return promedio, desviacion_estandar

def estadisticas_por_canal(arreglo_img):
    """
    Calcula el promedio y la desviación estándar de las intensidades por canal
    en una imagen representada como un arreglo de NumPy.
    
    Parámetros:
    arreglo_img (np.ndarray): Imagen representada como un arreglo de NumPy, con forma (alto, ancho, canales).
    
    Retorna:
    dict: Diccionario con el promedio y la desviación estándar por canal.
    """
    # Verificar que la imagen tenga al menos un canal
    if len(arreglo_img.shape) < 3:
        raise ValueError("La imagen debe tener al menos un canal para calcular estadísticas por canal.")
    
    # Inicializar el diccionario para almacenar los resultados por canal
    resultados = {}
    num_canales = arreglo_img.shape[2]
    
    # Calcular el promedio y la desviación estándar por canal
    for canal in range(num_canales):
        promedio = np.mean(arreglo_img[:, :, canal])
        desviacion_estandar = np.std(arreglo_img[:, :, canal])
        resultados[f'Canal_{canal+1}'] = {
            'Promedio': promedio,
            'Desviación Estándar': desviacion_estandar
        }
    
    return resultados