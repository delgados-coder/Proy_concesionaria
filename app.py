from backend.funciones.entidades import clientes
from backend.funciones.entidades import vehiculos
from backend.funciones.entidades import transacciones

from tkinter import Tk
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
    window_width=screen_width  
    window_height=screen_height
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
    
    btn = cargar_boton(buttons_path["button1"])
    
    label_button = Label(root,image=btn,border=0)
    label_button.place(x=100,y=100)


    root.mainloop()
if __name__ == "__main__":
    main()
    
    
input("CONTINUAR..............")
datos = clientes.listar_clientes()
print(datos)
    