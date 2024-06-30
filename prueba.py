from backend.funciones import api

tabla = api.leer_registros("transaccion")
print(tabla[0])
print("Total Compras:",tabla[1])
print("Total Ventas:",tabla[2])