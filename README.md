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

 

### Consignas a cumplir: 💼 

1. **CRUD**  

2. **Conococimiento de la asignatura y sus alcances**: esto quiere decir que no podiamos realizar el trabajo con algunas herramientas de python o funciones como ser try catch, manejo de excepciones etc., solamente con lo visto en clases. 

3.**Manejo de Json**

4.**Opcional**: interfaz, consumo de api y otras funciones que puedan ser utilizadas o le agreguen valor al trabajo. 

 

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

1. **crear_ventana_principal**: Crea la ventana principal de la aplicación con parámetros de ancho, alto, título, ícono y color de fondo.  

2. **crear_ventana_emergente**: Crea una ventana emergente dentro de la ventana principal con parámetros de ancho, alto, título y color de fondo. 

3. **crear_lienzo_canvas**: Crea un lienzo canvas para dibujar elementos gráficos como imágenes y rectángulos.  

4. **crear_boton**: Crea un botón con una imagen, configurable para realizar acciones específicas.  

5. **crear_tabla**: Crea una tabla utilizando ttk.Treeview para mostrar datos con encabezados y permite la interacción con los registros. 

### API para Manejo de Datos en JSON

Esta API permite gestionar datos almacenados en archivos JSON utilizando `pandas` y `json`. Las funciones principales incluyen:

- **Verificación y Creación de Archivos JSON**: Verifica si un archivo JSON existe y lo crea si no es así.
- **Lectura de Datos**: Lee datos desde un archivo JSON y los devuelve como un DataFrame.
- **Guardado de Datos**: Guarda un DataFrame en un archivo JSON.
- **Alta de Registros**: Agrega nuevos registros a un archivo JSON.
- **Baja de Registros**: Elimina registros específicos de un archivo JSON.
- **Modificación de Registros**: Modifica registros existentes en un archivo JSON.
- **Filtrado y Ordenamiento**: Lee registros de un JSON aplicando filtros y ordenamiento opcionales.

### Versiones y Evolución del Backend

Inicialmente, se realizaron bocetos de las entidades y sus atributos para definir la estructura de datos necesaria para el sistema. Este paso permitió identificar las principales entidades y sus relaciones, proporcionando una base sólida para el desarrollo del diagrama de entidad-relación.
Con los bocetos iniciales, se creó un diagrama de entidad-relación (ERD) detallado, que incluyó todas las entidades principales y sus atributos. Este diagrama sirvió como una guía visual para entender mejor las relaciones entre las diferentes partes del sistema y cómo interactuarían entre sí.
Luego elaboró un mapa mental que describía las operaciones CRUD (Create, Read, Update, Delete) para cada entidad identificada en el ERD. Esto ayudó a visualizar todas las operaciones necesarias para gestionar los datos del sistema y garantizar que todas las funcionalidades básicas estuvieran cubiertas.

Se realizaron pruebas iniciales de las funciones del backend a través de la consola. Esto incluyó la verificación de que las operaciones CRUD funcionaran correctamente, y se ajustaron los detalles según fuera necesario para asegurar la fiabilidad del sistema.
Para mejorar la experiencia de desarrollo y depuración, se crearon funciones auxiliares como limpiar la consola y generar menús de opciones. Estas funciones facilitaron la interacción con el sistema durante las pruebas y el desarrollo.
Una vez implementadas las funciones básicas, se realizó una optimización del código para identificar y eliminar patrones repetitivos. Este proceso permitió hacer el código más eficiente y mantenible, facilitando futuras actualizaciones y expansiones del sistema.

Durante el desarrollo, se identificó que la manipulación de datos en formato JSON podía optimizarse utilizando la librería Pandas. Esta librería permitió convertir los JSON en tablas, simplificando las operaciones de manipulación de datos y permitiendo una integración más eficiente con MySQL. El código fue modificado para aprovechar estas capacidades, mejorando significativamente el rendimiento y la simplicidad del backend.

Después de asegurar la funcionalidad del backend a través de la consola, se exploró la posibilidad de crear una interfaz gráfica para mejorar la interacción del usuario. Se evaluaron diferentes herramientas y se decidió implementar una interfaz usando Tkinter, debido a su facilidad de uso y capacidad para integrarse con el backend existente.

El proceso de desarrollo del backend incluyó varias etapas clave, desde la planificación inicial hasta la optimización y mejora continua. A través de pruebas rigurosas, modularización de funciones y mejoras en la manipulación de datos, el backend evolucionó para convertirse en una parte robusta y segura del sistema de gestión de la concesionaria de vehículos.

### Separación del Frontend y Backend por Seguridad

Para mejorar la seguridad y la integridad del sistema, se decidió separar más claramente el frontend del backend. Esta separación garantiza que el backend solo se encargue de las operaciones necesarias sin comprometer los datos sensibles de los clientes. Se implementaron medidas de seguridad adicionales para proteger los datos y asegurar la estabilidad del sistema a largo plazo, asegurando que las funciones críticas del backend no expongan la información a posibles ataques malintencionados.


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

  

### Versiones y evolución del FrontEnd. 

En un principio se trabajó con una traducción de código a traves de Tkdesign por medio de la consumicion del api de figma, para la realización de la misma se necesita conocimientos solidos de figma porque se deben seguir ciertas pautas para cumplir con la libreria tkdesign y que la transcripción sea correcta. En el repositorio del trabajo en Git-Hub se puede ver una primera version con la utilización de esta. 

Más adelante la versión 1.0 es descartada al hacer un análisis junto al backend del equipo si bien era funcional esta interfaz y programable a funciones el código que generaba la interfaz sino se tenía acceso al repositorio de figma o conocimientos en Tk con Canva podría dificultad la lectura de este. 

**Solución y evolución a la version 2.0** 💪 

Estudiando tkdesign con arquitectura inversa acompañado del compañero BackEnd se descubrió como es el funcionamiento de este y como se podría simplificar el mismo código trabajando como el sistema de etiquetado que hace tkDesign en Figma nos dimos cuenta que se podría implementar de una forma similar a este y con conocimientos en tkinter vanila, se imitó el funcionamiento de Tkdesign junto a tkinter, reduciendo y haciendo más legible el código hasta llegar luego de diferentes pruebas al codigo final, con la segmentación y una comunicación optmica con los datos y funciones del backend traidas y mostradas en el Front, haciendo una interfaz limpia, agradable visualmente, y funcional pudiendo mostrar tablas, totalizaciones, elementos nav, formularios etc.

## Tester 🔧 

La creación de Json fue realizada por el tester para tener una base en la que se pueda trabajar y que pueda ser relacionada con entidad relación más facil para la lectura de datos. 

Luego nos acompañó en diferentes testeo que se realizo en parte del back y del front para encontrar bugs tantos visuales como de código, aportándonos comentarios que nos ayudaban y daban otros puntos de vistas que enriquecia el proyecto.
 

### Notas sobre el proyecto 📖 

**Escalabilidad ** El proyecto puede ser escalable y replicado para otro tipo de negocios o gestor como ser una biblioteca, ventas de cualquier producto etc 

**Sencillez**  Fácil de entender y manipular con segmentación y una arquitectura de rápida compresión. 

**Actualización y mejora** Puede mejorarse a futuro ya que por el tiempo que fue hecho se pueden presentar algunos bugs no contemplados. 

**Ramificación de oportunidades** En la creación de este proyecto nos dimos cuenta de la posible creación de un framework ya que al hacer la arquitectura inversa nos percatamos de como podríamos solventar algunos errores y limpieza del código de la lógica de tkinter y tkinterdesign en general. 

## Contacto 📞 

Si tienen alguna pregunta o desean más información, no duden en ponerse en contacto con nosotros. Aquí están los contactos de los integrantes del proyecto: 

- **Santiago Delgado** - [delgados-coder](https://github.com/delgados-coder) - (https://www.linkedin.com/in/delgados-coder/)

- **Pablo Agustín, Jerez** - [PunksCode](https://github.com/PunksCode) (www.linkedin.com/in/punkscode)

- **Fernando, Gregoratti** - [Fernando Gregoratti](https://github.com/mvkgamingarg) 

  

Gracias por llegar hasta aquí y espero que le haya sido de su agrado este proyecto integrador.  

 

 
 

 
