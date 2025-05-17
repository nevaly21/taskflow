# test_main.py

from src.main import ejecutar_taskflow

def test_funciona_taskflow():
    assert ejecutar_taskflow() is None  # Solo imprime en consola, sin retorno
