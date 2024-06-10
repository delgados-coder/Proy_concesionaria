from utils import funciones as front_funciones
from utils import acciones as back_acciones

from tkinter import Tk
from tkinter import ttk
from tkinter import *

def main():
    root = Tk()
    
    

    screen_width= root.winfo_screenwidth()       
    screen_height= root.winfo_screenheight()
    window_width = screen_width  
    window_height = screen_height
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
    
    boton = Button(root, text="Eliminar Registro", command=back_acciones.llamar_eliminar_registro_json)
    boton.pack()
    

    root.mainloop()
    
if __name__ == "__main__":
    main()
    
    

