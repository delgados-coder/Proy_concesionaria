from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from utils import comandos as comando, auxiliares as aux
from backend.funciones import api
from utils import gui_maker as GM
import config
from PIL import Image, ImageTk


ancho_ventana_p=1280
alto_ventana_p=720
eliminar_esto=100


#-----------------------|INICIO - VENTANA PRIMARIA |-------------------------#
ventana_principal = GM.crear_ventana_principal(
ancho_ventana=ancho_ventana_p,
alto_ventana=alto_ventana_p,
titulo_ventana="Ventana de prueba",
icon_path="./recursos/iconos/favicon.ico",
color_base="#4B3621"
)
#-----------------------|FIN - VENTANA PRIMARIA |----------------------------#

#-----------------------|INICIO - LIENZO CANVAS |-------------------------#
lienzo = GM.crear_lienzo_canvas(ventana_principal,ancho_ventana_p-eliminar_esto,alto_ventana_p-eliminar_esto)
GM.posicionar_canva_fondo(lienzo,pos_x=(0+eliminar_esto)/2,pos_y=(0+eliminar_esto)/2)
#-----------------------|FIN - LIENZO CANVAS |----------------------------#

#-----------------------|INICIO - imagen en Lienzo |-------------------------#
# fondo = GM.crear_imagen(canvas_frame=lienzo,nombre_imagen="fondos/background.png",pos_centro_x=ancho_ventana_p/2,pos_centro_y=alto_ventana_p/2)
#-----------------------|FIN - imagen en Lienzo |----------------------------#


#-----------------------|INICIO - TODOS LOS BOTONES |-------------------------#

#-************- Copia y pega este pedazo de codigo dado el numero de botones que tengas*******-#
#-************- Solo cambia los valores encerrados que tengan > |-este-| para crear el boton**-#
#
##|-boton_#-| = GM.crear_boton(|-ventana_padre-|,|-"botones/btn_prueba.png"-|)
##|-boton_#-|.config(
##    command=lambda: |-FUNCION A EJECUTAR()-|
##)
##GM.posicionar_boton(
##    |-boton_#-|,
##    pos_x=|-10-|,
##    pos_y=|-20-|
##)
#
#*********************************************************************************************-#
#repetir para (inicio/clientes/vehiculos/transaccines/aceptar/cancelar - opcionales: BoToN_USER)

#-----------------------|FIN - TODOS LOS BOTONES |-------------------------#






ventana_principal.mainloop()
