from funciones import clientes
from funciones import vehiculos
from funciones import transacciones
import os



#---------INICIO FUNCIONES CONSOLA------------#
def limpiar_consola():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
#----------FIN FUNCIONES CONSOLA---------------#



#-------------------------------INICIO FUNCIONES AUX DE MENUs-----------------------------------#
def menu_principal():
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
def menu_vehiculos():
    while True:
        limpiar_consola()
        print("Menú Vehiculos:")
        print("1. Listar Vehiculos")
        print("2. Registrar Vehiculo")
        print("3. Editar Vehiculo")
        print("4. Eliminar Vehiculo")
        print("5. Cambiar Estado de Vehiculo")
        print("6. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            gestionar_vehiculos('Listar')
        elif opcion == '2':
            gestionar_vehiculos('Registrar')
        elif opcion == '3':
            gestionar_vehiculos('Editar')
        elif opcion == '4':
            gestionar_vehiculos('Eliminar')
        elif opcion == '5':
            gestionar_vehiculos('Cambiar Estado')
        elif opcion == '6':
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")



            #------SUBMENU------#
def menu_clientes():
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




            #------SUBMENU------#
def menu_transacciones():
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
def gestionar_vehiculos(accion):
    limpiar_consola()
    print(f"Gestionar Vehiculos - {accion}:")
    
    if accion == 'Listar':
        vehiculos.listar_vehiculos();
    elif accion == 'Registrar':
        vehiculos.listar_vehiculos();
    elif accion == 'Eliminar':
        vehiculos.listar_vehiculos();
    elif accion == 'Editar':
        vehiculos.listar_vehiculos();
    elif accion == 'Cambiar Estado':
        vehiculos.listar_vehiculos();
    else:
        print("Opción inválida.")
        
    input("...PRESIONE UNA TECLA PARA CONTINUAR...")




def gestionar_clientes(accion):
    limpiar_consola()
    print(f"Gestionar Clientes - {accion}:")
    if accion == 'Listar':
        clientes.listar_clientes();
    elif accion == 'Registrar':
        clientes.listar_clientes();
    elif accion == 'Eliminar':
        clientes.listar_clientes();
    elif accion == 'Editar':
        clientes.listar_clientes();
    elif accion == 'Cambiar Estado':
        clientes.listar_clientes();
    else:
        print("Opción inválida.")
    
    input("...PRESIONE UNA TECLA PARA CONTINUAR...")




def gestionar_transacciones(accion):
    limpiar_consola()
    print(f"Gestionar Transacciones - {accion}:")
        
    if accion == 'Listar':
        transacciones.listar_transacciones();
    elif accion == 'Registrar':
        transacciones.listar_transacciones();
    elif accion == 'Eliminar':
        transacciones.listar_transacciones();
    elif accion == 'Editar':
        transacciones.listar_transacciones();
    elif accion == 'Cambiar Estado':
        transacciones.listar_transacciones();
    else:
        print("Opción inválida.")
        
    input("...PRESIONE UNA TECLA PARA CONTINUAR...")
                #--------  FIN - REALIZAR ACCIONES--------#
    
    

#---------------------------------FIN FUNCIONES AUX DE MENUs-----------------------------------#    