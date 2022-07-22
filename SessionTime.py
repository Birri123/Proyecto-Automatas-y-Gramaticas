import datetime as dt
import re
import pandas as pd

class ErrorFecha(Exception):
    pass

def RegexFecha(fecha): 
    fecha_regex = re.compile(r'^[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}$')
    try:
        if fecha_regex == fecha:
            pass
    except ErrorFecha:
        print("El formato de la fecha ingresada es incorrecto, intente nuevamente")
    
    return fecha

