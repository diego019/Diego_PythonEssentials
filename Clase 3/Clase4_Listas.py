# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 18:39:44 2023

@author: User
"""

c = [0,0,0,0,0]
dispositivos = ["R1",
                "R2",
                "R3",
                "R4",
                "S1",
                "S2",
                "S3"]

print(dispositivos)
print(dispositivos[0])


devices = ("R1",
                "R2",
                "R3",
                "R4",
                "S1",
                "S2",
                "S3")
print(devices)
print(devices[0])

a = [1,3,5,7]
b = [0,2,4,6]


c[0] = a[0] + b[0]
c[1] = a[1] + b[1]

print(c)

## DICCIONARIOS

dict1 = {"R1":"10.10.10.1",
         "R2":"10.10.10.2",
         "alumno01":"Diego",
         "ID":"1804413290",
         1:"emp01",
         "email":"diegoarm019@gmail.com"}

print(dict1)
print(dict1[1])
print(dict1["ID"])
dict1["S1"] = "10.1.1.1"
print("AP" in dict1)
print("R1" in dict1)

dict["S1"] = "10.1.1.1"
print
