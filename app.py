from utils import funciones as front_funciones
from utils import acciones as back_acciones

from backend.funciones.entidades import cliente, common, transaccion, vehiculo

from tkinter import Tk
from tkinter import ttk
from tkinter import *


def cargar_boton(path):
        return PhotoImage(file=path)
buttons_path={
    "button1":"./assets/btns/btn_clientes.png",
    "button2":"./assets/btns/btn_vehiculos.png",
    "button3":"./assets/btns/btn_transacciones.png"
}


def main():
    root = Tk()
    
    

    screen_width= root.winfo_screenwidth()       
    screen_height= root.winfo_screenheight()
    window_width = screen_width-500
    window_height = screen_height-300
    x_cordinate = int((screen_width/2) - (window_width/2)) 
    y_cordinate = int((screen_height/2) - (window_height/2))               

    root_titulo="CONCESIONARIA <-UnerAutos S.A.->"
    root_color_base="#001B2E"
    root_path_icon="./favicon.ico"
    
    root.resizable(False, False) 
    root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))  

    root.title(root_titulo)
    root.iconbitmap(root_path_icon)
    root['bg'] = root_color_base
    
    
    
    #--------------| TEST: crear boton al hacer click eliminar un registro | ---------------------#
    #nombre_json="clientes"
    #filtro={"id_cliente": 2}
    #boton = Button(root, text="Eliminar Registro...",command=lambda: back_acciones.llamar_eliminar_registro_json(nombre_json,filtro))
    #boton.pack()
    
    
    
    #--------------| TEST: Crear una tabla | ---------------------#
    # campos = ("id_cliente", "name", "surname", "doc", "dir", "tel", "email")
    # etiquetas = ("ID Cliente", "Nombre", "Apellido", "Documento", "Dirección", "Teléfono", "Correo Electrónico")
    # tabla_clientes = front_funciones.front_crear_tabla(root, campos, etiquetas)
    
        
    #--------------| TEST: Obtener Registros y Rellenar la 'Tabla_Clientes" | ---------------------#
    # registros = back_acciones.llamar_listar_tabla_json() #carga los registros
    # front_funciones.front_rellenar_tabla(tabla_clientes,registros) #rellena la tabla
    
    
    
    #--------------| TEST: Crear un Formulario |---------------------#
    #nombre_form = "Formulario de Ejemplo"
    #campos = ["ID_cliente","Nombre","Apellido","Documento","Direccion","Telefono","Correo Electronico"]
    #front_funciones.crear_formulario(root,nombre_form, campos)
    
           
    
    
    
    
    
    
    
    
    
    
    

    root.mainloop()
    
if __name__ == "__main__":
    main()
    
    

