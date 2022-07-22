import pandas as pd

def open_file():
    datos = pd.ExcelFile('Datos.xlsx') #Si el OBJETO no es un búfer o una ruta, debe establecerse para identificarlo. Los motores soportados son: “xlrd”, “openpyxl”, “odf”, “pyxlsb”. Elegimos “openpyxl” porque soporta formatos de archivos Excel más nuevos.
    df = datos.parse('acts-user')
    print(df)
    
open_file()