import pandas as READERTABLE,os,json

def existe_json(nombre_json):
    path_file = "./backend/datos/" + nombre_json + ".json"
    if not os.path.isfile(path_file):
        with open(path_file, 'w') as f:
            json.dump([{}], f, indent=4)
            
def cargar_json_en_tabla(nombre_json):
    existe_json(nombre_json)
    return READERTABLE.read_json('./backend/datos/' + nombre_json + ".json") 

def guardar_tabla_en_json(nombre_json,tabla_a_guardar):
    existe_json(nombre_json)
    tabla_a_guardar.to_json('./backend/datos/' + nombre_json + ".json", orient='records',indent=4)
    


def cargar_json_en_serial(nombre_json):
    existe_json(nombre_json)
    return READERTABLE.read_json('./backend/datos/' + nombre_json + ".json", typ='series')


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



def eliminar_registro_json(nombre_json, filtro):
    print("Eliminando registro...")
    tabla = cargar_json_en_tabla(nombre_json)
    
    for columna, valor in filtro.items():
        tabla = tabla[tabla[columna] != valor]
        
    if not tabla.empty:
        guardar_tabla_en_json(nombre_json,tabla)
        print("Registro Eliminado.")

