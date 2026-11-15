"""Calculadora por consola.

Muestra el menú, solicita los datos y muestra los resultados.
Los cálculos se realizan en operaciones.py.
"""
import math

import operaciones as op


def convertir_numero(texto):
    """Convierte un texto en número. Devuelve None si no es un número válido.

    Acepta coma o punto decimal (2,5 o 2.5) y rechaza inf y nan.
    """
    try:
        numero = float(texto.strip().replace(",", "."))
    except ValueError:
        return None
    if math.isinf(numero) or math.isnan(numero):
        return None
    return numero


def pedir_numero(mensaje):
    """Pide un número hasta que el usuario escriba un valor válido."""
    while True:
        numero = convertir_numero(input(mensaje))
        if numero is not None:
            return numero
        print("  Entrada no válida. Escribe un número, por ejemplo 8 o 2.5.")


def pedir_lista(mensaje):
    """Pide varios números separados por espacios hasta que todos sean válidos."""
    while True:
        partes = input(mensaje).split()
        numeros = [convertir_numero(parte) for parte in partes]
        if not partes:
            print("  Escribe al menos un número.")
        elif None in numeros:
            print("  Hay valores que no son números. Ejemplo válido: 4 8 15.5")
        else:
            return numeros


def formatear(numero):
    """Muestra 5.0 como 5 y deja los demás números como están."""
    if isinstance(numero, float) and numero.is_integer() and abs(numero) < 1e15:
        return str(int(numero))
    return str(numero)


def pedir_dos_numeros():
    """Pide los dos números de una operación básica."""
    a = pedir_numero("Primer número: ")
    b = pedir_numero("Segundo número: ")
    return a, b


def calcular_suma():
    a, b = pedir_dos_numeros()
    return f"{formatear(a)} + {formatear(b)}", op.sumar(a, b)


def calcular_resta():
    a, b = pedir_dos_numeros()
    return f"{formatear(a)} - {formatear(b)}", op.restar(a, b)


def calcular_multiplicacion():
    a, b = pedir_dos_numeros()
    return f"{formatear(a)} × {formatear(b)}", op.multiplicar(a, b)


def calcular_division():
    a, b = pedir_dos_numeros()
    return f"{formatear(a)} ÷ {formatear(b)}", op.dividir(a, b)


def calcular_potencia():
    base = pedir_numero("Base: ")
    exponente = pedir_numero("Exponente: ")
    return f"{formatear(base)} ^ {formatear(exponente)}", op.potencia(base, exponente)


def calcular_modulo():
    a = pedir_numero("Dividendo: ")
    b = pedir_numero("Divisor: ")
    return f"{formatear(a)} mod {formatear(b)}", op.modulo(a, b)


def calcular_raiz():
    numero = pedir_numero("Número: ")
    return f"√{formatear(numero)}", op.raiz_cuadrada(numero)


def calcular_porcentaje():
    porcentaje_valor = pedir_numero("Porcentaje (%): ")
    cantidad = pedir_numero("Cantidad: ")
    return (
        f"{formatear(porcentaje_valor)} % de {formatear(cantidad)}",
        op.porcentaje(porcentaje_valor, cantidad),
    )


def calcular_absoluto():
    numero = pedir_numero("Número: ")
    return f"|{formatear(numero)}|", op.valor_absoluto(numero)


def calcular_factorial():
    n = pedir_numero("Número entero no negativo: ")
    return f"{formatear(n)}!", op.factorial(n)


def calcular_promedio():
    numeros = pedir_lista("Números separados por espacios: ")
    lista = ", ".join(formatear(n) for n in numeros)
    return f"promedio({lista})", op.promedio(numeros)


def calcular_redondeo():
    numero = pedir_numero("Número a redondear: ")
    decimales = pedir_numero("Cantidad de decimales: ")
    return (
        f"redondear({formatear(numero)}, {formatear(decimales)})",
        op.redondear(numero, decimales),
    )


# Opción del menú -> (nombre, función que pide los datos y calcula)
OPCIONES = {
    "1": ("Sumar", calcular_suma),
    "2": ("Restar", calcular_resta),
    "3": ("Multiplicar", calcular_multiplicacion),
    "4": ("Dividir", calcular_division),
    "5": ("Potencia", calcular_potencia),
    "6": ("Módulo (residuo)", calcular_modulo),
    "7": ("Raíz cuadrada", calcular_raiz),
    "8": ("Porcentaje", calcular_porcentaje),
    "9": ("Valor absoluto", calcular_absoluto),
    "10": ("Factorial", calcular_factorial),
    "11": ("Promedio", calcular_promedio),
    "12": ("Redondear", calcular_redondeo),
}


def mostrar_menu():
    """Muestra las operaciones disponibles."""
    print("\n=== CALCULADORA ===")
    for clave, (nombre, _) in OPCIONES.items():
        print(f"{clave}. {nombre}")


def main():
    mostrar_menu()
    opcion = input("\nElige una opción: ").strip()

    if opcion not in OPCIONES:
        print("Opción no válida.")
        return

    _, calcular = OPCIONES[opcion]
    try:
        expresion, resultado = calcular()
        print(f"Resultado: {expresion} = {formatear(resultado)}")
    except (ValueError, ZeroDivisionError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()