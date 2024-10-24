import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_imagen_a_arreglo():
    from codigo_estudiante import leer_imagen, imagen_a_arreglo
    ruta_imagen = os.path.join("data","imagen0.png")
    img = leer_imagen(ruta_imagen)
    arreglo_img = imagen_a_arreglo(img)
    assert arreglo_img.shape[2] == 3