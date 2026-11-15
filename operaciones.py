"""Funciones matemáticas de la calculadora.

Este módulo solo realiza cálculos. La interacción con el usuario
está en calculadora.py.
"""


def sumar(a, b):
    """Devuelve la suma de a y b."""
    return a + b


def restar(a, b):
    """Devuelve la resta de a menos b."""
    return a - b


def multiplicar(a, b):
    """Devuelve el producto de a por b."""
    return a * b


def dividir(a, b):
    """Devuelve el cociente de a entre b."""
    return a / b


def potencia(base, exponente):
    """Devuelve base elevada a exponente.

    Admite exponentes positivos, negativos y cero.
    """
    if base == 0 and exponente < 0:
        raise ValueError("0 no se puede elevar a un exponente negativo.")
    if base < 0 and not float(exponente).is_integer():
        raise ValueError("Una base negativa solo admite exponentes enteros.")
    try:
        return base ** exponente
    except OverflowError:
        raise ValueError("El resultado es demasiado grande.")


def modulo(a, b):
    """Devuelve el residuo de dividir a entre b."""
    return a % b

