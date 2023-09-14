# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 20:00:00 2023

@author: User
"""

lista3 = []
lista2 = ["R1",
          "R2",
          "R3",
          "OLT1",
          "R4",
          "S1",
          "S2",
          "S3",
          "AP1",
          "FW1",
          "OLT2"]

for item in lista2:
    if "R" in item:
        lista3.append(item)
        
print(lista3)

##Crear lista para routers, swhitches, dispositivos varios

routers = []
switches = []
devices = []
for i in lista2:
    if "R" in i:
        
        routers.append(i)
    elif "S" in i:
        switches.append(i)
    else:
        devices.append(i)
        
print("\t Routers:")
print(routers)
print("\t Switches: ")
print(switches)
print("\t Dispositivos varios")
print(devices)
    
       
"""
for item in lista2:
    if "R" in item:
        i+=1
        if i == 1:
            print("\t Routers:")
        print(item)
        routers.append(item)
    elif "S" in item:
        j+=1
        if j == 1:
            print("\t Switches:")
        print(item)
        switches.append(item)
    else:
        k+=1
        if k == 1:
            print("\t Otros Dispositivos:")
        print(item)
        devices.append(item)
 """
        