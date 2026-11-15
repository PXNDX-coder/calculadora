"""Funciones matemáticas de la calculadora.

Este módulo solo realiza cálculos. La interacción con el usuario
está en calculadora.py.
"""
import math

from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

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
    """Devuelve el cociente de a entre b. No permite dividir entre cero."""
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero.")
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
    """Devuelve el residuo de dividir a entre b. El divisor no puede ser cero."""
    if b == 0:
        raise ZeroDivisionError("No se puede calcular el módulo con divisor cero.")
    return a % b


def raiz_cuadrada(numero):
    """Devuelve la raíz cuadrada de un número no negativo."""
    if numero < 0:
        raise ValueError("No existe la raíz cuadrada real de un número negativo.")
    return math.sqrt(numero)


def porcentaje(porcentaje_valor, cantidad):
    """Devuelve el porcentaje indicado de una cantidad.

    Ejemplo: porcentaje(15, 200) devuelve 30.
    """
    return cantidad * porcentaje_valor / 100


def valor_absoluto(numero):
    """Devuelve el valor absoluto de un número."""
    return abs(numero)


def factorial(n):
    """Devuelve el factorial de un entero no negativo."""
    if n < 0 or not float(n).is_integer():
        raise ValueError("El factorial solo se calcula para enteros no negativos.")
    if n > 1000:
        raise ValueError("El número es demasiado grande (máximo 1000).")
    return math.factorial(int(n))


def promedio(numeros):
    """Devuelve el promedio de una lista de números."""
    if len(numeros) == 0:
        raise ValueError("Se necesita al menos un número para calcular el promedio.")
    return sum(numeros) / len(numeros)


def redondear(numero, decimales):
    """Redondea un número a la cantidad de decimales indicada.

    Usa el redondeo escolar: 2.5 se redondea a 3 y 2.675 a 2.68.
    """
    if decimales < 0 or not float(decimales).is_integer():
        raise ValueError("Los decimales deben ser un entero mayor o igual a 0.")
    paso = Decimal(1).scaleb(-int(decimales))
    try:
        return float(Decimal(str(numero)).quantize(paso, rounding=ROUND_HALF_UP))
    except InvalidOperation:
        raise ValueError("El número tiene demasiadas cifras para redondearlo así.")


