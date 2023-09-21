# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 18:24:28 2023

@author: User
"""

def readint(prompt, vmin, vmax):
    while True:
        try:
            v = int(input(prompt))
            if v >= vmin and v <= vmax:
                print("The number is:", v)
                return v
                break
            else:
                print("El valor no está en el rango permitido ")
                
        except Exception:
            print("Error en el ingreso")

while True:
    
    try:
        vmin = int(input("Ingrese el limite inferior: "))
        break
    except Exception:
        print("Error en el ingreso")
    
while True:
    try:
        vmax = int(input("Ingrese el limite superior: "))
        
        break
    except Exception:
        print("Error en el ingreso")

prompt = "Enter a number from "+ str(vmin) +" - "+ str(vmax) +": "
readint(prompt,vmin,vmax)


v = readint("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)