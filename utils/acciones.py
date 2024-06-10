from backend.funciones.entidades import common, clientes, vehiculos, transacciones


def llamar_listar_tabla_json():
    nombre_json = "clientes"
    return common.listar_tabla_json(nombre_json)
    
    
    
def llamar_eliminar_registro_json():
    nombre_json = "clientes"  
    filtro = {"id_cliente": 4}
    common.eliminar_registro_json(nombre_json, filtro)
   
    
    #todos_los_registros = clientes.listar_clientes_serie()
    # rellenar_treeview(tabla_clientes, todos_los_registros)
    
    