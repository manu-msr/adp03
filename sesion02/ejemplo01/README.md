[`Análisis de Datos con Python`](../../README.md) > [`Sesión 2`](../README.md) > `Ejemplo 1`

## Ejemplo 1: *Jupyter notebooks*

### 1. Objetivos :dart:

- Crear cuadernos con __Jupyter__

### 2. Requisitos :clipboard:

1. Ambiente de conda para el curso levantado
1. Servidor de __Jupyter__ levantado

### 3. Desarrollo :rocket:

A continuación se muestra el siguiente cuaderno de __Jupyter__ descargalo y agrégalo a tu servidor, analiza el contenido. Para analizarlo debes mover el archivo a la carpeta donde levantaste el servidor correspondiente.

---

<details><summary><a href="codigos/ejemplo1.ipynb">ejemplo1.ipynb</a></summary>

# Mi primer cuadero en Jupyter Notebook
## Manuel Soto Romero

### Notas sutíles
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed est ipsum, vehicula vel hendrerit et, tincidunt vitae diam. In et elementum elit. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nam laoreet risus id massa pharetra, quis eleifend ligula cursus. Vestibulum eu ultrices magna. Duis in cursus sem. Mauris leo turpis, condimentum sed facilisis et, consectetur quis dui. Proin consequat arcu nec neque mattis eleifend. Curabitur vitae massa gravida, tempor lorem eget, fermentum arcu. Fusce at felis eros. Curabitur in dignissim velit. Maecenas in turpis ac elit hendrerit dignissim. Nunc commodo vitae ex in dictum.


```python
print("¡Hola Mundo!")
```

    ¡Hola Mundo!



```python
for counter in range(1,1000):
    print("Línea " + str(counter) + " de 1000")
```

    Línea 1 de 1000
    Línea 2 de 1000
    Línea 3 de 1000
    Línea 4 de 1000
    Línea 5 de 1000
    Línea 6 de 1000
    Línea 7 de 1000
    Línea 8 de 1000
    Línea 9 de 1000
    Línea 10 de 1000
    ...



```python
import ejemplo1 as e1
e1.imprimirNombre('Manuel')
```

    Hola Manuel



```python
e1.imprimirNombre('Fulano')
```

    Hola Fulano



```python
variable1 = 1234
```


```python
variable2 = 5678
print("Variable 1: " + str(variable1))
print("Variable 2: " + str(variable2))
print("Suma: " + str(variable1+variable2))
```

    Variable 1: 1234
    Variable 2: 5678
    Suma: 6912

</details>

---

<br>

Si tienes dudas de cómo ejecutarlo pregunta a tu experto.

[`Anterior`](../README.md#jupyter-notebooks) | [`Siguiente`](../reto01/README.md)
