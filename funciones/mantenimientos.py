from funciones import common 
print("--MANTENIMIENTO.PY cargado con exito")
def get_tabla_mantenimientos():
    tabla_mantenimientos = common.cargar_json_en_tabla("mantenimientos")
    print(tabla_mantenimientos)
    return tabla_mantenimientos

def get_serie_mantenimientos():
    serie_mantenimientos = common.cargar_json_en_serial("mantenimientos")
    return serie_mantenimientos

def listar_mantenimientos():
    print(get_tabla_mantenimientos())