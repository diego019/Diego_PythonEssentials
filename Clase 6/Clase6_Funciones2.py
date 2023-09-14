# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 18:55:55 2023

@author: User
"""

def saludo(nombre):
    print("Hola!", nombre)

saludo ("Juan")
saludo ("Diego")


def saludo2(nombre, apellido):
    print("Hola!", nombre,apellido)
    
saludo2("Diego","Cáceres")


def direct(ciudad, barrio, calle):
    print("La ciudad de entrega es: ", ciudad)
    print("El sector es: ", barrio)
    print("El pedido esta en la calle: ", calle)
    
ci = input("Ingrese la ciudad: ")
ba = input("Ingrese el barrio: ")
cl = input("Ingrese la calle principal de su domicilio: ")

direct(ci, ba, cl)


def direct(ciudad = "Ambato", barrio = "Huachi Grande", calle = "Remigio Crespo"):
    print("La ciudad de entrega es: ", ciudad)
    print("El sector es: ", barrio)
    print("El pedido esta en la calle: ", calle)

direct()  #Imprime en las variables por defecto