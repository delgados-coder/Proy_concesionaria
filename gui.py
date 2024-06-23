import random
import tkinter as tk
from tkinter import font

from utils import comandos as comando, auxiliares as aux
from backend.funciones import api
import config

def color_aleatorio():
    color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    return color


root_titulo="CONCESIONARIA <-UnerCAR S.A.->"
root_color_base="#001B2E"
root_path_icon="./favicon.ico"


def main():
    root = tk.Tk()
    
    screen_width = root.winfo_screenwidth()       
    screen_height = root.winfo_screenheight()
    window_width = screen_width - 300  
    window_height = screen_height - 300
    x_cordinate = int((screen_width / 2) - (window_width / 2)) 
    y_cordinate = int((screen_height / 2) - (window_height / 2)) 
    
    root.title(root_titulo)
    root.iconbitmap(root_path_icon)
    root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    root.configure(background=root_color_base)
    
    bold_font = font.Font(family="Helvetica", size=12, weight="bold")
    
    print(root)
    config.root = root
    
    
    #----------------------------------------------------------------------------------------------------------------------#
    #----------------------------------------------------------------------------------------------------------------------#
    #----------------------------------------------------------------------------------------------------------------------#
    #----------------------------------------------------------------------------------------------------------------------#
    root_children={
        "header": tk.Frame(root, bg=color_aleatorio(), bd=2, relief=tk.SUNKEN),
        "nav": tk.Frame(root, bg=color_aleatorio(), bd=2, relief=tk.SUNKEN),
        "main": tk.Frame(root, bg=color_aleatorio(), bd=2, relief=tk.SUNKEN),
        "footer": tk.Frame(root, bg=color_aleatorio(), bd=2, relief=tk.SUNKEN),
    }
    
    header_children={
        "title": tk.Frame(root_children["header"], bg=color_aleatorio(), bd=2, relief=tk.SUNKEN),
        "space": tk.Frame(root_children["header"], bg=color_aleatorio(), bd=2, relief=tk.SUNKEN),
        "user": tk.Frame(root_children["header"], bg=color_aleatorio(), bd=2, relief=tk.SUNKEN),
    }

    nav_children={
        "space1": tk.Frame(root_children["nav"], bg=color_aleatorio(), bd=2, relief=tk.SUNKEN),
        "nav_home": tk.Frame(root_children["nav"], bg=color_aleatorio(), bd=2, relief=tk.SUNKEN),
        "nav_client": tk.Frame(root_children["nav"], bg=color_aleatorio(), bd=2, relief=tk.SUNKEN),
        "nav_vehicle": tk.Frame(root_children["nav"], bg=color_aleatorio(), bd=2, relief=tk.SUNKEN),
        "nav_transactions": tk.Frame(root_children["nav"], bg=color_aleatorio(), bd=2, relief=tk.SUNKEN),
        "space2": tk.Frame(root_children["nav"], bg=color_aleatorio(), bd=2, relief=tk.SUNKEN),
    }

    main_children={
        "tab_title": tk.Frame(root_children["main"], bg=color_aleatorio(), bd=2, relief=tk.SUNKEN),
        "tab_table": tk.Frame(root_children["main"], bg=color_aleatorio(), bd=2, relief=tk.SUNKEN),
        "tab_buttons": tk.Frame(root_children["main"], bg=color_aleatorio(), bd=2, relief=tk.SUNKEN),
    }
    
    tab_buttons_children={
        "space1": tk.Frame(main_children["tab_buttons"], bg=color_aleatorio(), bd=2, relief=tk.SUNKEN),
        "table_new": tk.Frame(main_children["tab_buttons"], bg=color_aleatorio(), bd=2, relief=tk.SUNKEN),
        "table_edit": tk.Frame(main_children["tab_buttons"], bg=color_aleatorio(), bd=2, relief=tk.SUNKEN),
        "table_delete": tk.Frame(main_children["tab_buttons"], bg=color_aleatorio(), bd=2, relief=tk.SUNKEN),
        "space2": tk.Frame(main_children["tab_buttons"], bg=color_aleatorio(), bd=2, relief=tk.SUNKEN),
    }
        
    footer_children={
        "foot": tk.Frame(root_children["footer"], bg=color_aleatorio(), bd=2, relief=tk.SUNKEN),
    }
    #----------------------------------------------------------------------------------------------------------------------#
    
    
    #----------------------------------------------------------------------------------------------------------------------#
    root.grid_columnconfigure(0, weight=1)
    
    root.grid_rowconfigure(0, weight=5)
    root.grid_rowconfigure(1, weight=2)
    root.grid_rowconfigure(2, weight=86)
    root.grid_rowconfigure(3, weight=7)
    
    root_children["header"].rowconfigure(0,weight=1)
    root_children["header"].columnconfigure(0,weight=30)
    root_children["header"].columnconfigure(1,weight=60)
    root_children["header"].columnconfigure(2,weight=10)
    
    root_children["nav"].rowconfigure(0,weight=1)
    root_children["nav"].columnconfigure(0,weight=30)
    root_children["nav"].columnconfigure(1,weight=10)
    root_children["nav"].columnconfigure(2,weight=10)
    root_children["nav"].columnconfigure(3,weight=10)
    root_children["nav"].columnconfigure(4,weight=10)
    root_children["nav"].columnconfigure(5,weight=30)
    
    root_children["main"].columnconfigure(0,weight=1)
    root_children["main"].rowconfigure(0,weight=5)
    root_children["main"].rowconfigure(1,weight=90)
    root_children["main"].rowconfigure(2,weight=5)

    main_children["tab_buttons"].rowconfigure(0,weight=1)
    main_children["tab_buttons"].columnconfigure(0,weight=35)
    main_children["tab_buttons"].columnconfigure(1,weight=10)
    main_children["tab_buttons"].columnconfigure(2,weight=10)
    main_children["tab_buttons"].columnconfigure(3,weight=10)
    main_children["tab_buttons"].columnconfigure(4,weight=35)
    

    #----------------------------------------------------------------------------------------------------------------------#
    
    
    #----------------------------------------------------------------------------------------------------------------------#
    root_children["header"].grid(column=0, row=0, sticky="nsew", padx=0, pady=0)
    root_children["nav"].grid(column=0, row=1, sticky="nsew", padx=0, pady=0)
    root_children["main"].grid(column=0, row=2, sticky="nsew", padx=0, pady=0)
    root_children["footer"].grid(column=0, row=3, sticky="nsew", padx=0, pady=0)

    header_children["title"].grid(column=0, row=0, sticky="nsew", padx=0, pady=0)
    header_children["space"].grid(column=1, row=0, sticky="nsew", padx=0, pady=0)
    header_children["user"].grid(column=2, row=0, sticky="nsew", padx=0, pady=0)
    
    nav_children["space1"].grid(column=0, row=0, sticky="nsew", padx=0, pady=0)
    nav_children["nav_home"].grid(column=1, row=0, sticky="nsew", padx=0, pady=0)
    nav_children["nav_client"].grid(column=2, row=0, sticky="nsew", padx=0, pady=0)
    nav_children["nav_vehicle"].grid(column=3, row=0, sticky="nsew", padx=0, pady=0)
    nav_children["nav_transactions"].grid(column=4, row=0, sticky="nsew", padx=0, pady=0)
    nav_children["space2"].grid(column=5, row=0, sticky="nsew", padx=0, pady=0)

    main_children["tab_title"].grid(column=0, row=0, sticky="nsew", padx=0, pady=0)
    main_children["tab_table"].grid(column=0, row=1, sticky="nsew", padx=0, pady=0)
    main_children["tab_buttons"].grid(column=0, row=2, sticky="nsew", padx=0, pady=0)
    
    tab_buttons_children["space1"].grid(column=0, row=0, sticky="nsew", padx=0, pady=0)
    tab_buttons_children["table_new"].grid(column=1, row=0, sticky="nsew", padx=0, pady=0)
    tab_buttons_children["table_edit"].grid(column=2, row=0, sticky="nsew", padx=0, pady=0)
    tab_buttons_children["table_delete"].grid(column=3, row=0, sticky="nsew", padx=0, pady=0)
    tab_buttons_children["space2"].grid(column=4, row=0, sticky="nsew", padx=0, pady=0)

    #----------------------------------------------------------------------------------------------------------------------#
    #----------------------------------------------------------------------------------------------------------------------#
    #----------------------------------------------------------------------------------------------------------------------#
    
    config.main_table = main_children["tab_table"]
    
    #------------------------------------| LISTA DE ELEMENTOS |---------------------------------------#
    header_elements = {
        "lbl_title": tk.Label(header_children["title"],text="UNERCAR S.A.",font=bold_font),
        "lbl_user": tk.Label(header_children["user"],text="USER",font=bold_font)
    }
    
    nav_elements = {
        "btn_inicio": tk.Button(nav_children["nav_home"],text="INICIO",font=bold_font,
        command=lambda:comando.accion()),
        
        "btn_clientes": tk.Button(nav_children["nav_client"],text="CLIENTES",font=bold_font,
        command=lambda:comando.btn_clientes_click(main_children["tab_table"])),
        
        "btn_vehiculos": tk.Button(nav_children["nav_vehicle"],text="VEHICULOS",font=bold_font,
        command=lambda:comando.btn_vehiculos_click(main_children["tab_table"])),
        
        "btn_transacciones": tk.Button(nav_children["nav_transactions"],text="TRANSACCIONES",font=bold_font,
        command=lambda:comando.btn_transacciones_click(main_children["tab_table"])),
    }
    
    main_elements = {
        "lbl_title": tk.Label(main_children["tab_title"],text="INICIO",font=bold_font),
        
        "btn_new": tk.Button(tab_buttons_children["table_new"],text="NUEVO",font=bold_font,
        command=lambda:comando.accion()),
        
        "btn_edit": tk.Button(tab_buttons_children["table_edit"],text="EDITAR",font=bold_font,
        command=lambda:comando.accion()),
        
        "btn_delete": tk.Button(tab_buttons_children["table_delete"],text="ELIMINAR",font=bold_font,
        command=lambda:comando.accion()),
    }
    
    footer_elements = {}
    #------------------------------------| LISTA DE ELEMENTOS |---------------------------------------#
    
    
    #---------------------------| CARGAR ELEMENTOS |--------------------------------#
    for elements, value in header_elements.items():
        header_elements[elements].pack()

    for elements, value in nav_elements.items():
        nav_elements[elements].pack()

    for elements, value in main_elements.items():
        main_elements[elements].pack()
        
    for elements, value in footer_elements.items():
        footer_elements[elements].pack()
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    root.mainloop()
if __name__ == "__main__":
    main()
