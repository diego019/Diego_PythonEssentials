# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 19:04:33 2023

@author: User
"""
##import nombre_modulo
"""
import math

print(math.sin(math.pi/2))
"""

#exportar variables en especifico
from math import sin, pi

print(sin(pi/2))

#namespace

#puedo tener mi propia funcion de seno
pi = 22/3
def sin():
    return 0.9999

print(sin())
print(pi)

#No entra en conficto por que se diferencian


#importar todo
# from math import *
#Esta forma es util para cuando no se que nomas voy a utilziar, luego podria solo llamar a las necesarias
#al importar todo pueden quedar brechas de seguridad, es por las versiones (hay versiones probadas y seguras), pero en versiones de prueba no tengo garantiza que en la version final este todo parchado y resuelto
#esto puede ser que tome problemas y abra un socket y quede abierto un socket, puerto o una brecha de seguridad
#y un agente de amenza externo este funcando su funcion que le permitira tener el comando y control del servidor

