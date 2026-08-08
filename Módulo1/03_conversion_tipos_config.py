"""
Ejercicio 03 — Conversión de tipos y None (leyendo "configuración")
===================================================================

El Tema 2 cubre str(), int(), float(), bool(), el tipo None y las conversiones.
Esto es EL pan de cada día en DevOps: las variables de entorno SIEMPRE llegan como
cadenas de texto, y hay que convertirlas al tipo correcto. Aquí las simulamos.

Objetivos:
  - Convertir cadenas a int y float.
  - Entender una trampa clásica de bool() con cadenas.
  - Usar None como "valor no definido" y darle un valor por defecto con `or`.

  ⚠️ TRAMPA IMPORTANTE (esto ha causado bugs reales en producción):
     bool("False") NO es False. Es True, porque cualquier cadena NO vacía es True.
     Por eso, para leer un booleano de texto, se compara: DEBUG.lower() == "true".

Pistas:
  - `int("8080")` -> 8080  ;  `float("0.75")` -> 0.75
  - `None or 30` -> 30  (None es "falsy", así que se queda con el segundo valor).
  - Concatenar texto con un número requiere str(numero) primero.
"""

# Simulamos variables de entorno: TODAS llegan como cadenas (o None si no existen)
ENV_PORT = "8080"
ENV_RATIO = "0.75"
ENV_DEBUG = "false"
ENV_TIMEOUT = None  # esta no está definida


def puerto_como_int():
    """Devuelve ENV_PORT convertido a entero."""
    # TODO: int(ENV_PORT)
    pass


def ratio_como_float():
    """Devuelve ENV_RATIO convertido a float."""
    # TODO: float(ENV_RATIO)
    pass


def debug_correcto():
    """Devuelve el booleano REAL de ENV_DEBUG, evitando la trampa de bool().
    Para 'false' debe devolver False."""
    # TODO: compara ENV_DEBUG.lower() con "true" y devuelve el booleano
    pass


def timeout_con_defecto():
    """Devuelve ENV_TIMEOUT si está definido; si es None, devuelve 30 por defecto."""
    # TODO: usa el operador `or`  ->  ENV_TIMEOUT or 30
    pass


if __name__ == "__main__":
    print("La trampa -> bool('false') =", bool("false"), "(¡ojo, es True!)")
    print("None == False ->", None == False, "(son cosas distintas)")

    puerto = puerto_como_int()
    print("Puerto (int):", puerto, "->", type(puerto).__name__)
    print("Ratio (float):", ratio_como_float())
    print("Debug real:", debug_correcto())
    print("Timeout efectivo:", timeout_con_defecto())

    # str() para poder concatenar número con texto:
    print("Mensaje: escuchando en el puerto " + str(puerto))
