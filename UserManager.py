import re
import pandas as pd

class ErrorUsuario(Exception):
    pass

def RegexUsuario(usuario):
    regex_usuario = re.compile((r'\b([A-Za-z-\.\/\d*]{1,})\b')) 
    try:
        if regex_usuario == usuario:
            pass
    except ErrorUsuario:
        print("El formato de usuario ingresado no es correcto, intente nuevamente")
    
    return usuario

