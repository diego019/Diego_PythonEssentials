# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 20:12:47 2023

@author: User
"""
print("\t Bienvenido al sistema de registro de estudiantes")
firstName = input("Ingrese su primer nombre: ")
lastName = input("Ingrese su apellido: ")
location = input ("Ingrese su ciudad actual: ")
age = input("Ingrese su edad: ")
space = " "

mensaje = "Hola" +space + firstName + space + lastName + space +","+ space + location +space+ "es una ciudad hermosa y acojedora" + space + "," + space + ". Tus" + space + age + space + "años es la edad perfecta para empezar el curso. Inscríbete YA!"  
print(mensaje)