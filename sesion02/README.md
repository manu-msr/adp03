[`Análisis de Datos con Python`](../README.md) > `Sesión 2`

## Sesión 2: Herramientas de *Data Scientist*

<img src="../imagenes/pizarron.png" align="right" height="100" width="100" hspace="10">

### 1. Objetivos :dart: 

- Aprender acerca de ambientes de __Python__
- Aprender sobre __Jupyter Notebooks__
- Aprender sobre __Pandas__
- Aprender bases simples de __MatPlotLib__

### 2. Contenido :blue_book:

El contenido de esta sesión lo puedes encontrar en [GitBook](https://beduexpert.gitbook.io/data-analysis/sesion-02-librerias-para-el-analisis-de-datos-con-python).

---
#### <ins>Ambientes de Python</ins>

Los ambientes no permiten modularizar los proyectos, de forma que cada uno tenga sus propios módulos definidos sin que interfieran con otros proyectos. En este módulo haremos uso de *Anaconda* o si lo prefieres también puedes instalar *Miniconda*.

La página de este gestionador de ambientes se ecuentra aquí:

- [Anaconda](https://www.anaconda.com/distribution/)
- [Miniconda](https://docs.conda.io/en/latest/miniconda.html)

Una vez instalado, deberás crear un ambiente para el curso:

```
$conda create --name 'bedu' python=3.7
$conda activate bedu
```

También puedes usar __Anaconda Powershell__ directamente. Instala las bibliotecas que usaremos en el curso:

```
$pip install numpy
$pip install pandas
$pip install matplotlib
$pip install jupyter
```

---
#### <ins>*Jupyter Notebooks*</ins>

> **Recuerda:** Para levantar un servidor de **Jupyter** es necesario ejecutar el comando `jupyter notebook`. A partir de esta sesión todo el contenido será compartido mediante cuadernos de **Jupyter**.

   - [**`EJEMPLO 1`**](ejemplo01/README.md)
   - [**`RETO 1`**](reto01/README.md)

---

#### <ins>*Pandas Dataframes*</ins>

> **Recuerda:** Con __Pandas__ puedes manipular datos mediante dos tipos de estructuras: *series* y *dataframes*. Para usar esta biblioteca escribir `import pandas as pd`.

   - [**`EJEMPLO 2`**](ejemplo02/README.md)
   - [**`RETO 2`**](reto02/README.md)
   - [**`RETO 3`**](reto03/README.md)
---

#### <ins>*Matplotlib*</ins>

> **Recuerda:** Con __Matplotlib__ puedes realizar gráficos de todo tipo. Para usar esta biblioteca escribir `import matplotlib.pyplot as plt`.

   - [**`EJEMPLO 3`**](ejemplo03/README.md)
---

### 3. Postwork :memo:
Aplica lo todo lo que aprendiste durante la sesión a tu proyecto personal.

- [**`POSTWORK SESIÓN 2`**](postwork/README.md)

<br/>

[`Anterior`](../sesion01/README.md) | [`Siguiente`](../sesion03/README.md)
