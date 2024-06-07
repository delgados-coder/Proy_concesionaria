from funciones import common 
print("--TRANSACCIONES.PY cargado con exito")
def get_tabla_transacciones():
    tabla_transacciones = common.cargar_json_en_tabla("transacciones")
    print(tabla_transacciones)
    return tabla_transacciones

def get_serie_transacciones():
    serie_transacciones = common.cargar_json_en_serial("transacciones")
    return serie_transacciones

def listar_transacciones():
    print(get_tabla_transacciones())