import os
from backend.funciones.entidades import clientes
from backend.funciones.entidades import vehiculos
from backend.funciones.entidades import transacciones


#---------INICIO FUNCIONES CONSOLA------------#
def limpiar_consola():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
#----------FIN FUNCIONES CONSOLA---------------#


#-------------------------------INICIO Funcion Auxiliar para Crear de Menus Dinamicos-----------------------------------#
def crear_menu(titulo, opciones, funciones):
    while True:
        if not isinstance(opciones, list) or not opciones:
            print("Las opciones deben ser una lista no vacía.")
            return
        if not isinstance(funciones, list) or not funciones:
            print("Los valores deben ser una lista no vacía.")
            return
        
        limpiar_consola()
        print(titulo)
        for num_op in range(len(opciones)):
            print(f"{num_op + 1}. {opciones[num_op]}")
        print(f"{len(opciones) + 1}. Salir")    
        seleccion = input("Seleccione una opción: ")

        try:
            seleccion = int(seleccion)
            if 1 <= seleccion <= len(funciones):
                nombre_funcion = funciones[seleccion-1]
                if nombre_funcion:
                    funcion_a_llamar = globals()[nombre_funcion]
                    funcion_a_llamar()
                else:
                    print("La función no existe. Intente de nuevo.")
            elif seleccion == len(opciones) + 1:
                break
            else:
                print("Selección no válida. Intente de nuevo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
#-------------------------------FIN Funcion Auxiliar para Crear de Menus Dinamicos-----------------------------------#    


#-------------------------||-Iniciar - creador Submenus acciones Por Entidad --||--------------------------------------------#
def menu_vehiculos():
    titulo='Gestionar Vehiculos'
    opciones=["Listar Vehiculos","Registrar Vehiculos","Editar Vehiculos","Eliminar Vehiculos","Cambiar Estado Vehiculo"]
    funciones=["gestionar_vehiculos_listar","gestionar_vehiculos_registrar","gestionar_vehiculos_editar","gestionar_vehiculos_eliminar","gestionar_vehiculos_estado"]
    crear_menu(titulo,opciones,funciones)

def menu_clientes():
    titulo='Gestionar Clientes'
    opciones=["Listar Clientes","Registrar Clientes","Editar Clientes","Eliminar Clientes","Cambiar Estado Clientes"]
    funciones=["gestionar_clientes_listar","gestionar_clientes_registrar","gestionar_clientes_editar","gestionar_clientes_eliminar","gestionar_clientes_estado"]
    crear_menu(titulo,opciones,funciones)
    
def menu_transacciones():
    titulo='Gestionar Transacciones'
    opciones=["Listar Transacciones","Registrar Transacciones","Editar Transacciones","Eliminar Transacciones","Cambiar Estado Transacciones"]
    funciones=["gestionar_transacciones_listar","gestionar_transacciones_registrar","gestionar_transacciones_editar","gestionar_transacciones_eliminar","gestionar_transacciones_estado"]
    crear_menu(titulo,opciones,funciones)

#------------------------------||-fin - creador Submenus acciones Por Entidad -||--------------------------------------------#



#---------------------------INICIAR - REALIZAR ACCIONES-----------------------------------#

#----------|opciones para Entidad Vehiculos|-------------#
def gestionar_vehiculos_listar():
    vehiculos.listar_vehiculos()
    input("...PRESIONE UNA TECLA PARA CONTINUAR...")
    #--------------------------#
def gestionar_vehiculos_registrar():
    vehiculos.registrar_vehiculos()
    input("...PRESIONE UNA TECLA PARA CONTINUAR...")
    #--------------------------#
def gestionar_vehiculos_editar():
    vehiculos.editar_vehiculos()
    input("...PRESIONE UNA TECLA PARA CONTINUAR...")
    #--------------------------#
def gestionar_vehiculos_eliminar():
    vehiculos.eliminar_vehiculos()
    input("...PRESIONE UNA TECLA PARA CONTINUAR...")
    #--------------------------#
def gestionar_vehiculos_estado():
    vehiculos.estado_vehiculos()
    input("...PRESIONE UNA TECLA PARA CONTINUAR...")
#----------------------------------------------------------#

#----------|opciones para Entidad Clientes|-------------#
def gestionar_clientes_listar():
    clientes.listar_clientes()
    input("...PRESIONE UNA TECLA PARA CONTINUAR...")
    #--------------------------#
def gestionar_clientes_registrar():
    clientes.registrar_clientes()
    input("...PRESIONE UNA TECLA PARA CONTINUAR...")
    #--------------------------#
def gestionar_clientes_editar():
    clientes.editar_clientes()
    input("...PRESIONE UNA TECLA PARA CONTINUAR...")
    #--------------------------#
def gestionar_clientes_eliminar():
    clientes.eliminar_clientes()
    input("...PRESIONE UNA TECLA PARA CONTINUAR...")
    #--------------------------#
def gestionar_clientes_estado():
    clientes.estado_clientes()
    input("...PRESIONE UNA TECLA PARA CONTINUAR...")
#----------------------------------------------------------#

#----------|opciones para Entidad Clientes|-------------#
def gestionar_transacciones_listar():
    transacciones.listar_transacciones()
    input("...PRESIONE UNA TECLA PARA CONTINUAR...")
    #--------------------------#
def gestionar_transacciones_registrar():
    transacciones.registrar_transacciones()
    input("...PRESIONE UNA TECLA PARA CONTINUAR...")
    #--------------------------#
def gestionar_transacciones_editar():
    transacciones.editar_transacciones()
    input("...PRESIONE UNA TECLA PARA CONTINUAR...")
    #--------------------------#
def gestionar_transacciones_eliminar():
    transacciones.eliminar_transacciones()
    input("...PRESIONE UNA TECLA PARA CONTINUAR...")
    #--------------------------#
def gestionar_transacciones_estado():
    transacciones.estado_transacciones()
    input("...PRESIONE UNA TECLA PARA CONTINUAR...")
#----------------------------------------------------------#

#------------------------------FIN - REALIZAR ACCIONES-----------------------------------#
