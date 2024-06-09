def menu_clientes():
    print("Menú de clientes")

def menu_vehiculos():
    print("Menú de vehículos")

def menu_transaccion():
    print("Menú de transacciones")

valores = [menu_clientes, menu_vehiculos, menu_transaccion]

op = 1

funcion_A_ejecutar = valores[op]

if 0 <= op < len(valores):
    valores[op]()  
else:
    print("La función especificada no existe")
