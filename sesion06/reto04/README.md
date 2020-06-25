[`Análisis de Datos con Python`](../../README.md) > [`Sesión 6`](../README.md) > `Reto 4`

## Reto 4: Subplanos de Dispersión 3D

### 1. Objetivos :dart:

- Aprender acerca de subplanos 3D

### 2. Requisitos :clipboard:

1. Ambiente de conda para el curso levantado
1. Servidor de __Jupyter__ levantado
1. Biblioteca __NumPy__ instalada
1. Biblioteca __Pandas__ instalada
1. Biblioteca __MatPlotLib__ instalada
1. Archivo [`dataset_cardio.csv`](codigos/meteoritos.json)

### 3. Desarrollo :rocket:

1. Ahora intenta generar un *grid* de 3 x 2 o bien, uno de 3 x 2

1. Agrega cuantos cubos necesites y observa los resultados

1. **Tip:** `add_subplot` es la función que te ayudará a hacer los espacios que necesitas

   ```python
   fig = plt.figure(figsize = (12,12))
   ax3D_1 = fig.add_subplot(2,2,1, projection='3d')
   ax3D_2 = fig.add_subplot(2,2,2, projection='3d')
   ax3D_3 = fig.add_subplot(2,2,3, projection='3d')
   ax3D_4 = fig.add_subplot(2,2,4, projection='3d')
   ```

[`Anterior`](../README.md#inssubplanos-de-dispersión-3dins) | [`Siguiente`](../README.md#3-postwork-memo)
