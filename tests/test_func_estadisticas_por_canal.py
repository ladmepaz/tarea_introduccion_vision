import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_estadisticas_por_canal():
    from codigo_estudiante import estadisticas_intensidad
    ruta_imagen = os.path.join("data","imagen0.png")
    img = Image.open(ruta_imagen)
    arreglo_img = np.array(img)
    resultados = estadisticas_por_canal(arreglo_img)
    assert int(resultados['Canal_1']['Promedio']) == 115