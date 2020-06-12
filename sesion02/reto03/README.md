[`Análisis de Datos con Python`](../../README.md) > [`Sesión 2`](../README.md) > `Reto 3`

## Reto 3: *Panda Dataframes*

### 1. Objetivos :dart:

- Manipular archivos __CSV__ usando __Pandas__

### 2. Requisitos :clipboard:

1. Ambiente de conda para el curso levantado
1. Servidor de __Jupyter__ levantado
1. Cuaderno del ejemplo 2

### 3. Desarrollo :rocket:

- El jefe de la policia necesita saber la distancia de cada crimen.
- Para ello, usaremos la distancia de semiverseno.
- Semiverseno: Dadas dos coordenadas lat/long, calcular la distancia entre ellas. 

[`Semiverseno.py`](codigos/Semiverseno.py)
```python
from math import radians, cos, sin, asin, sqrt

def ObtenerDistancia(lat1, lon1, lat2, lon2):
    # Convertimos grados a radianes
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # Formula del semiverseno:
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 
    return c * r
```

[`Anterior`](../reto02/README.md) | [`Siguiente`](../README.md#matplotlib)
