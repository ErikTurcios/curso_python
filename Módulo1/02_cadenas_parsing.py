"""
Ejercicio 02 — Cadenas: parsear una línea de log
================================================

El Tema 2 enseña el operador [] para acceder a caracteres y rangos (slicing), los
índices negativos, y las funciones len(), find(), upper(), lower(), replace().
Vamos a usarlos para lo que de verdad harás en DevOps/cyber: destripar un log.

Tenemos esta línea de log:

    2026-08-08 11:19:03 ERROR Intento de acceso desde 203.0.113.7

Posiciones (recuerda: se empieza a contar en 0):
    - fecha  -> caracteres 0 a 9
    - hora   -> caracteres 11 a 18
    - el nivel (ERROR) empieza en la posición 20

Objetivos:
  - Extraer trozos con slicing  cadena[inicio:fin].
  - Localizar una subcadena con find() y usar su posición.
  - Normalizar (upper/lower) y enmascarar datos con replace().

Pistas:
  - `linea[0:10]` te da del carácter 0 al 9 (el 10 NO se incluye).
  - `linea.find("desde ")` te da la posición donde empieza "desde ".
    Suma 6 (longitud de "desde ") para saltar hasta la IP.
  - `replace(viejo, nuevo)` NO modifica la original: devuelve una nueva cadena.
"""

LINEA = "2026-08-08 11:19:03 ERROR Intento de acceso desde 203.0.113.7"


def extrae_fecha():
    """Devuelve solo la fecha (los 10 primeros caracteres)."""
    # TODO: usa slicing LINEA[0:10]
    pass


def extrae_hora():
    """Devuelve solo la hora (caracteres 11 a 18)."""
    # TODO: usa slicing
    pass


def extrae_ip():
    """Devuelve la IP, localizándola con find() a partir de 'desde '."""
    # TODO: idx = LINEA.find("desde ") ; luego devuelve LINEA[idx + 6:]
    pass


def enmascara_ip():
    """Devuelve la línea con el último octeto de la IP oculto: 203.0.113.***"""
    # TODO: usa LINEA.replace("203.0.113.7", "203.0.113.***")
    pass


if __name__ == "__main__":
    print("Longitud de la línea:", len(LINEA))
    print("Fecha:", extrae_fecha())
    print("Hora :", extrae_hora())
    print("IP   :", extrae_ip())
    print("Enmascarada:", enmascara_ip())
    print("Últimos 8 caracteres (índice negativo):", LINEA[-8:])
