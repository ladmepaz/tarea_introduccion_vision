import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_leer_imagen():
    from codigo_estudiante import leer_imagen
    ruta_imagen = os.path.join("data","imagen0.png")
    img = leer_imagen(ruta_imagen)
    assert img.size[0] == 1024