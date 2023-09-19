# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 18:57:55 2023

@author: User
"""


def fibonacci(n):
    secuencia = [0, 1]
    print(secuencia[0]," ", secuencia[1], end = '  ')
    while secuencia[-1] < n:
        siguiente = secuencia[-1] + secuencia[-2]
        secuencia.append(siguiente)
        print(siguiente, end = '  ')


#fibonacci(5)

def fibonacci2(n):
    a , b = 0, 1  
    print(a, end = ' ')
    print(b, end = ' ')
    while b < n:
        banterior = b
        b = a + b
        a = banterior
        print(b, end = ' ')
        
#fibonacci2(5)
        
def test1():
    pass

def test2():
    pass

def test3():
    pass

def test4():
    pass

def test5():
    pass

pi = 24/7