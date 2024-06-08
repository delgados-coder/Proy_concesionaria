from funciones import common 

print("--vehiculos.PY cargado con exito")

def get_tabla_vehiculos():
    tabla_vehiculos = common.cargar_json_en_tabla("vehiculos")
    return tabla_vehiculos

def get_serie_vehiculos():
    serie_vehiculos = common.cargar_json_en_serial("vehiculos")
    return serie_vehiculos    
    
def listar_vehiculos():
    print(get_tabla_vehiculos())
    
