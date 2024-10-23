# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 17:00:25 2024

@author: jfrui
"""

# Completa las funciones de abajo

# Ejercicio 1: Completa la función de abajo de acuerdo a la descripción de los parámetros de entrada y salida

from PIL import Image

def obtener_info_imagen(ruta_imagen):
    """
    Lee una imagen y retorna el número de canales y las dimensiones.
    
    Parámetros:
    ruta_imagen (str): Ruta de la imagen a leer.
    
    Retorna:
    tuple: (num_canales, dimensiones) donde:
        - num_canales es el número de canales (1 para escala de grises, 3 para RGB, 4 para RGBA)
        - dimensiones es una tupla con las dimensiones (ancho, alto) de la imagen
    """
    # Abrir la imagen
    imagen = Image.open(ruta_imagen)
    
    # Obtener el número de canales
    modo = imagen.mode
    if modo == 'L':  # Escala de grises
        num_canales = 1 # Ingresa valor aquí
    elif modo == 'RGB':  # Imagen RGB
        num_canales = 3 # Ingresa valor aquí
    elif modo == 'RGBA':  # Imagen RGBA
        num_canales = 4 # Ingresa valor aquí
    else:
        num_canales = len(modo)  # Otros modos de imagen
    
    # Obtener las dimensiones de la imagen
    dimensiones = imagen.size  # Ingresa valor aquí para obtener (ancho, alto)
    
    return num_canales, dimensiones
