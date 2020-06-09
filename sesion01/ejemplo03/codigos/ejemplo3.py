# -*- coding: utf-8 -*-
"""
@author: Dr. Antonio Arista Jalife
"""
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
