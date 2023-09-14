# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 20:11:58 2023

@author: User
"""
lis1 = [2,4,7,9]
lis1

def saludo3(lista):
    for i in lista:
        print("Hola, ", i)
        
saludo3(["Diego"])
saludo3(["Diego","Armando", "Juan"])  #lista

saludo3(("Diego","Armando", "Juan")) #tupla (no se puede modificar)


def creaLista(n):
    lista = []
    for item in range(n):
        lista.append(item)
    return lista

print(creaLista(50))