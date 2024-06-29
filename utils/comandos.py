import config
import tkinter as tk
from tkinter import ttk
from backend.funciones import api
from utils import gui_maker as GM





#----------------------------------------------------------------------------------------------#

def accion():
    print("-----------------------| Boton Presionado |-----------------------------------")
    
def btn_secciones_click(seccion):
    GM.destruir_widget(config.tabla_contenido)
    GM.destruir_widget(config.frame_contenido)
    registros=None
    config.campos=None
    config.tabla_contenido=None
    config.frame_contenido=None
    config.imagen = GM.crear_imagen(canvas_frame=config.lienzo,nombre_imagen="fondos/fondo_index.png",pos_centro_x=1280/2,pos_centro_y=720/2)
    GM.destruir_widget(config.button_agregar)
    GM.destruir_widget(config.button_editar)
    GM.destruir_widget(config.button_eliminar)
    
    if seccion == 'inicio':
        config.seccion_actual='inicio'
        
        
    elif seccion == 'cliente':
        config.seccion_actual='cliente'
        entidad=seccion
        campos = ("id_cliente", "nombre", "apellido", "documento", "direccion", "telefono", "correo_electronico")
        etiquetas = ("ID Cliente", "Nombre", "Apellido", "Documento", "Dirección", "Teléfono", "Correo Electrónico")
        config.campos = campos
        config.frame_contenido = GM.crear_frame(
            config.ventana_principal,
            pos_x=21,
            pos_y=172,
            ancho_frame=1243,
            alto_frame=420,
            color="red"
            )        
        config.tabla_contenido = GM.crear_tabla(
        entidad=seccion,
        padre=config.frame_contenido,
        nombres_de_campos=campos,
        nombres_de_campos_a_mostrar=etiquetas,
        pos_x=0,
        pos_y=0,
        ancho_tabla=1243,
        alto_tabla=420
        )
        crear_botones_acciones(config.frame_contenido)
        
        registros=api.leer_registros(entidad)
        GM.rellenar_tabla(config.tabla_contenido,registros)
        
        
        
    elif seccion == 'vehiculo':
        config.seccion_actual='vehiculo'
        entidad=seccion
        campos = ("id_vehiculo","dominio","marca","modelo","tipo","anio","kilometraje","precio_compra","precio_venta","estado")
        etiquetas = ("ID vehiculo:","Dominio:","Marca:","Modelo:","Tipo:","Año:","Kilometraje:","Precio de Compra:","Precio de Venta:","Estado:")
        config.campos = campos
        config.frame_contenido = GM.crear_frame(
            config.ventana_principal,
            pos_x=21,
            pos_y=172,
            ancho_frame=1243,
            alto_frame=420,
            color="blue"
            )
        config.tabla_contenido = GM.crear_tabla(
        entidad=seccion,
        padre=config.frame_contenido,
        nombres_de_campos=campos,
        nombres_de_campos_a_mostrar=etiquetas,
        pos_x=0,
        pos_y=0,
        ancho_tabla=1243,
        alto_tabla=420
        )
        crear_botones_acciones(config.frame_contenido)
        
        registros=api.leer_registros(entidad)
        GM.rellenar_tabla(config.tabla_contenido,registros)
        
        
        
    elif seccion == 'transaccion':
        config.seccion_actual='transaccion'
        entidad=seccion
        campos = ("id_transaccion","id_vehiculo","id_cliente","tipo_transaccion","fecha","monto","observaciones")
        etiquetas = ("ID Transaccion:","ID Vehiculo:","ID Cliente:","Tipo de Transaccion:","Fecha:","Monto:","Observaciones")
        config.campos = campos
        config.frame_contenido = GM.crear_frame(
            config.ventana_principal,
            pos_x=21,
            pos_y=172,
            ancho_frame=1243,
            alto_frame=420,
            color="orange"
            )
        config.tabla_contenido = GM.crear_tabla(
        entidad=seccion,
        padre=config.frame_contenido,
        nombres_de_campos=campos,
        nombres_de_campos_a_mostrar=etiquetas,
        pos_x=0,
        pos_y=0,
        ancho_tabla=1243,
        alto_tabla=420
        )
        crear_botones_acciones(config.frame_contenido)
        
        registros=api.leer_registros(entidad)
        GM.rellenar_tabla(config.tabla_contenido,registros)
        
        
    else:
        print("Se produjo un error al ejecutar el click - no se escuentra la seccion")





def callback_clic_cabecera(entidad,tabla, campo):
    config.orden = not config.orden    
    registros = api.leer_registros(entidad, [campo, config.orden])
    GM.rellenar_tabla(tabla, registros)
    

def callback_clic_sec_cabecera(entidad, tabla, campo):    
   
    config.ventana_principal
    if config.ventana_principal is not None:
        GM.crear_formulario_de_busqueda(config.ventana_principal, campo,entidad,tabla)
    else:
        print("No se encontró 'root' en config.")
    
    
def callback_clic_registro(entidad,registro):
    config.registro_seleccionado_entidad=entidad
    config.registro_seleccionado_datos=registro
    
def btn_busqueda_por_campo(entidad,filtro):
        
    if entidad == 'cliente':
        campos = ("id_cliente", "nombre", "apellido", "documento", "direccion", "telefono", "correo_electronico")
        etiquetas = ("ID Cliente:", "Nombre:", "Apellido:", "Documento:", "Dirección:", "Teléfono:", "Correo Electrónico:")
    elif entidad == 'vehiculo':
        campos = ("id_vehiculo","dominio","marca","modelo","tipo","anio","kilometraje","precio_compra","precio_venta","estado")
        etiquetas = ("ID vehiculo:","Dominio:","Marca:","Modelo:","Tipo:","Año:","Kilometraje:","Precio de Compra:","Precio de Venta:","Estado:")
    elif entidad == 'transaccion':
        campos = ("id_vehiculo","dominio","marca","modelo","anio","kilometraje","precio_compra","precio_venta","estado")
        etiquetas = ("ID vehiculo:","Dominio:","Marca:","Modelo:","Año:","Kilometraje:","Precio de Compra:","Precio de Venta:","Estado:")

    registros = api.leer_registros(entidad,filtro_aplicado=filtro)
    GM.rellenar_tabla(config.tabla_contenido,registros)
    
def crear_botones_acciones(padre):
    def ventana(seleccion):
        GM.destruir_widget(config.ventana_emergente)
        config.ventana_emergente=None
        if seleccion=="agregar":
            config.ventana_emergente = GM.crear_ventana_emergente(config.ventana_principal,ancho_ventana=1243,alto_ventana=443)
            config.lienzo_emergente = GM.crear_lienzo_canvas(config.ventana_emergente,1243,443,bg_color="red")
            GM.posicionar_canva_fondo(config.lienzo_emergente,pos_x=0,pos_y=0)
            seccion_actual="fondos/form_"+config.seccion_actual+".png"
            print("seccion actual="+seccion_actual)
            config.image = GM.crear_imagen(canvas_frame=config.lienzo_emergente,nombre_imagen=seccion_actual,pos_centro_x=1243/2,pos_centro_y=443/2)
            GM.crear_formulario(config.lienzo_emergente, accion="agregar", seccion=config.seccion_actual, dict_datos=None)
                
            
            
        elif seleccion=="editar":
            if config.seccion_actual==config.registro_seleccionado_entidad:
                config.ventana_emergente = GM.crear_ventana_emergente(config.ventana_principal,ancho_ventana=1243,alto_ventana=443)
                config.lienzo_emergente = GM.crear_lienzo_canvas(config.ventana_emergente,1243,443,bg_color="blue")
                GM.posicionar_canva_fondo(config.lienzo_emergente,pos_x=0,pos_y=0)
                seccion_actual="fondos/form_"+config.seccion_actual+".png"
                print("seccion actual="+seccion_actual)
                config.image = GM.crear_imagen(canvas_frame=config.lienzo_emergente,nombre_imagen=seccion_actual,pos_centro_x=1243/2,pos_centro_y=443/2)
                GM.crear_formulario(config.lienzo_emergente, accion="editar", seccion=config.seccion_actual, dict_datos=config.registro_seleccionado_datos)
                
                
        elif seleccion=="eliminar":
            if config.seccion_actual==config.registro_seleccionado_entidad:
                primer_campo = next(iter(config.registro_seleccionado_datos.items()))
                id_eliminar = {primer_campo[0]: int(primer_campo[1])}
                api.baja_registro(config.registro_seleccionado_entidad,id_eliminar)
                btn_secciones_click(config.seccion_actual)
            
        else:
            print("hubo un error")
        
    config.button_agregar = GM.crear_boton(config.ventana_principal,"botones/btn_agregar.png")
    config.button_agregar.config(command=lambda: ventana("agregar"))
    config.button_editar = GM.crear_boton(config.ventana_principal,"botones/btn_editar.png")
    config.button_editar.config(command=lambda: ventana("editar"))
    config.button_eliminar = GM.crear_boton(config.ventana_principal,"botones/btn_eliminar.png")
    config.button_eliminar.config(command=lambda: ventana("eliminar"))
    
    
    GM.posicionar_boton(config.button_agregar,pos_x=373,pos_y=595)
    GM.posicionar_boton(config.button_editar,pos_x=568,pos_y=595)
    GM.posicionar_boton(config.button_eliminar,pos_x=763,pos_y=595)
    
    
def alta_registro(datos_dict):
    api.alta_registro(config.seccion_actual,datos_dict)
    
def editar_registro(dic_editar,datos_dict):
    api.modificar_registro(config.seccion_actual,dic_editar,datos_dict)