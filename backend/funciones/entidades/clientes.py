from backend.funciones.entidades import common 
print("--CLIENTES.PY cargado con exito")

def listar_clientes():
    print(common.listar_tabla_json("clientes"))
    print("-----------------------------------------------------------------------------------")
    print("-----------------------------------------------------------------------------------")
    

    #print(common.listar_tabla_json("clientes","documento",True))
    #TODA LA LISTA POR ORD POR col -DOCUMENTO- forma -ASCENDENTE-
    
    #print(common.listar_tabla_json("clientes","documento",False))
    #TODA LA LISTA POR ORD POR col -DOCUMENTO- forma -DESCENDENTE-
    
    #print(common.listar_tabla_json("clientes",filtros_aplicados={"nombre": "Pedro"}))
    #OBTENER LISTA CON FILTRO DE nombre = Pedro
    
def listar_clientes():
    print(common.listar_tabla_json("clientes"))

def registrar_clientes():
    print("registrar_clientes()")

def eliminar_clientes():
    print("eliminar_clientes()")

def editar_clientes():
    print("editar_clientes()")

def estado_clientes():
    print("estado_clientes()")
