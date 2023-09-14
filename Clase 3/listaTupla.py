# -*- coding: utf-8 -*-
lista = [1,4,6.4,"Hola",True,18]

print(type(lista))

print(lista)
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])
print(lista[5])
#print(lista[6])


print(lista[-1])
print(lista[-2])
print(lista[-3])
print(lista[-6])
#print(lista[-7])  #Se da la vuelta 1 sola vez

lista[5] = 20
print(lista)

lista[5]
print(lista)

tupla = (1,4,6.4,"Hola", True , 18)
# tupla[5]  = 20
# del tupla[5] 

print(tupla.__sizeof__)


lista1 = [1,4,6.4,"Hola",True,18]
lista2 = [4,9,False,3,"Hola",True,45]

lista2[2] = lista1
print(lista2) 