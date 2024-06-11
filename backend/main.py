from backend.funciones import utilidades as util

# utilidades.menu_principal() #(version antigua quedo obsoleta) ahora se utiliza un menu dinamico.. hace mas eficaz el codigo
def main():
        titulo='Menu Principal'
        opciones=["Gestion Clientes","Gestion Vehiculos","Gestion Transacciones"]
        funciones=["menu_clientes","menu_vehiculos","menu_transacciones"]
        util.crear_menu(titulo,opciones,funciones)

if __name__ == "__main__":
    main()
