#Funciones usadas por el Front para llamar al Back

from backend.funciones import api


def llamar_listar_tabla_json(nombre_json):
    return api.leer_registros(nombre_json)
    
def llamar_eliminar_registro_json(nombre_json,filtro):
    api.eliminar_registro_json(nombre_json, filtro)
   
 
    