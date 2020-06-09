[`Análisis de Datos con Python`](../../README.md) > [`Sesión 1`](../README.md) > `Ejemplo 5`

## Ejemplo 5: Ciclos

### 1. Objetivos :dart:

- Usar ciclos para hacer que un código se repita una y otra vez, hasta que la condición deje de cumplirse o hasta que se agote el número de ciclos de rango.

### 2. Requisitos :clipboard:

1. Python 3 instalado.

### 3. Desarrollo :rocket:

A continuación se muestra el siguiente *script*. Ejecútalo y analiza el código en un editor de textos.

[`ejemplo5.py`](codigos/ejemplo5.py)
```python
listaCantidades = [3,2,4,1]
listaCosas = ['manzanas', 'peras', 'cajas de cereal', 'paquetes de arroz']

listaSuper = []
for contador in range(0, len(listaCosas)):
    listaSuper.append(str(listaCantidades[contador]) + " " +listaCosas[contador])
    print(listaSuper[contador])
```

Puedes ejecutar este programa usando directamente el intérprete de __Python__ u otras alternativas como __iPython__ o __Colab__ de Google. Si tienes dudad de cómo ejecutarlo pregunta a tu experto.

[`Anterior`](../README.md#ciclos) | [`Siguiente`](../reto05/README.md)
