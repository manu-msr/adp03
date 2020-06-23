[`Análisis de Datos con Python`](../../README.md) > [`Sesión 3`](../README.md) > `Reto 4`

## Reto 4: Operaciones punto a punto y funciones con __NumPy__

### 1. Objetivos :dart:

- Transformar una funcion de *normal* en una función que use __NumPy__.

### 2. Requisitos :clipboard:

1. Ambiente de conda para el curso levantado
1. Servidor de __Jupyter__ levantado
1. Biblioteca __NumPy__ instalada

### 3. Desarrollo :rocket:

Esta es la función de semiverseno de la sesión pasada. El reto consiste en construir la versión para __Numpy__.

```python
def ObtenerDistancia_numPy(lat1, lon1, lat2, lon2):
	# Convertimos grados a radianes
    lon1, lat1, lon2, lat2 = map(radians, [lon1,lat1,lon2,lat2])
    
    # Fórmula del semiverseno
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371
    return c * r
```

Funciones de __NumPy__ que te servirán:

- `X = np.radians(X)`
- `np.sin(x)`
- `np.cos(y)`
- `np.power(x,2) = x**2`
- `np.arcsin(x)`
- `np.sqrt(x)`

[`Anterior`](../ejemplo05/README.md) | [`Siguiente`](../README.md#3-postwork-memo)
