import pandas as READERTABLE,os,json

#-----------------------------------------------------------------------------------------------------------------#
def existe_json(nombre_json):
    path_file = "./backend/datos/" + nombre_json + ".json"
    if not os.path.isfile(path_file):
        with open(path_file, 'w') as f:
            json.dump([{}], f, indent=4)
#-----------------------------------------------------------------------------------------------------------------#


#-----------------------------------------------------------------------------------------------------------------#
def obtener_tabla_desde_json(nombre_del_json):
    existe_json(nombre_del_json)
    pk="id_cliente"
    return READERTABLE.read_json('./backend/datos/' + nombre_del_json + ".json", )

def obtener_json_desde_tabla(nombre_del_json,tabla_a_guardar):
    existe_json(nombre_del_json)
    tabla_a_guardar.to_json('./backend/datos/' + nombre_del_json + ".json", orient='records',indent=4)
#-----------------------------------------------------------------------------------------------------------------#
    
def alta_registro(nombre_del_json, registro_a_agregar):
    tabla = obtener_tabla_desde_json(nombre_del_json)
    campo = "id_"+nombre_del_json
    id_asignado=0;

    while True:
        if campo not in tabla.columns or not any(tabla[campo] == id_asignado):
            registro_a_agregar = {campo: id_asignado, **registro_a_agregar}
            break
        id_asignado+=1
    
    tabla = READERTABLE.concat([tabla, READERTABLE.DataFrame([registro_a_agregar])], ignore_index=True)
    tabla = tabla.sort_values(campo,ascending=True)
    
    obtener_json_desde_tabla(nombre_del_json,tabla)      
    
    

def baja_registro(nombre_del_json,registro_a_eliminar):
    tabla = obtener_tabla_desde_json(nombre_del_json)
    
    for clave, valor in registro_a_eliminar.items():
        tabla = tabla[tabla[clave] != valor]

    obtener_json_desde_tabla(nombre_del_json,tabla)    
    
    
    
      
def modificar_registro(nombre_del_json,registro_a_modificar,nuevos_valores):
    tabla = obtener_tabla_desde_json(nombre_del_json)
    campo="id_"+nombre_del_json
    
    if campo not in tabla.columns or registro_a_modificar not in tabla[campo].values:
        print(f"Registro con {campo} = {registro_a_modificar} no encontrado.")
        return
    
    indice = tabla[tabla[campo] == registro_a_modificar].index[campo]

    for columna, valor in nuevos_valores.items():
        tabla.at[indice, columna] = valor
    print("Registro modificado")
    
    obtener_json_desde_tabla(nombre_del_json,tabla)
    
    
    
    
    
      
def leer_registros(nombre_del_json, ordenar=None, filtro_aplicado=None):
    tabla = obtener_tabla_desde_json(nombre_del_json)
    
    if filtro_aplicado:
        for clave, valor in filtro_aplicado.items():
            tabla = tabla[tabla[clave] == valor]
            
    if ordenar:
        tabla = tabla.sort_values(ordenar[0],ascending=ordenar[1])
    
    return tabla
    
