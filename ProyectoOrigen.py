# Luca Terranova - Abril Freytes - Carla Centeleghe - Abril Britos
#------------------------------------------------------------------

#Proyecto examen final Autómatas y Gramáticas
#------------------------------------------------------------------

'''Sobre la Base de Datos dada este codigo deberá hacer un seguimiento del Tiempo de Sesión (Session Time) de un usuario
en un período de tiempo establecido (Rango de Fechas). Debe incluir una lista de usuarios y la posibilidad de ingresar
un Rango de Fechas'''

#------------------------------------------------------------------
#Importar ruta de archivo
import os

#Importamos libreria re
import re

# Definimos la expresion regular para el usuario
usuario = re.compile(r'^[a-zA-Z0-9]{1,}$')

#Definimos el Rango de Fechas (dias-mes-año)   
fecha = re.compile(r'^[0-9]{1,2}-[0-9]{1,2}-[0-9]{4}$')

#Abrimos archivo
archivo = open('datos.txt')

#Leemos el archivo Datos.txt
i = 1
j = 0
fecha1 = input(print("Ingrese la fecha : "))

#Validacion de formato de fecha
if fecha1 == fecha:
    print("Formato correcto")

else:
    print("Formato incorrecto")

print("BUscamos los usuarios en esa fecha")



for linea in archivo:
    if i < 30:
        lineas = linea.rstrip("\\n")
        print("%4d: %s" % (lineas))
        i += 1   


       
















