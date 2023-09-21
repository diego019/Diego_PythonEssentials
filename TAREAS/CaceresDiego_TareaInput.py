# -*- coding: utf-8 -*-

"""
        TAREA Python Essentials
        
Nombre: Diego Cáceres

        Ejemplo de uso de input()
        
"""
print("\t\t BIENVENIDO")
print("Para habilitar la entrega de su producto, confirme los siguientes datos: \n")
nombre = input("Por favor, ingrese su nombre: ")
apellido = input("Ahora, ingrese su apellido: ")
ubicacion = input("Ingrese la ciudad en la que se encuentra: ")
edad = input("Finalmente, ingrese su edad: ")

space = ' '

mensaje = ('\nMuchas gracias por confirmar sus datos ✅,' + space + nombre 
            + space + apellido + space + 'de' + space + edad + space 
            + 'años de edad, de la maravillosa ciudad de' + space + ubicacion  
            + ', su pedido se encuentra en camino. Espere con paciencia. \n\n Gracias por su preferencia, fue un placer atenderlo 😊😊')
            

print(mensaje)