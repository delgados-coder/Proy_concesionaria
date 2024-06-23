import tkinter as tk
from tkinter import ttk

#------------| FUNCIONES FRONT PARA CREAR (ventana, formulario, tabla)|----------------#
def front_crear_ventana_hija(ventana_padre,nombre_de_ventana):
    ventana_hija = tk.Toplevel(ventana_padre)
    ventana_hija.title(nombre_de_ventana)
    etiqueta = tk.Label(ventana_hija, text="Esta es una ventana hija")
    etiqueta.pack()

# def front_crear_tabla(ventana_padre, nombres_de_campos, nombres_de_campos_a_mostrar, **adiocionales):
#     tabla = ttk.Treeview(ventana_padre, columns=nombres_de_campos, show='headings', **adiocionales)
#     tabla.pack(expand=True, fill='both')
#     for campo, etiqueta in zip(nombres_de_campos, nombres_de_campos_a_mostrar): # zip para unir(NOMBRES DE CAMPOS con la etiqueta a mostrar en LA COLUMNA)
#         tabla.heading(campo, text=etiqueta)
#     return tabla

def front_crear_tabla(ventana_padre, nombres_de_campos, nombres_de_campos_a_mostrar, callback_clic_cabecera,callback_clic_registro, **adiocionales):
    tabla = ttk.Treeview(ventana_padre, columns=nombres_de_campos, show='headings', **adiocionales)
    tabla.pack(expand=True, fill='both')

    for campo, etiqueta in zip(nombres_de_campos, nombres_de_campos_a_mostrar):
        tabla.heading(campo, text=etiqueta)
    

    def encabezado_click(event):
        region = tabla.identify('region', event.x, event.y)
        if region == 'heading': 
            columna_id = tabla.identify_column(event.x)
            columna = int(columna_id.replace('#', '')) - 1
            campo = nombres_de_campos[columna]
            callback_clic_cabecera(tabla, campo)


    def registro_click(event):
        region = tabla.identify('region', event.x, event.y)
        if region == 'cell':
            item = tabla.selection()
            if item:
                registro = {campo: tabla.item(item, 'values')[i] for i, campo in enumerate(nombres_de_campos)}
                callback_clic_registro(registro)    

    tabla.bind('<ButtonRelease-1>', encabezado_click)
    tabla.bind('<Button-1>', registro_click)

    return tabla

#ejemplo
# campos = ("id_cliente", "name", "surname", "doc", "dir", "tel", "email")
# etiquetas = ("ID Cliente", "Nombre", "Apellido", "Documento", "Dirección", "Teléfono", "Correo Electrónico")
# tabla_clientes = front_crear_tabla(root, campos, etiquetas)


def crear_formulario(ventana_padre,nombre_form, campos):

    valores_campos = {}

    for i, campo in enumerate(campos):
        label = ttk.Label(ventana_padre, text=campo)
        label.grid(row=i, column=0, padx=10, pady=5)

        entry = ttk.Entry(ventana_padre)
        entry.grid(row=i, column=1, padx=10, pady=5)

        valores_campos[campo] = entry



#------------| FUNCIONES FRONT PARA rellenar tablas con datos desde el backend|----------------#
def front_rellenar_tabla(tabla_a_rellenar, datos_a_utilizar):
    for item in tabla_a_rellenar.get_children():
        tabla_a_rellenar.delete(item)
    for _, registro in datos_a_utilizar.iterrows():
        tabla_a_rellenar.insert('', 'end', values=registro.tolist())
       
        
def front_rellenar_tabla_serie(tabla_a_rellenar, datos_a_utilizar):
    for index, registro in datos_a_utilizar.iteritems():
        tabla_a_rellenar.insert('', 'end', values=registro)
        
        


