import tkinter as tk
from tkinter import ttk
from backend.funciones import api
from utils import comandos as comando


def ajustar_ancho_columnas(tabla, nombres_de_campos):
    for col in nombres_de_campos:
        max_length = max(len(str(tabla.set(item, col))) for item in tabla.get_children())
        max_length = max(max_length, len(col)) 
        tabla.column(col, width=(max_length * 2))  




def crear_tabla(entidad,ventana_padre, nombres_de_campos, nombres_de_campos_a_mostrar,**adicionales):
    for widget in ventana_padre.winfo_children():
        if isinstance(widget, ttk.Treeview):
            widget.destroy()
    
    style = ttk.Style()
    style.configure("mystyle.Treeview", highlightthickness=5, bd=3, font=('Helvetica', 15))  
    style.configure("mystyle.Treeview", rowheight=25, bordercolor="black", borderwidth=2)
    style.map("mystyle.Treeview", background=[('selected', 'red')], foreground=[('selected', 'white')])  
        
    tabla = ttk.Treeview(ventana_padre, columns=nombres_de_campos, show='headings', style='mystyle.Treeview', **adicionales)
    tabla.pack(expand=True, fill='both')

    for campo, etiqueta in zip(nombres_de_campos, nombres_de_campos_a_mostrar):
        tabla.heading(campo, text=etiqueta)
    
    tabla.bind('<Map>', lambda event: ajustar_ancho_columnas(tabla, nombres_de_campos))
    
    
    
    def encabezado_click(event):
        region = tabla.identify('region', event.x, event.y)
        if region == 'heading': 
            columna_id = tabla.identify_column(event.x)
            columna = int(columna_id.replace('#', '')) - 1
            campo = nombres_de_campos[columna]
            comando.callback_clic_cabecera(entidad, tabla, campo)

    def registro_click(event):
        region = tabla.identify('region', event.x, event.y)
        if region == 'cell':
            item = tabla.selection()
            if item:
                registro = {campo: tabla.item(item, 'values')[i] for i, campo in enumerate(nombres_de_campos)}
                comando.callback_clic_registro(entidad, registro)
    
    def encabezado_click_derecho(event):
        region = tabla.identify('region', event.x, event.y)
        if region == 'heading':
            columna_id = tabla.identify_column(event.x)
            columna = int(columna_id.replace('#', '')) - 1
            campo = nombres_de_campos[columna]
            comando.callback_clic_sec_cabecera(entidad, tabla, campo) 
            

    tabla.bind('<Button-1>', encabezado_click)
    tabla.bind('<Button-3>', encabezado_click_derecho)
    tabla.bind('<ButtonRelease-1>', registro_click)
    
    return tabla





def rellenar_tabla(tabla_a_rellenar, datos_a_utilizar):
    for item in tabla_a_rellenar.get_children():
        tabla_a_rellenar.delete(item)
    for _, registro in datos_a_utilizar.iterrows():
        tabla_a_rellenar.insert('', 'end', values=registro.tolist())
        
        
        
        
        
def crear_ventana_hija(ventana_padre,nombre_de_ventana):
    ventana_hija = tk.Toplevel(ventana_padre)
    screen_width = ventana_hija.winfo_screenwidth()       
    screen_height = ventana_hija.winfo_screenheight()
    window_width = 500  
    window_height = 500
    x_cordinate = int((screen_width / 2) - (window_width / 2)) 
    y_cordinate = int((screen_height / 2) - (window_height / 2))
    ventana_hija.title(nombre_de_ventana)
    ventana_hija.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    etiqueta = tk.Label(ventana_hija, text="Esta es una ventana hija")
    
    
    etiqueta.pack()
    return ventana_hija
    
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
        filtro = {campo: valor_buscar}
        comando.btn_busqueda_por_campo(entidad, filtro)
    
    boton_buscar = ttk.Button(frame_formulario, text="Buscar", command=obtener_valor)
    boton_buscar.grid(row=0, column=2, padx=5, pady=5)
    
    
    
    
def crear_formulario(ventana_padre,nombre_form, campos):

    valores_campos = {}

    for i, campo in enumerate(campos):
        label = ttk.Label(ventana_padre, text=campo)
        label.grid(row=i, column=0, padx=10, pady=5)

        entry = ttk.Entry(ventana_padre)
        entry.grid(row=i, column=1, padx=10, pady=5)

        valores_campos[campo] = entry
        
        
