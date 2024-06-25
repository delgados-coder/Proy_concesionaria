from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from backend.funciones import api
from pathlib import Path
import tkinter as tk

OUTPUT_PATH = Path(__file__).parent
OUTPUT_PATH_UP_ONE = OUTPUT_PATH.parent
ASSETS_PATH = OUTPUT_PATH_UP_ONE / Path(r".\assets\frame")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

#|---------------|funciones - Ventana PRINCIPAL|--------------------#
def crear_ventana_principal(nombre_ventana,ancho_ventana,alto_ventana,titulo_ventana,icon_path,color_base):
    nombre_ventana = Tk()
    screen_width = nombre_ventana.winfo_screenwidth()       
    screen_height = nombre_ventana.winfo_screenheight()
    window_width = ancho_ventana  
    window_height = alto_ventana
    x_cordinate = int((screen_width / 2) - (window_width / 2)) 
    y_cordinate = int((screen_height / 2) - (window_height / 2)) 
        
    nombre_ventana.title(titulo_ventana)
    nombre_ventana.iconbitmap(icon_path)
    nombre_ventana.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    nombre_ventana.configure(background=color_base)    
#|---------------|funciones - Ventana PRINCIPAL|--------------------#


#|---------------|funciones - lienzo canvas|--------------------#
def crear_lienzo_canvas(ventana_padre,ancho,alto,bg_color="red"):
    frame_canvas = Canvas(
    ventana_padre,
    bg = bg_color,
    height = alto,
    width = ancho,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"    
    )
    return frame_canvas

def posicionar_canva_fondo(canvas_frame,pos_x=0,pos_y=0):
    canvas_frame.place(x=pos_x,y=pos_y)
#|---------------|funciones - lienzo canvas|--------------------#

#|---------------|Funciones de imagenes|--------------------#
def crear_imagen(canvas_frame,nombre_imagen,pos_centro_x=0,pos_centro_y=0):
    cargar_imagen = PhotoImage(file=relative_to_assets(nombre_imagen+".png"))
    medida1=pos_centro_x
    medida2=pos_centro_y
    cargar_imagen.image = cargar_imagen
    return canvas_frame.create_image(medida1,medida2, image=cargar_imagen)
#|---------------|Funciones de imagenes|--------------------#

#|---------------|Funciones de rectangulos|--------------------#
def crear_rectangulo(canvas_frame,pos_x=0,pos_y=0,ancho=10,alto=10,fondo="green"):
    canvas_frame.create_rectangle(pos_x,pos_y,pos_x+ancho,pos_y+alto,fill=fondo,outline="")
#|---------------|Funciones de rectangulos|--------------------#

#|---------------|Funciones de BOTONES|--------------------#
def crear_boton(nombre_boton):
    btn_image = PhotoImage(file=relative_to_assets(nombre_boton+".png"))
    btn_name = Button(
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
#|---------------|Funciones de BOTONES|--------------------#

#|---------------|Funciones de Textos|--------------------#
def crear_texto(canvas_frame,texto="default",pos_x=0,pos_y=0,color_fuente="blue",size_fuente=10,tipo_fuente="Arial"):
    return canvas_frame.create_text(pos_x,pos_y,anchor="nw",text=Text,fill=color_fuente,font=(tipo_fuente, size_fuente))
#|---------------|Funciones de Textos|--------------------#