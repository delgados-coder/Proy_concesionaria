#Tabla clientes/vehiculos/transacciones
import tkinter as tk

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from utils import comandos as comando, auxiliares as aux
from backend.funciones import api
import config

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame0")
proporcion=1


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("841x744")
window.configure(bg = "#FFFFFF")

config.window = window






#############################################################
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 744,
    width = 841,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    420.58441162109375,
    372.0,
    image=image_image_1
)
#############################################################
image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    768.844482421875,
    33.948944091796875,
    image=image_image_2
)
#############################################################
canvas.create_text(
    30.80126953125,
    20.5,
    anchor="nw",
    text="UNERCAR S.A.",
    fill="#000000",
    font=("SourceSerifPro SemiBold", 23 * -1)
)
#############################################################
canvas.create_rectangle(
    109.29144287109375,
    205.14060974121094,
    773.8067626953125,
    518.9882354736328,
    fill="#F6FDFF",
    outline="")
#############################################################
btn_agregar_image_1 = PhotoImage(
    file=relative_to_assets("btn_agregar.png"))
btn_agregar = Button(
    cursor="hand2",
    image=btn_agregar_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("btn_agregar clicked"),
    relief="flat"
)
btn_agregar.place(
    x=75.3935546875,
    y=562.8216552734375,
    width=139.68263244628906,
    height=46.17124938964844
)
#############################################################
btn_editar_image = PhotoImage(
    file=relative_to_assets("btn_editar.png"))
btn_editar = Button(
    cursor="hand2",
    image=btn_editar_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("btn_editar clicked"),
    relief="flat"
)
btn_editar.place(
    x=350.667724609375,
    y=562.8216552734375,
    width=139.68263244628906,
    height=46.17124938964844
)
#############################################################
btn_eliminar_image_3 = PhotoImage(
    file=relative_to_assets("btn_eliminar.png"))
btn_eliminar = Button(
    cursor="hand2",
    image=btn_eliminar_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("btn_eliminar clicked"),
    relief="flat"
)
btn_eliminar.place(
    x=625.94189453125,
    y=562.8216552734375,
    width=139.68263244628906,
    height=46.17124938964844
)

# image_image_3 = PhotoImage(
#     file=relative_to_assets("image_3.png"))
# image_3 = canvas.create_image(
#     434.6802978515625,
#     361.14060974121094,
#     image=image_image_3
# )
#############################################################








tabla=tk.Frame(window, bd=2, relief=tk.SUNKEN)
tabla.place(
    x=20.6802978515625,
    y=195.14060974121094,
    width=801,
    height=315
)







config.tabla = tabla







#############################################################
image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    769.0267333984375,
    33.377838134765625,
    image=image_image_4
)
#############################################################
btn_transacciones_image_4 = PhotoImage(
    file=relative_to_assets("btn_transacciones.png"))
btn_transacciones = Button(
    cursor="hand2",
    image=btn_transacciones_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:comando.btn_transacciones_click(tabla),
    relief="flat"
)
btn_transacciones.place(
    x=520.7415771484375,
    y=84.16024780273438,
    width=139.0981903076172,
    height=28.637863159179688
)
#############################################################
btn_vehiculos_image_5 = PhotoImage(
    file=relative_to_assets("btn_vehiculos.png"))
btn_vehiculos = Button(
    cursor="hand2",
    image=btn_vehiculos_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:comando.btn_vehiculos_click(tabla),
    relief="flat"
)
btn_vehiculos.place(
    x=407.3589782714844,
    y=84.16024780273438,
    width=105.78475952148438,
    height=28.637863159179688
)
#############################################################
btn_clientes_image_6 = PhotoImage(
    file=relative_to_assets("btn_clientes.png"))
btn_clientes = Button(
    cursor="hand2",
    image=btn_clientes_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:comando.btn_clientes_click(tabla),
    relief="flat"
)
btn_clientes.place(
    x=293.9764404296875,
    y=84.16024780273438,
    width=105.78475952148438,
    height=28.637863159179688
)
#############################################################
button_image_7 = PhotoImage(
    file=relative_to_assets("btn_inicio.png"))
button_7 = Button(
    cursor="hand2",
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("btn_inicio clicked"),
    relief="flat"
)
button_7.place(
    x=180.5938720703125,
    y=84.16024780273438,
    width=105.78475952148438,
    height=28.637863159179688
)
#############################################################
canvas.create_rectangle(
    29.80398154258728,
    62.24349570274353,
    790.758544921875,
    62.82794189453125,
    fill="#000000",
    outline="")
#############################################################
canvas.create_rectangle(
    175.33388876914978,
    126.82479453086853,
    660.4241943359375,
    127.40924072265625,
    fill="#000000",
    outline="")
#############################################################
canvas.create_rectangle(
    39.74239706993103,
    672.1131246089935,
    800.6969604492188,
    672.6975708007812,
    fill="#000000",
    outline="")
#############################################################
canvas.create_text(
    233.80126953125,
    147.5,
    anchor="nw",
    text="Tabla de Registros de la Consecionaria ",
    fill="#000000",
    font=("AnekBangla Regular", 21 * -1)
)
#############################################################
canvas.create_text(
    338.80126953125,
    681.5,
    anchor="nw",
    text="Copyright © 2024 \nDelgado, Santiago\nGregotari, Fernando\nJerez, Pablo Agustín\n\n",
    fill="#000000",
    font=("Signika Regular", 14 * -1)
)
#############################################################






window.resizable(False, False)
window.mainloop()
