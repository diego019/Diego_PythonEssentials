# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 20:26:27 2023

@author: User
"""

file = open("devices.txt")

#si no tengo en la misma carpeta debo dar todo el path (direccion)
#C:\Users\User\Desktop\CURSO PYTHON\Documentación GitHub\Clase 10\Archivos

for item in file:
    print(item)
file.close()