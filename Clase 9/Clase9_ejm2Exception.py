# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 20:03:14 2023

@author: User
"""

try:
    x = int(input("Enter a number: "))
    y = 1/x
    print(y)
    
except ZeroDivisionError:
    print("You cannot divide by zero, sorry.")

except ValueError:
    print("You must enter an integer value.")
    
except:  #por ejemplo, deteniendo la terminal4
    print("Oh dear, something went wrong...")
print("THE END,")