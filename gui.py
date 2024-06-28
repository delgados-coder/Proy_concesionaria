from utils import comandos as comando
from utils import gui_maker as GM
import config


ancho_ventana_p=1280
alto_ventana_p=720



#-----------------------|INICIO - VENTANA PRIMARIA |-------------------------#
config.ventana_principal = GM.crear_ventana_principal(
ancho_ventana=ancho_ventana_p,
alto_ventana=alto_ventana_p,
titulo_ventana="software de Gestion -UNERCAR-",
icon_path="./recursos/iconos/favicon.ico",
color_base="#4B3621"
)
#-----------------------|FIN - VENTANA PRIMARIA |----------------------------#



#-----------------------|INICIO - LIENZO CANVAS |-------------------------#
config.lienzo = GM.crear_lienzo_canvas(config.ventana_principal,ancho_ventana_p,alto_ventana_p)
GM.posicionar_canva_fondo(config.lienzo,pos_x=0,pos_y=0)
#-----------------------|FIN - LIENZO CANVAS |----------------------------#



#-----------------------|INICIO - imagen en Lienzo |-------------------------#
config.image = GM.cargar_imagen(canvas_frame=config.lienzo,nombre_imagen="fondos/fondo_index.png",pos_centro_x=ancho_ventana_p/2,pos_centro_y=alto_ventana_p/2)
#-----------------------|FIN - imagen en Lienzo |----------------------------#




#-----------------------|INICIO - TODOS LOS BOTONES |-------------------------#

#-|1.Crera Botones |-#
button_inicio = GM.crear_boton(config.ventana_principal,"botones/btn_inicio.png")
button_inicio.config(
    command=lambda: comando.btn_secciones_click("inicio")
)
button_clientes = GM.crear_boton(config.ventana_principal,"botones/btn_clientes.png")
button_clientes.config(
    command=lambda: comando.btn_secciones_click("cliente")
)
button_vehiculos = GM.crear_boton(config.ventana_principal,"botones/btn_vehiculos.png")
button_vehiculos.config(
    command=lambda: comando.btn_secciones_click("vehiculo")
)
button_transacciones = GM.crear_boton(config.ventana_principal,"botones/btn_transacciones.png")
button_transacciones.config(
    command=lambda: comando.btn_secciones_click("transaccion")
)

#-|2.Podisionar Botoned |-#
GM.posicionar_boton(
    button_inicio,
    pos_x=330,
    pos_y=121
)
GM.posicionar_boton(
    button_clientes,
    pos_x=468,
    pos_y=121
)
GM.posicionar_boton(
    button_vehiculos,
    pos_x=637,
    pos_y=121
)
GM.posicionar_boton(
    button_transacciones,
    pos_x=816,
    pos_y=121
)

config.ventana_principal.mainloop()
