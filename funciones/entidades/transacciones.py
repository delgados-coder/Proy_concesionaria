from funciones.entidades import common 
print("--TRANSACCIONES.PY cargado con exito")
    
    
def listar_transacciones():
    print(common.listar_tabla_json("transacciones"))

def registrar_transacciones():
    print("registrar_transacciones()")
