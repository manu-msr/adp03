[`Análisis de Datos con Python`](../../README.md) > [`Sesión 1`](../README.md) > `Ejemplo 2`

## Ejemplo 2: Procedimientos

### 1. Objetivos :dart:

- Mostrar cómo operan los procedimientos como bloques que solucionan un problema específico.

### 2. Requisitos :clipboard:

1. Python 3 instalado.

### 3. Desarrollo :rocket:

A continuación se muestra el siguiente *script*. Ejecútalo y analiza el código en un editor de textos.

[`ejemplo2.py`](codigos/ejemplo2.py)
```python
def prepararDesayuno():
    print("Buscando ingredientes...")
    print("Eligiendo una receta...")
    print("Cocinando...")
    print("Preparando café...")
    print("Cafe y comida lista! Sirviendo...")
    print("¡El desayuno está listo!")


def abordarElTransporte(nombreDelTransporte,rutaASeguir):
    print("Subiendo a "+nombreDelTransporte)
    print("Yendo por "+rutaASeguir)
    print("¡Has llegado a tu destino!")

prepararDesayuno()
abordarElTransporte("Metrobus","linea 1")
```

Puedes ejecutar este programa usando directamente el intérprete de __Python__ u otras alternativas como __iPython__ o __Colab__ de Google. Si tienes dudad de cómo ejecutarlo pregunta a tu experto.

[`Anterior`](../README.md#procedimientos-y-funciones) | [`Siguiente`](../reto02/README.md)
