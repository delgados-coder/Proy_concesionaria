import config
import tkinter as tk
from tkinter import ttk
from backend.funciones import api
from utils import auxiliares as aux




#----------------------------------------------------------------------------------------------#

def accion():
    print("-----------------------| Boton Presionado |-----------------------------------")


def btn_inicio_click():
    print("btn_inicio_click():")
    
    
def btn_clientes_click(padre):
    entidad='cliente'
    campos = ("id_cliente", "nombre", "apellido", "documento", "direccion", "telefono", "correo_electronico")
    etiquetas = ("ID Cliente", "Nombre", "Apellido", "Documento", "Dirección", "Teléfono", "Correo Electrónico")
    registros = api.leer_registros('cliente')
    main_tabla_registros = aux.crear_tabla(entidad,padre, campos, etiquetas)
    aux.rellenar_tabla(main_tabla_registros,registros)
    
def btn_vehiculos_click(padre):
    entidad='vehiculo'
    campos = ("id_vehiculo","dominio","marca","modelo","anio","kilometraje","precio_compra","precio_venta","estado")
    etiquetas = ("ID vehiculo","Dominio","Marca","Modelo","Año","Kilometraje","Precio de Compra","Precio de Venta","Estado")
    registros = api.leer_registros('vehiculo')
    main_tabla_registros = aux.crear_tabla(entidad,padre, campos, etiquetas)
    aux.rellenar_tabla(main_tabla_registros,registros)
    
    
def btn_transacciones_click(padre):
    entidad='transaccion'
    campos = ("id_transaccion","id_vehiculo","id_cliente","tipo_transaccion","fecha","monto","observaciones")
    etiquetas = ("ID Transaccion","ID Vehiculo","ID Cliente","Tipo de Transaccion","Fecha","Monto","Observaciones")
    registros = api.leer_registros('transaccion')
    main_tabla_registros = aux.crear_tabla(entidad,padre, campos, etiquetas)
    aux.rellenar_tabla(main_tabla_registros,registros)
    
def btn_busqueda_por_campo(entidad,filtro):
        
    if entidad == 'cliente':
        campos = ("id_cliente", "nombre", "apellido", "documento", "direccion", "telefono", "correo_electronico")
        etiquetas = ("ID Cliente", "Nombre", "Apellido", "Documento", "Dirección", "Teléfono", "Correo Electrónico")
    elif entidad == 'vehiculo':
        campos = ("id_vehiculo","dominio","marca","modelo","anio","kilometraje","precio_compra","precio_venta","estado")
        etiquetas = ("ID vehiculo","Dominio","Marca","Modelo","Año","Kilometraje","Precio de Compra","Precio de Venta","Estado")
    elif entidad == 'transaccion':
        campos = ("id_vehiculo","dominio","marca","modelo","anio","kilometraje","precio_compra","precio_venta","estado")
        etiquetas = ("ID vehiculo","Dominio","Marca","Modelo","Año","Kilometraje","Precio de Compra","Precio de Venta","Estado")

    registros = api.leer_registros(entidad,filtro_aplicado=filtro)
    main_tabla_registros = aux.crear_tabla(entidad,config.main_table, campos, etiquetas)
    aux.rellenar_tabla(main_tabla_registros,registros)
    

def callback_clic_cabecera(entidad,tabla, campo):    
    registros = api.leer_registros(entidad, [campo, True])
    aux.rellenar_tabla(tabla, registros)
    

def callback_clic_sec_cabecera(entidad, tabla, campo):    
    print(f"ENTIDAD: {entidad}")
    print(f"TABLA: {tabla}")
    
    root = config.root
    if root is not None:
        aux.crear_formulario_de_busqueda(root, campo,entidad,tabla)
    else:
        print("No se encontró 'root' en config.")
    
    
def callback_clic_registro(entidad,registro):
    print("Registro seleccionado:", registro)
    return registro
    