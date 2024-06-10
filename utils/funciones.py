import tkinter as tk
from tkinter import ttk

def front_crear_ventana_hija(ventana_padre,nombre_de_ventana):
    ventana_hija = tk.Toplevel(ventana_padre)
    ventana_hija.title(nombre_de_ventana)
    etiqueta = tk.Label(ventana_hija, text="Esta es una ventana hija")
    etiqueta.pack()

def front_crear_tabla(ventana_padre, nombres_de_campos, nombres_de_campos_a_mostrar, **adiocionales):
    tabla = ttk.Treeview(ventana_padre, columns=nombres_de_campos, show='headings', **adiocionales)
    tabla.pack(expand=True, fill='both')
    for campo, etiqueta in zip(nombres_de_campos, nombres_de_campos_a_mostrar): # zip para unir(NOMBRES DE CAMPOS con la etiqueta a mostrar en LA COLUMNA)
        tabla.heading(campo, text=etiqueta)
    return tabla

#ejemplo
# campos = ("id_cliente", "name", "surname", "doc", "dir", "tel", "email")
# etiquetas = ("ID Cliente", "Nombre", "Apellido", "Documento", "Dirección", "Teléfono", "Correo Electrónico")
# tabla_clientes = front_crear_tabla(root, campos, etiquetas)


def front_rellenar_tabla(tabla_a_rellenar, datos_a_utilizar,):
    for _, registro in datos_a_utilizar.iterrows():
        tabla_a_rellenar.insert('', 'end', values=registro.tolist())
       
        
def front_rellenar_tabla_serie(tabla_a_rellenar, datos_a_utilizar):
    for index, registro in datos_a_utilizar.iteritems():
        tabla_a_rellenar.insert('', 'end', values=registro)