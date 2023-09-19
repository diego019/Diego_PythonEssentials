# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 18:53:12 2020

@author: Juan Carlos
"""

from time import sleep
seconds = 0
while True:
    try:
        print(seconds)
        seconds += 1
        sleep(1)
    except KeyboardInterrupt:
        print("¡No hagas eso!")   #no va a parar por el while true, le detuve con Ctrl + .   
        
        
'''
La excepción KeyboardInterrupt en Python se genera cuando el usuario interrumpe la ejecución de un programa presionando la combinación de teclas Ctrl+C (o Cmd+C en macOS) en la consola o terminal donde se está ejecutando el programa. Esta excepción generalmente se utiliza para detener un programa que se encuentra en un bucle infinito o en un estado bloqueado.
'''

##Uso: 
try:
    while True:
        pass  # Este bucle se ejecutará indefinidamente hasta que se interrumpa con Ctrl+C.
except KeyboardInterrupt:
    print("El programa fue interrumpido por el usuario.")