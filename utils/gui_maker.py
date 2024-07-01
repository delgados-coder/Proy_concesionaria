from backend.funciones import api
import os
import config
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, ttk, messagebox, font as tkfont
from utils import comandos as comando
from pathlib import Path

OUTPUT_PATH = Path(__file__).parent
OUTPUT_PATH_UP_ONE = OUTPUT_PATH.parent
ASSETS_PATH = OUTPUT_PATH_UP_ONE / Path(r".\recursos\imagenes")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

#|---------------|funciones - eliminar|--------------------#
def destruir_widget(widget):
    if widget is not None:
        widget.destroy()

#|---------------|funciones - Ventana PRINCIPAL|--------------------#
def crear_ventana_principal(ancho_ventana=100,alto_ventana=100,titulo_ventana="default",icon_path=None,color_base="green"):
    window_root = Tk()
    screen_width = window_root.winfo_screenwidth()       
    screen_height = window_root.winfo_screenheight()
    window_width = ancho_ventana  
    window_height = alto_ventana
    x_cordinate = int((screen_width / 2) - (window_width / 2)) 
    y_cordinate = int((screen_height / 2) - (window_height / 2)) 
        
    window_root.title(titulo_ventana)
    window_root.iconbitmap(icon_path)
    window_root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    window_root.configure(background=color_base)
    window_root.resizable(False, False)
    return window_root    

#|---------------|funciones - Ventana emergente|--------------------#

def crear_ventana_emergente(padre,ancho_ventana=100,alto_ventana=100,titulo_ventana="Formulario",color_base="white"):
    ventana_emergente = tk.Toplevel(padre)
    screen_width = ventana_emergente.winfo_screenwidth()       
    screen_height = ventana_emergente.winfo_screenheight()
    window_width = ancho_ventana  
    window_height = alto_ventana
    x_cordinate = int((screen_width / 2) - (window_width / 2)) 
    y_cordinate = int((screen_height / 2) - (window_height / 2)) 
        
    ventana_emergente.title(titulo_ventana)
    ventana_emergente.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    ventana_emergente.configure(background=color_base)
    ventana_emergente.resizable(True, True)
    return ventana_emergente    


#|---------------|funciones - lienzo canvas|--------------------#
def crear_lienzo_canvas(ventana_padre,ancho,alto,bg_color="#989A9A"):
    frame_canvas = Canvas(
    ventana_padre,
    bg = bg_color,
    height = alto,
    width = ancho,
    bd = 0,
    highlightthickness = 0,
    relief = "flat"    
    )
    return frame_canvas

def posicionar_canva_fondo(canvas_frame,pos_x=0,pos_y=0):
    canvas_frame.place(x=pos_x,y=pos_y)

#|---------------|Funciones de imagenes-fondo|--------------------#
def crear_imagen2(canvas_frame,nombre_imagen,pos_centro_x=0,pos_centro_y=0):
    cargar_imagen = PhotoImage(file=relative_to_assets(nombre_imagen))
    medida1=pos_centro_x
    medida2=pos_centro_y
    cargar_imagen.image = cargar_imagen
    return canvas_frame.create_image(medida1,medida2, image=cargar_imagen)

#|---------------|Funciones de imagenes-arreglo de fondo|--------------------#
'''Este crear imagen es necesario por más que repita code porque arrastra el error de que no encuentra la imagen y lo repara si se lo hace en un mismo archivo rompe al no poder
procesar la imagen y repararla en la misma funcion'''
def crear_imagen(canvas_frame, nombre_imagen, pos_centro_x=0, pos_centro_y=0):
    imagen_path = relative_to_assets(nombre_imagen)
    if os.path.isfile(imagen_path):
        cargar_imagen = PhotoImage(file=imagen_path)
        canvas_frame.image = cargar_imagen
        medida1=int(pos_centro_x)
        medida2=int(pos_centro_y)
        canvas_frame.create_image(medida1, medida2, image=cargar_imagen)
    else:
        print(f"La imagen {nombre_imagen} no existe en la ruta especificada.")
        canvas_frame.after(1000, lambda: crear_imagen(canvas_frame, nombre_imagen, medida1, medida2))


#|---------------|Funciones de rectangulos|--------------------#
def crear_rectangulo(canvas_frame,pos_x=0,pos_y=0,ancho=10,alto=10,fondo="green"):
    canvas_frame.create_rectangle(pos_x,pos_y,pos_x+ancho,pos_y+alto,fill=fondo,outline="")

#|---------------|funciones - frame|--------------------#
def crear_frame(padre, pos_x=20, pos_y=20, ancho_frame=200, alto_frame=200, color="green"):
    frame = Frame(padre, width=ancho_frame, height=alto_frame, bg=color)
    frame.place(x=pos_x, y=pos_y)
    return frame

#|---------------|Funciones de BOTONED|--------------------#
def crear_boton(ventana_padre,nombre_boton):
    btn_image = PhotoImage(file=relative_to_assets(nombre_boton))
    btn_name = Button(
     ventana_padre,
     cursor="hand2",
     image=btn_image,
     borderwidth=0,
     highlightthickness=0,
     relief="flat"
    )
    btn_name.image = btn_image
    return btn_name

def posicionar_boton(boton,pos_x=0,pos_y=0,ancho=None,alto=None):
    boton.place(
        x=pos_x,
        y=pos_y,
        width=ancho,
        height=alto
    )
#|---------------|Funciones de Textos|--------------------#
def crear_texto(padre, texto="default", pos_x=0, pos_y=0, color_fuente="blue", size_fuente=10, tipo_fuente="Arial"):
    etiqueta = tk.Label(padre, text=texto, fg=color_fuente, font=(tipo_fuente, size_fuente), background="#C3DBEB")
    etiqueta.place(x=pos_x, y=pos_y)
    
#|---------------|Funciones de Tablas|--------------------#
def crear_tabla(entidad, padre, nombres_de_campos, nombres_de_campos_a_mostrar, pos_x=0, pos_y=0, ancho_tabla=1000, alto_tabla=500):
    def ajustar_ancho_columnas(event=None):
        total_columnas = len(nombres_de_campos)
        if not tabla.get_children():  # Si no hay datos en la tabla
            ancho_por_columna = tabla.winfo_width() // total_columnas
            for columna in nombres_de_campos:
                tabla.column(columna, width=ancho_por_columna)
        else:
            for columna in nombres_de_campos:
                max_ancho = max(
                    tkfont.Font().measure(tabla.heading(columna, 'text')),
                    max(tkfont.Font().measure(tabla.set(item, columna)) for item in tabla.get_children())
                )
                tabla.column(columna, width=max_ancho)

    style = ttk.Style()
    style.configure("mystyle.Treeview", highlightthickness=5, bd=3, font=('Arial', 13))  
    style.configure("mystyle.Treeview", rowheight=25, bordercolor="black", borderwidth=2)
    style.map("mystyle.Treeview", background=[('selected', 'gray')], foreground=[('selected', 'white')])  
        
    tabla = ttk.Treeview(padre, columns=nombres_de_campos, show='headings', style='mystyle.Treeview')
    tabla.place(x=pos_x, y=pos_y, width=ancho_tabla, height=alto_tabla)

    for campo, etiqueta in zip(nombres_de_campos, nombres_de_campos_a_mostrar):
        tabla.heading(campo, text=etiqueta)
    
    
    def registro_click(event):
        region = tabla.identify('region', event.x, event.y)
        if region == 'cell':
            item = tabla.selection()
            if item:
                registro = {campo: tabla.item(item, 'values')[i] for i, campo in enumerate(nombres_de_campos)}
                comando.callback_clic_registro(entidad, registro)
                
    def encabezado_click(event):
        region = tabla.identify('region', event.x, event.y)
        if region == 'heading': 
            columna_id = tabla.identify_column(event.x)
            columna = int(columna_id.replace('#', '')) - 1
            campo = nombres_de_campos[columna]
            comando.callback_clic_cabecera(entidad, tabla, campo)  
    
    def encabezado_click_derecho(event):
        region = tabla.identify('region', event.x, event.y)
        if region == 'heading':
            columna_id = tabla.identify_column(event.x)
            columna = int(columna_id.replace('#', '')) - 1
            campo = nombres_de_campos[columna]
            comando.callback_clic_sec_cabecera(entidad, tabla, campo)   
    
    
    tabla.bind('<Configure>', ajustar_ancho_columnas)
    tabla.bind('<ButtonRelease-1>', registro_click)
    tabla.bind('<Button-3>', encabezado_click)
    tabla.bind('<Button-1>', encabezado_click_derecho)
    
    return tabla

def rellenar_tabla(tabla_a_rellenar, datos_a_utilizar):
    for item in tabla_a_rellenar.get_children():
        tabla_a_rellenar.delete(item)
    for _, registro in datos_a_utilizar.iterrows():
        tabla_a_rellenar.insert('', 'end', values=registro.tolist())

def crear_formulario_de_busqueda(ventana_padre, campo, entidad, tabla):
    ventana_hija = tk.Toplevel(ventana_padre)
    screen_width = ventana_hija.winfo_screenwidth()       
    screen_height = ventana_hija.winfo_screenheight()
    window_width = 500  
    window_height = 100
    x_cordinate = int((screen_width / 2) - (window_width / 2)) 
    y_cordinate = int((screen_height / 2) - (window_height / 2))
    ventana_hija.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    ventana_hija.title(f"Buscar por {campo}")
    
    label_principal = tk.Label(ventana_hija, text=f"Buscar por {campo}")
    label_principal.pack(pady=10)
    
    frame_formulario = ttk.Frame(ventana_hija)
    frame_formulario.pack(padx=10, pady=10)
    
    label_buscar = ttk.Label(frame_formulario, text="Buscar:")
    label_buscar.grid(row=0, column=0, padx=5, pady=5)
    
    entry_buscar = ttk.Entry(frame_formulario)
    entry_buscar.grid(row=0, column=1, padx=5, pady=5)
    
    def obtener_valor():
        valor_buscar = entry_buscar.get()
        if valor_buscar.isdigit():
            valor_buscar = int(valor_buscar)
        filtro = {campo: valor_buscar}
        comando.btn_busqueda_por_campo(entidad, filtro)

    
    boton_buscar = ttk.Button(frame_formulario, text="Buscar", command=obtener_valor)
    boton_buscar.grid(row=0, column=2, padx=5, pady=5) 

#---------------------------------------------------------------------------------------#
def crear_formulario(padre, accion, seccion, pos_x=100, pos_y=100, dict_datos=None):
    campos_clie = ["nombre", "apellido", "documento", "direccion", "telefono", "correo_electronico"]
    campos_vehi = ["dominio","marca","modelo","tipo","anio","kilometraje","precio_compra","precio_venta","estado"]
    campos_tran = ["id_vehiculo","id_cliente","tipo_transaccion","fecha","monto","observaciones"]
    
    if seccion == "cliente":
        campos = campos_clie
        
        
    elif seccion == "vehiculo":
        campos = campos_vehi
        
        
    elif seccion == "transaccion":
        campos = campos_tran
        
        
    else:
        raise ValueError("Sección no válida")
    
   
    entries = {}
    for i, campo in enumerate(campos):
          
        entrada = tk.Entry(padre,background="#C3DBEB", relief="flat")
        
        if accion == "editar" and dict_datos is not None:
            entrada.insert(0, dict_datos.get(campo, ""))
        
        entrada.place(x=pos_x+15, y=pos_y + i*49 +2, width=272)  #x30
        entries[campo] = entrada                 
    
    button_aceptar = crear_boton(padre, "botones/btn_aceptar.png")
    button_aceptar.config(command=lambda: aceptar(entries, accion, seccion))
    posicionar_boton(button_aceptar, pos_x=241, pos_y=549)

def aceptar(entries, accion, seccion):
    datos = {}
    for campo, entry in entries.items():
        valor = entry.get()
        if valor.isdigit():
            datos[campo] = int(valor)
        else:
            datos[campo] = valor
    print(f"Acción: {accion}, Sección: {seccion}, Datos: {datos}")

    primer_registro = list(config.registro_seleccionado_datos.items())[0]
    clave_primer_registro = primer_registro[0]
    valor_primer_registro = primer_registro[1]
    clave_valor_id = {clave_primer_registro: int(valor_primer_registro)}
    id_entidad = valor_primer_registro
    dic_sin_id = {k: v for k, v in datos.items() if k != clave_primer_registro}

    print("primer_registro =", primer_registro)
    print("clave_primer_registro =", clave_primer_registro)
    print("valor_primer_registro =", valor_primer_registro)
    print("clave_valor_id =", clave_valor_id)
    print("id_entidad =", id_entidad)
    print("dic_sin_id =", dic_sin_id)
    
    if accion == 'agregar':
        api.alta_registro(seccion, datos)
        destruir_widget(widget=config.ventana_emergente)
        comando.btn_secciones_click(seccion)
        
    elif accion == 'editar':
        api.modificar_registro(seccion, clave_valor_id, dic_sin_id)
        destruir_widget(widget=config.ventana_emergente)
        comando.btn_secciones_click(seccion)
    else:
        print("Se produjo un error")