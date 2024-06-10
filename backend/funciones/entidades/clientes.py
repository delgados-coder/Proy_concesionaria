from backend.funciones.entidades import common 

def listar_clientes():
    return (common.listar_tabla_json('clientes', orden_por=None, orden_ascendente=True, filtros_aplicados=None))

def listar_clientes_serie():
    return (common.listar_serie_json('clientes', orden_por=None, orden_ascendente=True, filtros_aplicados=None))
  

    #print(common.listar_tabla_json("clientes","documento",True))
    #TODA LA LISTA POR ORD POR col -DOCUMENTO- forma -ASCENDENTE-
    
    #print(common.listar_tabla_json("clientes","documento",False))
    #TODA LA LISTA POR ORD POR col -DOCUMENTO- forma -DESCENDENTE-
    
    #print(common.listar_tabla_json("clientes",filtros_aplicados={"nombre": "Pedro"}))
    #OBTENER LISTA CON FILTRO DE nombre = Pedro
   
def registrar_clientes():
    print("registrar_clientes()")

def eliminar_clientes():
    print("eliminar_clientes()")

def editar_clientes():
    print("editar_clientes()")

def estado_clientes():
    print("estado_clientes()")
