# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 20:11:29 2023

@author: User
"""

import qrcode
img = qrcode.make('Some data here')
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")


# Define el enlace web que deseas codificar en el QR
enlace_web = "https://www.youtube.com/watch?v=dJrTg9T7SvA"

# Crea un objeto QRCode
codigo_qr = qrcode.QRCode(
    version=1,  # Versión del código QR (1 a 40, dependiendo del tamaño)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Nivel de corrección de errores (L, M, Q, H)
    box_size=10,  # Tamaño de cada caja del código QR
    border=4,  # Ancho del borde del código QR
)

#Agrega el enlace web al código QR
codigo_qr.add_data(enlace_web)
codigo_qr.make(fit=True)

# Crea una imagen del código QR
imagen_qr = codigo_qr.make_image(fill_color="black", back_color="white")

# Guarda la imagen del código QR en un archivo
imagen_qr.save("codigo_qr.png")

# Opcional: Mostrar la imagen del código QR
imagen_qr.show()



##################forma pr