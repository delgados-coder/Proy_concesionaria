from funciones.entidades import common 
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
    

def registrar_clientes():
    print("registrar_clientes()")

def elimnar_clientes():
    print("elimnar_clientes()")

def editar_clientes():
    print("editar_clientes()")
