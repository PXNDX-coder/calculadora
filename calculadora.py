"""Calculadora por consola.

Muestra el menú, solicita los datos y muestra los resultados.
Los cálculos se realizan en operaciones.py.
"""

import operaciones as op


def pedir_numero(mensaje):
    """Pide un número al usuario."""
    return float(input(mensaje))


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


# Opción del menú -> (nombre, función que pide los datos y calcula)
OPCIONES = {
    "1": ("Sumar", calcular_suma),
    "2": ("Restar", calcular_resta),
    "3": ("Multiplicar", calcular_multiplicacion),
    "4": ("Dividir", calcular_division),
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
    expresion, resultado = calcular()
    print(f"Resultado: {expresion} = {formatear(resultado)}")


if __name__ == "__main__":
    main()