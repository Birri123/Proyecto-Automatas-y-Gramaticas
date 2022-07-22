# Luca Terranova - Abril Freytes - Carla Centeleghe - Abril Britos
#------------------------------------------------------------------

#Proyecto examen final Autómatas y Gramáticas
#------------------------------------------------------------------

'''Sobre la Base de Datos dada este codigo deberá hacer un seguimiento del Tiempo de Sesión (Session Time) de un usuario
en un período de tiempo establecido (Rango de Fechas). Debe incluir una lista de usuarios y la posibilidad de ingresar
un Rango de Fechas'''

#------------------------------------------------------------------
'''el usuario ingresa la fecha (luens y viernes) para limitar la busqueda de datos (persomas) 
 y tira la lista de perssonas conectadas en ese momento. luego se puede selcecionar a la persona y expostarla a exel
 hacer que el programa sigua corriendo y que pueda seguir buscando nuevas fechas y personas. 
 Primero pregunta si quiere buscar otra persona en ese rango de fechas 
 y luego pregunta si quiere buscar otro rango de fechas '''



#Importar ruta de archivo
import os

#Importamos libreria re
import re
# Definimos la expresion regular para el usuario
usuario = re.compile(r'^[a-zA-Z0-9]{1,}$')

#Definimos el Rango de Fechas (dias-mes-año)   
fecha = re.compile(r'^[0-9]{1,2}-[0-9]{1,2}-[0-9]{4}$')

#Definimos la ruta del archivo
archivo =open("Datos.txt")
#Leemos el archivo por pantalla
i = 1
j = 0

def imprimir_primeras_30_lineas():
    i = 0

    for linea in archivo:
        if fecha.match(fecha1):
            print (linea)
        else:
            print('No se encontraron resultados')

#        if i < 30:
 #           lineas = linea.rstrip("\\n")
  #          print("%4d: %s" % (lineas))
   #         i += 1   
    #        return lineas
        
fecha1 = input("Ingrese la fecha desde la cual desea buscar: ")
a = imprimir_primeras_30_lineas()
print(a.imprimir_primeras_30_lineas())
'''

def buscar_fecha():
    for line in archivo:
        if fecha == archivo[1,2]:
            return line
            
print(buscar_fecha())

'''
'''def tiempo_sesion(lista):
    #Creamos una lista vacia
    lista_tiempo = []
    #Recorremos la lista
    for i in range(len(archivo)):
        #Si el usuario es igual a la lista
        if lista[i] == lista[i+1]:
            #Agregamos el tiempo de sesión a la lista
            lista_tiempo.append(archivo.iloc[i][2])


#Buscar usuario dentro del archivo excel
def buscar_usuario(archivo):

    #Creamos una lista vacia
    lista = []

    #Recorremos el archivo de texto
    for i in range(len(archivo)):
        #Si el usuario coincide con la expresion regular
        if usuario.match(archivo.iloc[i][0]):
            #Agregamos el usuario a la lista
            lista.append(archivo.iloc[i][0])
            #Retornamos la lista
            return lista
#Buscar fecha dentro del archivo excel
def buscar_fecha(fecha):
    
        #Creamos una lista vacia
        lista = []
    
        Recorremos el archivo de texto
        for i in range(len(archivo)):
            #Si la fecha coincide con la expresion regular
            if fecha.match(archivo.iloc[i][1]):
                #Agregamos la fecha a la lista
                lista.append(archivo.iloc[i][1])
                #Retornamos la lista
                return lista



'''