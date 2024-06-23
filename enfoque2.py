
from utils import funciones as front_funciones
from utils import comandos as comando
from backend.funciones import api
import random
import tkinter as tk
from tkinter import font

root_titulo="CONCESIONARIA <-UnerAutos S.A.->"
root_color_base="#001B2E"
root_path_icon="./favicon.ico"
elementos=[]
orden=True


def color_aleatorio():
    color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    return color


def mi_callback_clic_cabecera(tabla, campo):
    print(f"Se hizo clic en el encabezado de la columna: {campo}")
    registros = api.leer_registros('cliente', [campo, orden])
    front_funciones.front_rellenar_tabla(tabla, registros)
    
def mi_callback_clic_registro(registro):
    print("Registro seleccionado:", registro)
    return registro


def main():
    root = tk.Tk()
    
    
    screen_width= root.winfo_screenwidth()       
    screen_height= root.winfo_screenheight()
    window_width = screen_width-300  
    window_height = screen_height-300
    x_cordinate = int((screen_width/2) - (window_width/2)) 
    y_cordinate = int((screen_height/2) - (window_height/2)) 
    
    
    root.title(root_titulo)
    root.iconbitmap(root_path_icon)
    root.geometry("{}x{}+{}+{}".format(window_width,window_height,x_cordinate,y_cordinate))
    root.configure(background=root_color_base)
    
    bold_font = font.Font(family="Helvetica", size=12, weight="bold")
    
    

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
  
#-------------------------------| SECTIONS / GRID AREAS |-------------------------------------------#    
    root_windows = {
        "header": tk.Frame(root, bg=color_aleatorio(), bd=2, relief=tk.SUNKEN),
        "tittle": tk.Frame(root, bg=color_aleatorio(), bd=2, relief=tk.SUNKEN),
        "aside": tk.Frame(root, bg=color_aleatorio(), bd=2, relief=tk.SUNKEN),
        "main": tk.Frame(root, bg=color_aleatorio(), bd=2, relief=tk.SUNKEN)
    }
    
    header_windows = {
        "h_1": tk.Frame(root_windows["header"], bg=color_aleatorio(), bd=2, relief=tk.SUNKEN),
        "section": tk.Frame(root_windows["header"], bg=color_aleatorio(), bd=2, relief=tk.SUNKEN),
        "close": tk.Frame(root_windows["header"], bg=color_aleatorio(), bd=2, relief=tk.SUNKEN),
    }
    
    aside_windows = {
        "user_img": tk.Frame(root_windows["aside"], bg=color_aleatorio(), bd=2, relief=tk.SUNKEN),
        "options": tk.Frame(root_windows["aside"], bg=color_aleatorio(), bd=2, relief=tk.SUNKEN),
    }
    
    main_windows = {
        "tabla_registros": tk.Frame(root_windows["main"], bg=color_aleatorio(), bd=2, relief=tk.SUNKEN),
        "tabla_acciones": tk.Frame(root_windows["main"], bg=color_aleatorio(), bd=2, relief=tk.SUNKEN),
    }
#-------------------------------| SECTIONS / GRID AREAS |-------------------------------------------#    


    
    
#-------------------------------| GRID TEMPLATE |-------------------------------------------#    
    root.grid_columnconfigure(0, weight=5, minsize=200)  
    root.grid_columnconfigure(1, weight=95)  
    root.grid_rowconfigure(0, weight=3, minsize=20)     
    root.grid_rowconfigure(1, weight=97)     
    
    root_windows["header"].grid_columnconfigure(0, weight=5, minsize=50)  
    root_windows["header"].grid_columnconfigure(1, weight=90)  
    root_windows["header"].grid_columnconfigure(2, weight=5, minsize=50)  
    root_windows["header"].grid_rowconfigure(0, weight=1, minsize=20)     
    
    root_windows["aside"].grid_columnconfigure(0, weight=1)  
    root_windows["aside"].grid_rowconfigure(0, weight=30)     
    root_windows["aside"].grid_rowconfigure(1, weight=70)     
    
    root_windows["main"].grid_columnconfigure(0, weight=1)  
    root_windows["main"].grid_rowconfigure(0, weight=92)     
    root_windows["main"].grid_rowconfigure(1, weight=8)     
    
#-------------------------------| GRID TEMPLATE |-------------------------------------------#    




#-------------------------------| GRID AREAS POSITION |-------------------------------------------#    
    root_windows["tittle"].grid(column=0, row=0, sticky="nsew", padx=0, pady=0)
    root_windows["header"].grid(column=1, row=0, sticky="nsew", padx=0, pady=0)
    root_windows["aside"].grid(column=0, row=1, sticky="nsew", padx=0, pady=0)
    root_windows["main"].grid(column=1, row=1, sticky="nsew", padx=0, pady=0)
    
    header_windows["h_1"].grid(column=0, row=0, sticky="nsew", padx=0, pady=0)
    header_windows["section"].grid(column=1, row=0, sticky="nsew", padx=0, pady=0)
    header_windows["close"].grid(column=2, row=0, sticky="nsew", padx=0, pady=0)
    
    aside_windows["user_img"].grid(column=0, row=0, sticky="nsew", padx=0, pady=0)
    aside_windows["options"].grid(column=0, row=1, sticky="nsew", padx=0, pady=0)
    
    main_windows["tabla_registros"].grid(column=0, row=0, sticky="nsew", padx=0, pady=0)
    main_windows["tabla_acciones"].grid(column=0, row=1, sticky="nsew", padx=0, pady=0)
#-------------------------------| GRID AREAS POSITION |-------------------------------------------#    

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#


    tittle_elements = {
        "lbl_tittle": tk.Label(root_windows["tittle"],text="Titulo",font=bold_font)
    }
    
    header_elements = {
        "icon_nav": tk.Label(header_windows["h_1"],text="NAV(≡),",font=bold_font),
        "lbl_seccion": tk.Label(header_windows["section"],text="Titulo_entidad",font=bold_font),
        "btn_close": tk.Label(header_windows["close"],text="Cerrar(X)",font=bold_font)
    }
    
    aside_options_elements = {
        "lbl_opciones": tk.Label(aside_windows["options"],text="Titulo_entidad",font=bold_font),
        "btn_home": tk.Button(aside_windows["options"],text="INICIO",font=bold_font, command=lambda:comando.btn_inicio_click()),
        "btn_clientes": tk.Button(aside_windows["options"],text="CLIENTES",font=bold_font, command=lambda:comando.btn_clientes_click()),
        "btn_vehiculos": tk.Button(aside_windows["options"],text="VEHICULOS",font=bold_font, command=lambda:comando.btn_vehiculos_click()),
        "btn_transacciones": tk.Button(aside_windows["options"],text="TRANSACCIONES",font=bold_font, command=lambda:comando.btn_transacciones_click())
    }
    
    main_tablaregistros_elements = {
        "tbe_registros": tk.Label(main_windows["tabla_registros"],text="tabla de registros",font=bold_font),
    }
    
    main_tablaacciones_elements = {
        "btn_agregar": tk.Button(main_windows["tabla_acciones"],text="AGREGAR",font=bold_font),
        "btn_editar": tk.Button(main_windows["tabla_acciones"],text="EDITAR",font=bold_font),
        "btn_eliminar": tk.Button(main_windows["tabla_acciones"],text="ELIMINAR",font=bold_font)
    }
    
    
    for elements, value in tittle_elements.items():
        tittle_elements[elements].pack()
        
    for elements, value in header_elements.items():
        header_elements[elements].pack()
        
    for elements, value in aside_options_elements.items():
        aside_options_elements[elements].pack()
        
    # for elements, value in main_tablaregistros_elements.items():
    #     main_tablaregistros_elements[elements].pack()
        
    for elements, value in main_tablaacciones_elements.items():
        main_tablaacciones_elements[elements].pack()
    

    

    
    campos = ("id_cliente", "nombre", "apellido", "documento", "direccion", "telefono", "correo_electronico")
    etiquetas = ("ID Cliente", "Nombre", "Apellido", "Documento", "Dirección", "Teléfono", "Correo Electrónico")
    tabla_clientes = front_funciones.front_crear_tabla(main_windows["tabla_registros"], campos, etiquetas,mi_callback_clic_cabecera,mi_callback_clic_registro)
    
    registros = api.leer_registros('cliente')
    
    
    front_funciones.front_rellenar_tabla(tabla_clientes,registros) 
    
    




   
    
    root.mainloop()
    
if __name__ == "__main__":
    main()
