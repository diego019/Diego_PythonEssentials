# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 20:13:13 2023

@author: User
"""
try:
    y = 1/0
except ZeroDivisionError:
    print("Zero Division")
except ArithmeticError:
    print("Arithmetic problem")
    
print("The END")


try:
    y = 1/0
except ArithmeticError:
    print("Arithmetic problem")
except ZeroDivisionError:
    print("Zero Division")
    
print("The END")