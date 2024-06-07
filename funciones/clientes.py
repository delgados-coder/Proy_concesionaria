from funciones import common 
print("--CLIENTES.PY cargado con exito")
def get_tabla_clientes():
    tabla_clientes = common.cargar_json_en_tabla("clientes")
    print(tabla_clientes)
    return tabla_clientes

def get_serie_clientes():
    serie_clientes = common.cargar_json_en_serial("clientes")
    return serie_clientes

def listar_clientes():
    print(get_tabla_clientes())

