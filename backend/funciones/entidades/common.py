import pandas as READERTABLE,os,json


#-----------------------------------------------------------------------------------------------------------------#
def existe_json(nombre_json):
    path_file = "./backend/datos/" + nombre_json + ".json"
    if not os.path.isfile(path_file):
        with open(path_file, 'w') as f:
            json.dump([{}], f, indent=4)
#-----------------------------------------------------------------------------------------------------------------#
            
            
            
#-----------------------------------------------------------------------------------------------------------------#
def cargar_json_en_tabla(nombre_json):
    existe_json(nombre_json)
    return READERTABLE.read_json('./backend/datos/' + nombre_json + ".json") 

def guardar_tabla_en_json(nombre_json,tabla_a_guardar):
    existe_json(nombre_json)
    tabla_a_guardar.to_json('./backend/datos/' + nombre_json + ".json", orient='records',indent=4)
    


def cargar_json_en_serial(nombre_json):
    existe_json(nombre_json)
    return READERTABLE.read_json('./backend/datos/' + nombre_json + ".json", typ='series')
#-----------------------------------------------------------------------------------------------------------------#


#---------------------------------------------------|C|rud--------------------------------------------------------#
def crear_registro_json(nombre_json, registro_a_guardar):
    tabla = cargar_json_en_tabla(nombre_json)
    campo = "id_" + nombre_json
    id_nuevo = 0

    while True:
        id_nuevo += 1
        if campo not in tabla.columns or not any(tabla[campo] == id_nuevo):
            registro_a_guardar = {campo: id_nuevo, **registro_a_guardar}
            break

    tabla = READERTABLE.concat([tabla, READERTABLE.DataFrame([registro_a_guardar])], ignore_index=True)
    guardar_tabla_en_json(nombre_json, tabla)

    print("Registro Creado.")
#-----------------------------------------------------------------------------------------------------------------#



#--------------------------------------------------c|R|ud-------------------------------------------------------#
def listar_tabla_json(nombre_json, orden_por=None, orden_ascendente=True, filtros_aplicados=None):
    tabla = cargar_json_en_tabla(nombre_json)
    
    if filtros_aplicados:
        for columna, valor in filtros_aplicados.items():
            tabla = tabla[tabla[columna] == valor]
   
    if orden_por:
        tabla = tabla.sort_values(by=orden_por, ascending=orden_ascendente)
    return tabla
    
    
    
def listar_serie_json(nombre_json, orden_por=None, orden_ascendente=True, filtros_aplicados=None):
    tabla_out = listar_tabla_json(nombre_json, orden_por, orden_ascendente, filtros_aplicados)
    return tabla_out.squeeze()
#-----------------------------------------------------------------------------------------------------------------#



#--------------------------------------------------#cr|U|d---------------------------------------------------------#
def editar_registro_json(nombre_json, registro_a_editar, nuevos_campos):
    print("Editando registro...")
    tabla = cargar_json_en_tabla(nombre_json)
    campo = "id_" + nombre_json
    
    # Verificar si el ID existe en la tabla
    if campo not in tabla.columns or registro_a_editar not in tabla[campo].values:
        print(f"Registro con {campo} = {registro_a_editar} no encontrado.")
        return
    
    # Localizar el índice del registro a editar
    indice = tabla[tabla[campo] == registro_a_editar].index[campo]
    
    # Actualizar los valores del registro
    for columna, valor in nuevos_campos.items():
        tabla.at[indice, columna] = valor
    
    # Guardar la tabla actualizada en el JSON
    guardar_tabla_en_json(nombre_json, tabla)
    
    print("Registro Editado...")
    
    #ejemplo de uso:
        
    # nombre_json = "cliente"
    # id_registro = 5
    # nuevos_valores = {
    #    "id_cliente": id_registro,
    #    "nombre": "prueba",
    #    "apellido": "codigo",
    #    "documento": "34812574",
    #    "direccion": "Pruebalandia",
    #    "telefono": "384-4253125",
    #    "correo_electronico": "codigoprueba@gmail.com"
    # }

    # editar_registro_json(nombre_json, id_registro, nuevos_valores)
    
#-----------------------------------------------------------------------------------------------------------------#



#----------------------------------------------------#cru|D|------------------------------------------------------#
def eliminar_registro_json(nombre_json, registro_a_eliminar):
    print("Eliminando registro...")
    tabla = cargar_json_en_tabla(nombre_json)
    
    for columna, valor in registro_a_eliminar.items():
        tabla = tabla[tabla[columna] != valor]
        
        
    if not tabla.empty:
        guardar_tabla_en_json(nombre_json,tabla)
        print("Registro Eliminado.")
#-----------------------------------------------------------------------------------------------------------------#


