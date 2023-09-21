# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 08:55:56 2023

@author: Juan Carlos
"""

class LecturaSensorError(Exception):
    pass

class SensorTemperatura:
    def leer_temperatura(self):
        temperatura = input("Ingrese la temperatura: ")
        try:
            temperatura = float(temperatura)
        except ValueError:
            raise LecturaSensorError("Valor de temperatura inválido")
        return temperatura

    def verificar_rango(self, temperatura):
        if temperatura < -50 or temperatura > 100:
            raise LecturaSensorError("Valor de temperatura fuera de rango")

# Programa principal
sensor = SensorTemperatura()

while True:
    try:
        temperatura = sensor.leer_temperatura()
        sensor.verificar_rango(temperatura)
        print("Temperatura válida:", temperatura)
    except LecturaSensorError as e:
        print("Error al leer la temperatura:", e)
    
    opcion = input("¿Desea ingresar otra temperatura? (s/n): ")
    if opcion.lower() != 's':
        break
