import os
from funciones.entidades import clientes
from funciones.entidades import vehiculos
from funciones.entidades import transacciones



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
                input(nombre_funcion)
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

def menu_vehiculos():
    input("MENU VEHICULOS ... ")
    
    titulo='Gestionar Vehiculos'
    opciones=["Listar Vehiculos","Registrar Vehiculos","Editar Vehiculos","Eliminar Vehiculos","Cambiar Estado Vehiculo"]
    funciones=["gestionar_vehiculos_listar","gestionar_vehiculos_registrar","gestionar_vehiculos_editar","gestionar_vehiculos_eliminar","gestionar_vehiculos_estado"]
    crear_menu(titulo,opciones,funciones)
    


    
#-------------------------------INICIO FUNCIONES AUX DE MENUs-----------------------------------#
def menu_principal(): #---------------| MENU ANTIGUO(primeras versiones)...ahora se utiliza CREADOR MENU DINAMICO (func: crear_menu('titulo','opciones','funciones'))
    while True:
        limpiar_consola()
        print("Menú Principal:")
        print("1. Gestionar Vehiculos")
        print("2. Gestionar Clientes")
        print("3. Gestionar Transacciones")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            menu_vehiculos()
        elif opcion == '2':
            menu_clientes()
        elif opcion == '3':
            menu_transacciones()
        elif opcion == '4':
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")



            #------SUBMENU------#
# def menu_vehiculos():#---------------| MENU ANTIGUO(primeras versiones)...ahora se utiliza CREADOR MENU DINAMICO (func: crear_menu('titulo','opciones','funciones'))
#     while True:
#         limpiar_consola()
#         print("Menú Vehiculos:")
#         print("1. Listar Vehiculos")
#         print("2. Registrar Vehiculo")
#         print("3. Editar Vehiculo")
#         print("4. Eliminar Vehiculo")
#         print("5. Cambiar Estado de Vehiculo")
#         print("6. Volver al Menú Principal")
#         opcion = input("Seleccione una opción: ")

#         if opcion == '1':
#             gestionar_vehiculos('Listar')
#         elif opcion == '2':
#             gestionar_vehiculos('Registrar')
#         elif opcion == '3':
#             gestionar_vehiculos('Editar')
#         elif opcion == '4':
#             gestionar_vehiculos('Eliminar')
#         elif opcion == '5':
#             gestionar_vehiculos('Estado')
#         elif opcion == '6':
#             break
#         else:
#             print("Opción inválida. Por favor, seleccione una opción válida.")

            #------SUBMENU------#
            
def menu_clientes():#---------------| MENU ANTIGUO(primeras versiones)...ahora se utiliza CREADOR MENU DINAMICO (func: crear_menu('titulo','opciones','funciones'))
    while True:
        limpiar_consola()
        print("Menú Clientes:")
        print("1. Listar Clientes")
        print("2. Registrar Cliente")
        print("3. Editar Cliente")
        print("4. Eliminar Cliente")
        print("5. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            gestionar_clientes('Listar')
        elif opcion == '2':
            gestionar_clientes('Registrar')
        elif opcion == '3':
            gestionar_clientes('Editar')
        elif opcion == '4':
            gestionar_clientes('Eliminar')
        elif opcion == '5':
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


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


            #------SUBMENU------#
def menu_transacciones():#---------------| MENU ANTIGUO(primeras versiones)...ahora se utiliza CREADOR MENU DINAMICO (func: crear_menu('titulo','opciones','funciones'))
    while True:
        limpiar_consola()
        print("Menú Transacciones:")
        print("1. Listar Transacciones")
        print("2. Registrar Transacción")
        print("3. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            gestionar_transacciones('Listar')
        elif opcion == '2':
            gestionar_transacciones('Registrar')
        elif opcion == '3':
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

            #--------INICIAR - REALIZAR ACCIONES--------#
            
#---------------| MENU ANTIGUO(primeras versiones)...ahora se utiliza CREADOR MENU DINAMICO (func: crear_menu('titulo','opciones','funciones'))            
def gestionar_vehiculos(accion):
    limpiar_consola()
    print(f"Gestionar Vehiculos - {accion}:")
    
    if accion == 'Listar':
        vehiculos.listar_vehiculos();
    elif accion == 'Registrar':
        vehiculos.registrar_vehiculos();
    elif accion == 'Eliminar':
        vehiculos.eliminar_vehiculos();
    elif accion == 'Editar':
        vehiculos.editar_vehiculos();
    elif accion == 'Estado':
        vehiculos.estado_vehiculos();
    else:
        print("Opción inválida.")
        
    input("...PRESIONE UNA TECLA PARA CONTINUAR...")

#---------------| MENU ANTIGUO(primeras versiones)...ahora se utiliza CREADOR MENU DINAMICO (func: crear_menu('titulo','opciones','funciones'))
def gestionar_clientes(accion):
    limpiar_consola()
    print(f"Gestionar Clientes - {accion}:")
    if accion == 'Listar':
        clientes.listar_clientes();
    elif accion == 'Registrar':
        clientes.registrar_clientes();
    elif accion == 'Eliminar':
        clientes.elimnar_clientes();
    elif accion == 'Editar':
        clientes.editar_clientes();
    else:
        print("Opción inválida.")
    
    input("...PRESIONE UNA TECLA PARA CONTINUAR...")



#---------------| MENU ANTIGUO(primeras versiones)...ahora se utiliza CREADOR MENU DINAMICO (func: crear_menu('titulo','opciones','funciones'))
def gestionar_transacciones(accion):
    limpiar_consola()
    print(f"Gestionar Transacciones - {accion}:")
        
    if accion == 'Listar':
        transacciones.listar_transacciones();
    elif accion == 'Registrar':
        transacciones.registrar_transacciones();
    else:
        print("Opción inválida.")
        
    input("...PRESIONE UNA TECLA PARA CONTINUAR...")
                #--------  FIN - REALIZAR ACCIONES--------#
    
    

#---------------------------------FIN FUNCIONES AUX DE MENUs-----------------------------------#    