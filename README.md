# UNERCAR S.A. Sistema de gestión de concesionaria de vehículos 🚗 

  

## Autores ✒️ 

* **Santiago, Delgado** - *BackEnd* -  [delgados-coder](https://github.com/delgados-coder) 

* **Pablo Agustín, Jerez** - *FrontEnd* - [PunksCode](https://github.com/PunksCode) 

* **Fernando, Gregoratti** - *Tester-base Json* - [Fernando Gregoratti](https://github.com/mvkgamingarg) 

  

## Introducción 📖 

Hola, ¡Bienvenidos a nuestro proyecto de sistema de gestión de concesionaria de vehículos para la asignatura Programación 1 para la Tecnicatura en Desarrollo Web que es cursada en la Universidad Nacional de Entre Rios de modalidad virtual (UNER)!
A continuación se detallarán los pasos que se tomaron para la construcción del mismo proyecto con los roles asignados, además de la descripción de las tareas a realizar de cada integrante, además de apartados donde se describen un poco las funcionalidades hechas y la estructura del mismo. 

  

## Requisitos para su construcción📋 

- **Python 3.8 o superior**: Lenguaje de programación principal. 

- **Tkinter**: Biblioteca para la interfaz gráfica de usuario. 

- **Pandas**: Librería para manipulación y análisis de datos. 

- **Figma**: Herramienta para diseño de interfaces. 

- **XMind**: Herramienta para mapas mentales y diagramas lógicos. 

- **JSON**: Formato para el almacenamiento de datos. 

 

###Consignas a cumplir: 💼 

1. **CRUD**  

2. **Conococimiento de la asignatura y sus alcances: ** esto quiere decir que no podiamos realizar el trabajo con algunas herramientas de python o funciones como ser try catch, manejo de excepciones etc., solamente con lo visto en clases. 

3.Manejo de Json. 

4.**Opcional: ** interfaz, consumo de api y otras funciones que puedan ser utilizadas o le agreguen valor al trabajo. 

 

### Análisis y diseño del sistema: 

1. **Reuniones con el equipo**: Identificación de los requisitos mínimos del sistema mediante reuniones con el equipo. 

2. **Herramientas de diseño**: Uso de herramientas como XMind para crear diagramas lógicos y mapas mentales. 

3. **Desarrollo en Python**: Escritura de código en Python para generar las funciones  de la aplicación. 

 

 ## BackEnd 🛠️ 

### CRUD 

Esta sección presenta los Endpoints CRUD (Create, Read, Update, Delete) de la API backend de UNERCAR. Estos permiten realizar operaciones básicas de gestión de datos en los archivos JSON, facilitando la creación, lectura, actualización y eliminación de registros. 

  

### CRUD (Create, Read, Update, Delete): 

- **Create**: Permite crear un nuevo registro en la base de datos o archivo JSON. 

- **Read**: Permite leer y consultar los registros existentes. 

- **Update**: Permite modificar y actualizar los datos de un registro existente. 

- **Delete**: Permite eliminar un registro de la base de datos o archivo JSON. 

### Modularización de funciones 

Se modularizo el código para que este sea más legible, escalable, además que para una óptima y limpia conexión con el FrontEnd y sulventar de forma eficaz posibles errores en pruducción de una manera rapida y sencilla.  

Algunas de estas funciones modularizadas y una breve explicacion son: 

1.**crear_ventana_principal**: Crea la ventana principal de la aplicación con parámetros de ancho, alto, título, ícono y color de fondo.  

2. **crear_ventana_emergente**: Crea una ventana emergente dentro de la ventana principal con parámetros de ancho, alto, título y color de fondo. 

 3. **crear_lienzo_canvas**: Crea un lienzo canvas para dibujar elementos gráficos como imágenes y rectángulos.  

4. **crear_boton**: Crea un botón con una imagen, configurable para realizar acciones específicas.  

5. **crear_tabla**: Crea una tabla utilizando ttk.Treeview para mostrar datos con encabezados y permite la interacción con los registros. 

###Versiones y evolución del backend. 


## FrontEnd 🎨 

El proyecto se enfoca en el diseño y desarrollo de la interfaz gráfica para el frontend de una aplicación. 
Se siguió un proceso cuidadosamente planificado, desde la lluvia de ideas inicial hasta la implementación final, utilizando la biblioteca Tkinter en Python. 
El resultado es una interfaz limpia, organizada y altamente funcional que brinda una experiencia de usuario intuitiva y agradable. 

  

### Proceso de diseño: 

1. **Bocetos en papel**: El equipo comenzó con bocetos en papel para visualizar las ideas iniciales. 

2. **Diseño digital en Figma**: Luego se trasladaron los bocetos a un diseño digital en Figma, refinando y detallando la interfaz. 

3. **Iteración y aprobación**: Se realizaron varias iteraciones y revisiones hasta obtener la aprobación final del diseño. 

4. **Transición al código**: Traducción del diseño a código. 

5. **Pruebas y refinamiento**: Pruebas exhaustivas y refinamiento continuo de la interfaz. 

  

 ###Versiones y evolución de la interfaz. 

En un principio se trabajó con una traducción de código a traves de Tkdesign por medio de la consumicion del api de figma, para la realización de la misma se necesita conocimientos solidos de figma porque se deben seguir ciertas pautas para cumplir con la libreria tkdesign y que la transcripción sea correcta. En el repositorio del trabajo en Git-Hub se puede ver una primera version con la utilización de esta. 

Más adelante la versión 1.0 es descartada al hacer un análisis junto al backend del equipo si bien era funcional esta interfaz y programable a funciones el código que generaba la interfaz sino se tenía acceso al repositorio de figma o conocimientos en Tk con Canva podría dificultad la lectura de este. 

**Solución y evolución a la version 2.0** 💪 

Estudiando tkdesign con arquitectura inversa acompañado del compañero BackEnd se descubrió como es el funcionamiento de este y como se podría simplificar el mismo código trabajando como el sistema de etiquetado que hace tkDesign en Figma nos dimos cuenta que se podría implementar de una forma similar a este y con conocimientos en tkinter vanila, se imitó el funcionamiento de Tkdesign junto a tkinter, reduciendo y haciendo más legible el código. 

## Tester 🔧 

La creación de Json coherente fue realizada también por el testeador para tener una base coherente y que pueda ser relacionada con entidad relación más facil para la lectura de datos. 

Luego nos acompañó a un testeo riguroso para encontrar bugs tantos visuales como de código, aportándonos comentarios que nos ayudaban a la escala y evolución del proyecto mismo. 

 

###Notas sobre el proyecto 📖 

 **Escalabilidad ** El proyecto puede ser escalable y replicado para otro tipo de negocios o gestor como ser una biblioteca, ventas de cualquier producto etc 

**Sencillez**  Fácil  de entender y manipular con segmentación y una arquitectura de rápida compresión. 

**Actualización y mejora** Puede mejorarse a futuro ya que por el tiempo que fue hecho se pueden presentar algunos bugs no contemplados. 

**Ramificación de oportunidades** En la creación de este proyecto nos dimos cuenta de la posible creación de un framework ya que al hacer la arquitectura inversa nos dimos cuenta de como podríamos solventar algunos errores y limpieza del código la lógica de tkinter en general. 

## Contacto 📞 

Si tienen alguna pregunta o desean más información, no duden en ponerse en contacto con nosotros. Aquí están los contactos de los integrantes del proyecto: 

- **Santiago Delgado** - [delgados-coder](https://github.com/delgados-coder) - (https://www.linkedin.com/in/delgados-coder/)

- **Pablo Agustín, Jerez** - [PunksCode](https://github.com/PunksCode) (www.linkedin.com/in/punkscode)

- **Fernando, Gregoratti** - [Fernando Gregoratti](https://github.com/mvkgamingarg) 

  

Gracias por llegar hasta aquí y espero que le haya sido de su agrado este proyecto integrador.  

 

 
 

 
