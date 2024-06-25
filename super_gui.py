from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from utils import comandos as comando, auxiliares as aux
from backend.funciones import api
from utils import gui_maker as GM
import config
from PIL import Image, ImageTk

from pathlib import Path
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH/ Path(r".\assets\frame")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.geometry("1000x900")
window.configure(bg = "gray")

#-----------------------|INICIO - LIENZO CANVAS |-------------------------#
lienzo = GM.crear_lienzo_canvas(window,900,800)
GM.posicionar_canva_fondo(lienzo,pos_x=(1000-900)/2,pos_y=(900-800)/2)
#-----------------------|FIN - LIENZO CANVAS |----------------------------#

#-----------------------|INICIO - imagen en Lienzo |-------------------------#
fondo = GM.crear_imagen(canvas_frame=lienzo,nombre_imagen="image_1",pos_centro_x=450,pos_centro_y=400)

#-----------------------|FIN - imagen en Lienzo |----------------------------#


#-----------------------|INICIO - TODOS LOS BOTONES |-------------------------#
btn_clientes = GM.crear_boton("btn_clientes")
btn_clientes.config(
    command=lambda: print("|-------------|PRUEBA Clientes--------------|"))
GM.posicionar_boton(
    btn_clientes,
    pos_x=150,
    pos_y=50

)

btn_vehiculos = GM.crear_boton("btn_vehiculos")
btn_vehiculos.config(
    command=lambda: print("|-------------|PRUEBA Vehiculos|--------------|"))
GM.posicionar_boton(
    btn_vehiculos,
    pos_x=100.9764404296875,
    pos_y=20.16024780273438,
    ancho=105.78475952148438,
    alto=28.637863159179688
)
#-----------------------|FIN - TODOS LOS BOTONES |----------------------------#

#-----------------------|INICIO - TODOS LOS RECTANGULOS |-------------------------#
GM.crear_rectangulo(canvas_frame=lienzo,pos_x=20,pos_y=50,ancho=600,alto=3)
#-----------------------|FIN - TODOS LOS RECTANGULOS |----------------------------#

#-----------------------|INICIO - TODOS LOS TEXTOS |-------------------------#
GM.crear_texto(lienzo,texto="default",pos_x=30,pos_y=20,color_fuente="blue",size_fuente=20,tipo_fuente="Arial")
#-----------------------| FIN   - TODOS LOS TEXTOS |-------------------------#




window.resizable(False, False)
window.mainloop()


