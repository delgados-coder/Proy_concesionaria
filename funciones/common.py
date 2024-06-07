print("GENERAL.PY cargado con exito")


import pandas as TABLETEADOR

def cargar_json_en_tabla(nombre_tabla):
    return TABLETEADOR.read_json('./datos/' + nombre_tabla + ".json") 

def cargar_json_en_serial(nombre_tabla):
    return TABLETEADOR.read_json('./datos/' + nombre_tabla + ".json", typ='series')


