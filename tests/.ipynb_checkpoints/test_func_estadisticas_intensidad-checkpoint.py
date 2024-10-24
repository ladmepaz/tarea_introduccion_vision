import sys
import os
import numpy as np
from PIL import Image

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_estadisticas_intensidad():
    from codigo_estudiante import estadisticas_intensidad
    ruta_imagen = os.path.join("data","imagen0.png")
    img = Image.open(ruta_imagen)
    arreglo_img = np.array(img)
    promedio, _ = estadisticas_intensidad(arreglo_img)
    assert int(promedio) == 144