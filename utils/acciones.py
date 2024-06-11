#Funciones usadas por el Front para llamar al Back

from backend.funciones.entidades import cliente, common, transaccion, vehiculo


def llamar_listar_tabla_json(nombre_json):
    return common.listar_tabla_json(nombre_json)
    
def llamar_eliminar_registro_json(nombre_json,filtro):
    common.eliminar_registro_json(nombre_json, filtro)
   
 
    