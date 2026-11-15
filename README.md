# 🧮 Calculadora en Python

Calculadora de consola con 12 operaciones matemáticas, validación de entradas e historial de operaciones.

## 📋 Descripción

Calculadora de consola escrita en Python. El usuario elige una operación en un menú, escribe los datos y obtiene el resultado. Puede hacer varias operaciones seguidas sin reiniciar el programa y consultar o borrar el historial de lo que calculó.

Su finalidad es practicar la organización de tareas con GitHub Issues, el registro de cambios con Git y la documentación con Markdown.

## ✅ Operaciones y estado

| N.º | Operación | Descripción | Estado |
|---|---|---|---|
| Base | Suma, resta, multiplicación y división | Operaciones básicas entre dos números. | ✅ Completado |
| 1 | Potencia | Base elevada a un exponente. | ✅ Completado |
| 2 | Módulo | Residuo de una división. | ✅ Completado |
| 3 | Raíz cuadrada | Raíz cuadrada de un número no negativo. | ✅ Completado |
| 4 | Porcentaje | Porcentaje de una cantidad (15 % de 200 = 30). | ✅ Completado |
| 5 | Valor absoluto | Valor absoluto de un número. | ✅ Completado |
| 6 | Factorial | Factorial de un entero no negativo. | ✅ Completado |
| 7 | Promedio | Promedio de varios números. | ✅ Completado |
| 8 | Redondeo | Redondeo a la cantidad de decimales indicada. | ✅ Completado |
| 9 | Validación de entradas | Control de entradas no numéricas. | ✅ Completado |
| 10 | División por cero | Evitar divisiones y módulos con divisor cero. | ✅ Completado |
| 11 | Mejorar el menú | Menú claro y organizado por categorías. | ✅ Completado |
| 12 | Repetir operaciones | Varias operaciones sin reiniciar el programa. | ✅ Completado |
| 13 | Historial de operaciones | Guardar y mostrar las operaciones realizadas. | ✅ Completado |
| 14 | Limpiar historial | Borrar el historial de operaciones. | ✅ Completado |
| 15 | Mejorar documentación | Ejemplos de uso y mejor presentación del README. | ✅ Completado |

## 🛠️ Tecnologías

- **Python 3**: lenguaje del programa, sin librerías externas.
- **Git**: control de versiones, con un commit por funcionalidad.
- **GitHub**: repositorio y organización de tareas con Issues.
- **Markdown**: documentación del proyecto.

## 🚀 Instalación y ejecución

Requisito: tener instalado Python 3.8 o superior.

```bash
git clone https://github.com/PXNDX-coder/calculadora.git
cd calculadora
python calculadora.py
```

En algunos sistemas el comando es `python3 calculadora.py`.

## 📁 Estructura del proyecto

```
calculadora/
├── README.md
├── calculadora.py
└── operaciones.py
```

| Archivo | Responsabilidad |
|---|---|
| `calculadora.py` | Muestra el menú, pide los datos, valida las entradas, muestra los resultados, guarda el historial y repite el programa hasta elegir Salir. |
| `operaciones.py` | Contiene las funciones matemáticas y realiza los cálculos. |

## 🖥️ Menú principal

```
==============================================
                 CALCULADORA
==============================================
 Operaciones básicas
   1. Sumar                 2. Restar
   3. Multiplicar           4. Dividir
 Operaciones avanzadas
   5. Potencia              6. Módulo (residuo)
   7. Raíz cuadrada         8. Porcentaje
   9. Valor absoluto       10. Factorial
 Estadística y redondeo
  11. Promedio             12. Redondear
 Historial
  13. Ver historial        14. Limpiar historial
   0. Salir
==============================================
```

## 💡 Ejemplos de uso

**Porcentaje**

```
Elige una opción: 8

--- Porcentaje ---
Porcentaje (%): 15
Cantidad: 200
Resultado: 15 % de 200 = 30
```

**Potencia con exponente negativo**

```
Elige una opción: 5

--- Potencia ---
Base: 2
Exponente: -3
Resultado: 2 ^ -3 = 0.125
```

**Promedio de varios números** (separados por espacios)

```
Elige una opción: 11

--- Promedio ---
Números separados por espacios: 4 8 15 16 23 42
Resultado: promedio(4, 8, 15, 16, 23, 42) = 18
```

**Entrada no numérica**: el programa vuelve a pedir el dato en lugar de fallar. Acepta coma o punto decimal.

```
Elige una opción: 1

--- Sumar ---
Primer número: abc
  Entrada no válida. Escribe un número, por ejemplo 8 o 2.5.
Primer número: 2,5
Segundo número: 4
Resultado: 2.5 + 4 = 6.5
```

**División entre cero y raíz de un negativo**

```
--- Dividir ---
Primer número: 10
Segundo número: 0
Error: No se puede dividir entre cero.

--- Raíz cuadrada ---
Número: -9
Error: No existe la raíz cuadrada real de un número negativo.
```

**Historial**

```
Elige una opción: 13

--- Historial de operaciones ---
  1. 15 % de 200 = 30
  2. 2 ^ -3 = 0.125
  3. 2.5 + 4 = 6.5
  4. promedio(4, 8, 15, 16, 23, 42) = 18
```

Las operaciones con error no se guardan en el historial. La opción 14 lo borra por completo.

## ⚠️ Validaciones

| Caso | Comportamiento |
|---|---|
| Se escribe texto en lugar de un número | Muestra un aviso y vuelve a pedir el dato. |
| División o módulo con divisor 0 | Muestra un error y no realiza la operación. |
| Raíz cuadrada de un número negativo | Muestra un error. |
| Factorial de un negativo o de un decimal | Muestra un error. Admite enteros de 0 a 1000. |
| 0 elevado a un exponente negativo | Muestra un error. |
| Redondeo con decimales negativos o no enteros | Muestra un error. |
| Opción que no está en el menú | Avisa y vuelve a mostrar el menú. |
| Ctrl + C | Termina el programa sin mostrar errores. |

## 👤 Autor

Edilberto
