# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 18:39:29 2023

@author: User
"""

datos = 1
nativa = 100
if datos == nativa:
    print("1")
    print("Las variables son iguales")
    print("2")
else:
    if datos == nativa:
        print("Las variables son diferentes")
    else:
        if datos == nativa:
            print("Hola")
        else:
            if datos == nativa:
                print("Hola 2")
                
#USO DEL elif

acl = int(input("Ingrese el dato del # de ACL: "))
if acl >=1 and acl <=99:
    print("Es un ACL estándar")
elif acl >=100 and acl <=199:
    print("Es un ACL extendida")
else: 
    print("El valor ingresado no es un ACL")