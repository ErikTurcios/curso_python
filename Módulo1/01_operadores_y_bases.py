"""
Ejercicio 01 — Operadores, bases numéricas y bits (con sabor a permisos Unix)
=============================================================================

El Tema 2 cubre los operadores aritméticos (+ - * / // % **), los literales en
binario/hexadecimal y los operadores de bits (& | ^ << >>). En vez de sumar peras,
los vas a usar como se usan en la vida real de un DevOps.

Objetivos:
  - Distinguir división normal (/) de división entera (//) y módulo (%).
  - Escribir enteros en binario (0b...) y hexadecimal (0x...) y convertir con bin()/hex().
  - Usar operadores de bits para manejar FLAGS de permisos, igual que hace `chmod`.

Contexto: los permisos de un fichero en Linux (rwx) son 3 bits:
    lectura (r) = 4   ->  0b100
    escritura (w) = 2 ->  0b010
    ejecución (x) = 1 ->  0b001
Se combinan sumando/OR: rw- = 4|2 = 6 ;  rwx = 7 ;  r-x = 5.  (De ahí el famoso 755.)

Pistas:
  - `a // b` -> parte entera ; `a % b` -> resto.
  - `bin(n)` y `hex(n)` devuelven la representación como cadena.
  - Para saber si un flag está activo: `bool(permisos & FLAG)`.
"""

# Constantes de permisos (en MAYÚSCULAS, como enseña el tema para las "constantes")
LECTURA = 4
ESCRITURA = 2
EJECUCION = 1


def parte_a_aritmetica():
    """Un fichero ocupa 5500 bytes. Calcula cuántos KiB ENTEROS son (1 KiB = 1024 B)
    y cuántos bytes sobran. Devuelve la tupla (kib_enteros, bytes_restantes)."""
    total_bytes = 5500
    # TODO: kib_enteros con //  y  bytes_restantes con %
    # TODO: devuelve (kib_enteros, bytes_restantes)
    pass


def parte_b_bases():
    """El octeto 192 de una IP. Comprueba que 192 se puede escribir en decimal,
    binario y hexadecimal y que son EL MISMO número. Imprime sus representaciones."""
    decimal = 192
    # TODO: imprime bin(decimal) y hex(decimal)
    # TODO: comprueba e imprime si  decimal == 0b11000000 == 0xC0
    pass


def parte_c_permisos():
    """Construye el permiso 'rw-' combinando flags con OR (|) y comprueba con AND (&)
    qué se puede hacer. Devuelve la tupla (puede_leer, puede_escribir, puede_ejecutar)."""
    permisos = LECTURA | ESCRITURA  # rw-
    # TODO: puede_leer = bool(permisos & LECTURA)
    # TODO: idem para escritura y ejecución
    # TODO: devuelve la tupla de tres booleanos
    pass


if __name__ == "__main__":
    print("A) 5500 bytes ->", parte_a_aritmetica(), "(KiB, resto)")
    parte_b_bases()
    print("C) permisos rw- (leer, escribir, ejecutar):", parte_c_permisos())
