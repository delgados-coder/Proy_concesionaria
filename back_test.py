
from backend.funciones import utilidades as util
from backend.funciones import api as api

util.limpiar_consola()


############### LISTADO #######################
orden = ["documento",True]
filtro={"id_cliente":2}

# print(api.leer_registros("cliente"))
print("------------------------------------------------------------------------------------------------------------------------------------")
   #or
print(api.leer_registros("cliente",orden))
print("------------------------------------------------------------------------------------------------------------------------------------")
   #or
# print(api.leer_registros("cliente",filtro_aplicado=filtro))



############## ELIMINACION ###################
# entidad='cliente'
# registro_a_eliminar = {"id_cliente":5}

# print(api.leer_registros(entidad))
# input("-----------------------------------------------------------------------------------------------------------------------------------------------------")
# api.baja_registro(entidad,registro_a_eliminar)
# input("-----------------------------------------------------------------------------------------------------------------------------------------------------")
# print(api.leer_registros(entidad))



############## CREACION ###################
# entidad='cliente'
# registro_a_agregar={
#         "nombre":"Fatum",
#         "apellido":"Encoder",
#         "documento":12745381,
#         "direccion":"mirter@gmail.com",
#         "telefono":"3812545256",
#         "correo_electronico":"example@gmail.com"
# }
# print(api.leer_registros(entidad))
# input("-----------------------------------------------------------------------------------------------------------------------------------------------------")
# util.limpiar_consola()
# api.alta_registro(entidad,registro_a_agregar)
# print(api.leer_registros(entidad))
# input("-----------------------------------------------------------------------------------------------------------------------------------------------------")
# util.limpiar_consola()



############## EDICION ###################


