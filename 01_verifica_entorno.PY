"""
Ejercicio 01 — Verifica tu entorno
==================================

El Tema 1 insiste en comprobar la instalación con `python --version`. Vamos a hacer
lo mismo, pero desde código, que es como se comprueba un entorno en un pipeline real.

Objetivos:
  - Ejecutar tu primer script de Python.
  - Usar el módulo `sys` para inspeccionar el intérprete.
  - Manejar imports que pueden fallar con try/except.

Contraste con Java: aquí no compilas nada. Guardas el .py y lo ejecutas directamente
con `python 01_verifica_entorno.py`. No hay `javac`, no hay .class.

Pistas:
  - `sys.version` -> cadena con la versión completa.
  - `sys.version_info` -> tupla (major, minor, micro). Compara con (3, 8).
  - `sys.executable` -> ruta del python que está ejecutando el script.
  - Para saber si una librería está instalada, intenta importarla y captura ImportError.
"""

import sys


def info_interprete():
    """Imprime versión y ruta del intérprete de Python."""
    # TODO: imprime sys.version
    # TODO: imprime sys.executable
    pass


def cumple_version_minima(major=3, minor=8):
    """Devuelve True si la versión de Python es >= (major, minor)."""
    # TODO: compara sys.version_info[:2] con (major, minor) y devuelve el booleano
    pass


def libreria_disponible(nombre):
    """Devuelve True si la librería `nombre` se puede importar, False si no."""
    # TODO: usa un try/except con __import__(nombre) y captura ImportError
    pass


if __name__ == "__main__":
    info_interprete()
    print("¿Cumple 3.8+?:", cumple_version_minima())
    for lib in ("numpy", "pandas", "estemodulonoexiste"):
        print(f"{lib}: {'disponible' if libreria_disponible(lib) else 'NO instalada'}")