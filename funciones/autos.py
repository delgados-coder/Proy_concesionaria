from funciones import common 

print("--AUTOS.PY cargado con exito")

def get_tabla_autos():
    tabla_autos = common.cargar_json_en_tabla("autos")
    print(tabla_autos)
    return tabla_autos

def get_serie_autos():
    serie_autos = common.cargar_json_en_serial("autos")
    return serie_autos    
    
def listar_autos():
    print(get_tabla_autos())
    
