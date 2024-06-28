from backend.funciones import api

entidad="vehiculo"

registro_a_editar={"id_vehiculo":2}

nuevos_datos={
        "dominio":"MNO789xxx",
        "marca":"Hondaxxxx",
        "modelo":"Civiczxc",
        "anio":2017,
        "kilometraje":35000,
        "precio_compra":17000,
        "precio_venta":19000,
        "estado":"disponible"
}

input("tecla............")
api.modificar_registro(entidad,registro_a_editar,nuevos_datos) 
