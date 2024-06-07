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
        print("1. Gestionar Autos")
        print("2. Gestionar Clientes")
        print("3. Gestionar Transacciones")
        print("4. Gestionar Mantenimientos")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            menu_autos()
        elif opcion == '2':
            menu_clientes()
        elif opcion == '3':
            menu_transacciones()
        elif opcion == '4':
            menu_mantenimientos()
        elif opcion == '5':
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")



            #------SUBMENU------#
def menu_autos():
    while True:
        limpiar_consola()
        print("Menú Autos:")
        print("1. Listar Autos")
        print("2. Registrar Auto")
        print("3. Editar Auto")
        print("4. Eliminar Auto")
        print("5. Cambiar Estado de Auto")
        print("6. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            gestionar_autos('Listar')
        elif opcion == '2':
            gestionar_autos('Registrar')
        elif opcion == '3':
            gestionar_autos('Editar')
        elif opcion == '4':
            gestionar_autos('Eliminar')
        elif opcion == '5':
            gestionar_autos('Cambiar Estado')
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




            #------SUBMENU------#
def menu_mantenimientos():
    while True:
        limpiar_consola()
        print("Menú Mantenimientos:")
        print("1. Listar Mantenimientos")
        print("2. Registrar Mantenimiento")
        print("3. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            gestionar_mantenimientos('Listar')
        elif opcion == '2':
            gestionar_mantenimientos('Registrar')
        elif opcion == '3':
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


            #--------INICIAR - REALIZAR ACCIONES--------#
def gestionar_autos(accion):
    limpiar_consola()
    print(f"Gestionar Autos - {accion}:")
    input("...PRESIONE UNA TECLA PARA CONTINUAR...")


def gestionar_clientes(accion):
    limpiar_consola()
    print(f"Gestionar Clientes - {accion}:")
    input("...PRESIONE UNA TECLA PARA CONTINUAR...")

def gestionar_transacciones(accion):
    limpiar_consola()
    print(f"Gestionar Transacciones - {accion}:")
    input("...PRESIONE UNA TECLA PARA CONTINUAR...")

def gestionar_mantenimientos(accion):
    limpiar_consola()
    print(f"Gestionar Mantenimientos - {accion}:")
    input("...PRESIONE UNA TECLA PARA CONTINUAR...")
                #--------  FIN - REALIZAR ACCIONES--------#
    
    

#---------------------------------FIN FUNCIONES AUX DE MENUs-----------------------------------#    