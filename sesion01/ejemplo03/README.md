[`Análisis de Datos con Python`](../../README.md) > [`Sesión 1`](../README.md) > `Ejemplo 3`

## Ejemplo 3: Funciones

### 1. Objetivos :dart:

- Mostrar cómo operan las funciones como bloques que solucionan un problema específico.

### 2. Requisitos :clipboard:

1. Python 3 instalado.

### 3. Desarrollo :rocket:

A continuación se muestra el siguiente *script*. Ejecútalo y analiza el código en un editor de textos.

[`ejemplo3.py`](codigos/ejemplo3.py)
```python
def calcularCalorias(tiempoEnHoras):
    tiempoEnMinutos = tiempoEnHoras*60
    calorias = tiempoEnMinutos/3 
    return calorias

def hacerEjercicio(deporte, tiempoEnHoras, equipoAUsar):
    print("Vamos a jugar "+deporte);
    print("Jugarás durante "+str(tiempoEnHoras)+" horas")
    calorias = calcularCalorias(tiempoEnHoras)
    print("Gastaste "+str(calorias)+ " Cals")
    print("con "+equipoAUsar)

hacerEjercicio("Fútbol",3,"balón")
```

Puedes ejecutar este programa usando directamente el intérprete de __Python__ u otras alternativas como __iPython__ o __Colab__ de Google. Si tienes dudad de cómo ejecutarlo pregunta a tu experto.

[`Anterior`](../reto02/README.md) | [`Siguiente`](../reto03/README.md)
