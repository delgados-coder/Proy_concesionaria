import tkinter as tk
from tkinter import ttk


def mostrar_inicio():
    limpiar_seccion()
    label_seccion.config(text="Inicio")

def mostrar_clientes():
    limpiar_seccion()
    label_seccion.config(text="Clientes")
    btn_agregar.grid(row=1, column=0, padx=10, pady=10)
    btn_editar.grid(row=1, column=1, padx=10, pady=10)
    btn_eliminar.grid(row=1, column=2, padx=10, pady=10)

def mostrar_vehiculos():
    limpiar_seccion()
    label_seccion.config(text="Vehículos")
    btn_agregar.grid(row=1, column=0, padx=10, pady=10)
    btn_editar.grid(row=1, column=1, padx=10, pady=10)
    btn_eliminar.grid(row=1, column=2, padx=10, pady=10)

def mostrar_transacciones():
    limpiar_seccion()
    label_seccion.config(text="Transacciones")
    btn_agregar.grid(row=1, column=0, padx=10, pady=10)
    btn_editar.grid(row=1, column=1, padx=10, pady=10)
    btn_eliminar.grid(row=1, column=2, padx=10, pady=10)

def salir():
    root.quit()

def limpiar_seccion():
    for widget in frame_seccion.winfo_children():
        widget.grid_forget()


root = tk.Tk()
root.title("UNERCAR S.A.")


root.geometry("800x600")
root.configure(bg="#000000")


frame_menu = tk.Frame(root, bg="#333333", width=200, height=600)
frame_menu.grid(row=0, column=0, rowspan=2, sticky="ns")
frame_menu.grid_propagate(False)

frame_seccion = tk.Frame(root, bg="#FFDADA", width=600, height=550)
frame_seccion.grid(row=1, column=1, sticky="nsew")
frame_seccion.grid_propagate(False)

frame_footer = tk.Frame(root, bg="#6A3332", width=600, height=50)
frame_footer.grid(row=2, column=1, sticky="ew")
frame_footer.grid_propagate(False)


label_titulo = tk.Label(root, text="UNERCAR S.A.", font=("Arial", 18, "bold"), bg="#6A3332", fg="#FFFFFF")
label_titulo.grid(row=0, column=1, sticky="ew")


btn_inicio = tk.Button(frame_menu, text="INICIO", command=mostrar_inicio, bg="#AAAAAA")
btn_clientes = tk.Button(frame_menu, text="CLIENTES", command=mostrar_clientes, bg="#AAAAAA")
btn_vehiculos = tk.Button(frame_menu, text="VEHICULOS", command=mostrar_vehiculos, bg="#AAAAAA")
btn_transacciones = tk.Button(frame_menu, text="TRANSACCIONES", command=mostrar_transacciones, bg="#AAAAAA")
btn_salir = tk.Button(frame_menu, text="SALIR", command=salir, bg="#AAAAAA")


btn_inicio.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
btn_clientes.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
btn_vehiculos.grid(row=3, column=0, padx=10, pady=10, sticky="ew")
btn_transacciones.grid(row=4, column=0, padx=10, pady=10, sticky="ew")
btn_salir.grid(row=5, column=0, padx=10, pady=10, sticky="ew")


label_seccion = tk.Label(frame_seccion, text="Inicio", font=("Arial", 18), bg="#FFDADA")
label_seccion.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="w")


btn_agregar = tk.Button(frame_seccion, text="AGREGAR", bg="#D6CFC7")
btn_editar = tk.Button(frame_seccion, text="EDITAR", bg="#D6CFC7")
btn_eliminar = tk.Button(frame_seccion, text="ELIMINAR", bg="#D6CFC7")


root.mainloop()
