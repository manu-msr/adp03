[`Análisis de Datos con Python`](../../README.md) > [`Sesión 2`](../README.md) > `Ejemplo 2`

## Ejemplo 2: *Panda Dataframes*

### 1. Objetivos :dart:

- Cargar archivos __CSV__ usando __Pandas__

### 2. Requisitos :clipboard:

1. Ambiente de conda para el curso levantado
1. Servidor de __Jupyter__ levantado
1. Archivo __CSV__ con el reporte de crímenes

### 3. Desarrollo :rocket:

A continuación se muestra el siguiente cuaderno de __Jupyter__ descargalo y agrégalo a tu servidor, analiza el contenido. Para analizarlo debes mover el archivo a la carpeta donde levantaste el servidor correspondiente.

---

<details><summary><a href="codigos/ejemplo2.ipynb">ejemplo2.ipynb</a></summary>

# Pandas Dataframes
### Dr. Antonio Arista Jalife
### Modificado por: L. en C.C. Manuel Soto Romero

Pandas utiliza una estructura llamada "DataFrame" para manejar sus datos, de tal manera que es importante que nos familiaricemos con la estructura de ellos. 

#### Importamos Pandas a nuestro notebook:


```python
import pandas as pd
```

#### Cargamos el Dataset y lo desplegamos:


```python
dataframe = pd.read_csv('CrimeReports.csv')

dataframe
```

Si nosotros queremos las primeras 10 líneas podemos utilizar el comando .head(10), o el comando .tail(10) si queremos las últimas 10.


```python
dataframe.head(10)
```


```python
dataframe.tail(10)
```

No todas las columnas en un dataframe son útiles, por lo que nosotros podemos elegir las columnas y el orden de la siguiente manera:
dataframe[['nombre columna 1', 'nombre columna 2',...]]


```python
dataframe[['address','latitude','longitude', 'ucr_ncic_code']]
```


</details>

---

Si tienes dudas de cómo ejecutarlo pregunta a tu experto.

[`Anterior`](../README.md#pandas-dataframes) | [`Siguiente`](../reto02/README.md)
