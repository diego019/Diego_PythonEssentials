# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 20:25:08 2023

@author: User
"""
#* diferentes parametros posicionales, el parametro que va a recibir puede ser un valor o varios valores

def suma(*a):
    print("\n \t Tipo de datos del argumento", type(a))
    sum = 0
    for n in a:
        sum += n
    
    print("Suma: ", sum)

suma(1)
suma(5,8)
suma(1,6)
suma (2,8,10)
suma(0,1)
suma(1,2)
suma(3,5)
suma(4,5,6,7)
suma(1,2,3,5,6)
suma(1,2,3,5,6,7,8,9,10)
suma(1,2,3,5,6,7,8,9,10,11,12,13,14)
suma(1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17)


