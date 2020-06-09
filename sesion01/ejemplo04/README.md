[`Análisis de Datos con Python`](../../README.md) > [`Sesión 1`](../README.md) > `Ejemplo 4`

## Ejemplo 4: Condicionales

### 1. Objetivos :dart:

- Aprender acerca de condicionales para bifurcar el código como se necesite, dependiendo de si las condiciones se cumplen o no.

### 2. Requisitos :clipboard:

1. Python 3 instalado.

### 3. Desarrollo :rocket:

A continuación se muestra el siguiente *script*. Ejecútalo y analiza el código en un editor de textos.

[`ejemplo4.py`](codigos/ejemplo4.py)
```python
def salirDePaseo(estaLloviendo, traesParaguas):
    print("Saldremos de paseo?...")
    if(estaLloviendo == True):
        if(traesParaguas == True):
            print("Ok! vamos a salir!")
        else:
            print("No creo que sea una buena idea")
    else:
        print("Ok! vamos a salir!")
        
salirDePaseo(True, True)
```

Puedes ejecutar este programa usando directamente el intérprete de __Python__ u otras alternativas como __iPython__ o __Colab__ de Google. Si tienes dudad de cómo ejecutarlo pregunta a tu experto.

[`Anterior`](../README#condicionales) | [`Siguiente`](../reto04/README.md)
