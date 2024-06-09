from funciones.auxiliares import utilidades

# utilidades.menu_principal() #(version antigua quedo obsoleta) ahora se utiliza un menu dinamico.. hace mas eficaz el codigo

titulo='Menu Principal'
opciones=["Gestion Clientes","Gestion Vehiculos","Gestion Transacciones"]
funciones=["menu_clientes","menu_vehiculos","menu_transacciones"]
utilidades.crear_menu(titulo,opciones,funciones)

