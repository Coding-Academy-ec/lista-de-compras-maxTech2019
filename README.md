# Asignación de la Lista de Compras

Este repositorio contiene una asignación para el curso de programación en Python. La asignación es sobre la manipulación de listas y tuplas en Python.

## Descripción de la Asignación

El archivo `ejercicio.py` contiene un script que pide al usuario que ingrese una lista de compras. El usuario debe ingresar los elementos de la lista separados por comas. El script luego imprime la lista de compras.

Además, el script contiene una función llamada `convertir_lista_a_tupla()` que está destinada a convertir la lista de compras en una tupla. Esta función aún no está completa.

## Tareas Pendientes

- Completar la función `convertir_lista_a_tupla()` para que convierta la lista de compras en una tupla.

## Cómo Ejecutar el Código

Para ejecutar el test puedes utilizar el siguiente comando en tu terminal:

```bash
pytest -s
```

Pytest es una biblioteca que facilita la escritura de pruebas en Python. El parámetro `-s` se utiliza para mostrar la salida de la prueba en la terminal.

Ejemplo de salida:

```bash
$ pytest -s
================================================= test session starts =================================================
platform linux -- Python 3.8.10, pytest-6.2.4, pluggy-0.13.1
rootdir: /home/user/Documentos/Python/Asignacion_Lista_Compras
collected 1 item

test_ejercicio.py Lista de Compras: [manzanas, peras, plátanos, uvas]

================================================== 1 passed in 0.01s ==================================================
```