"""
Ejercicio 04 — Booleanos, comparación e identidad (validaciones)
================================================================

El Tema 2 cubre los operadores lógicos (and, or, not), los de comparación
(< <= > >= == !=) y el tipo None. Vamos a usarlos para validar entradas, que es
la base de cualquier control de seguridad.

IMPORTANTE: aquí NO usamos `if` todavía (eso es de temas posteriores). Solo vamos a
CALCULAR valores booleanos (True/False) y mostrarlos. Una validación, al final, no es
más que una expresión que da True o False.

Objetivos:
  - Construir expresiones booleanas combinando comparaciones con and/or/not.
  - Usar la comparación encadenada de Python (algo que en Java NO puedes hacer).
  - Distinguir `== None` de `is None` (lo correcto es `is None`).

Contraste con Java:
  - En Java escribirías: (1 <= puerto) && (puerto <= 65535)
  - En Python puedes encadenar directamente: 1 <= puerto <= 65535

Pistas:
  - `password.find(" ") != -1` es True si la contraseña CONTIENE un espacio.
  - `not` invierte un booleano.
  - Para saber si algo "no tiene valor", se usa `variable is None`.
"""

PUERTO = 8080
PASSWORD = "SuperSecreta2026"
ENTRADA_USUARIO = None


def puerto_valido():
    """Devuelve True si PUERTO está en el rango válido 1..65535 (comparación encadenada)."""
    # TODO: return 1 <= PUERTO <= 65535
    pass


def password_es_fuerte():
    """Devuelve True si PASSWORD: tiene 12+ caracteres, NO contiene espacios y
    NO es la típica 'password123'. Combina las tres condiciones con and/not."""
    # TODO: longitud_ok = len(PASSWORD) >= 12
    # TODO: sin_espacios = PASSWORD.find(" ") == -1
    # TODO: no_es_comun = PASSWORD != "password123"
    # TODO: return longitud_ok and sin_espacios and no_es_comun
    pass


def falta_entrada():
    """Devuelve True si ENTRADA_USUARIO no tiene valor. Usa `is None`, no `== None`."""
    # TODO: return ENTRADA_USUARIO is None
    pass


if __name__ == "__main__":
    print("¿Puerto válido?:", puerto_valido())
    print("¿Password fuerte?:", password_es_fuerte())
    print("¿Falta la entrada?:", falta_entrada())

    # Diferencia entre valores "falsy" y None:
    print("bool(0) or not(bool()) ->", bool(0) or not (bool()))
