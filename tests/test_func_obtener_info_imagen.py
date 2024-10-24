import sys
import os
from PIL import Image
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_obtener_info_imagen():
    from codigo_estudiante import obtener_info_imagen
    ruta_imagen = os.path.join("data","imagen0.png")
    img = Image.open(ruta_imagen)
    num_canales, _ = obtener_info_imagen(img)
    assert num_canales == 3