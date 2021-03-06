
#### Universidad de San Carlos de Guatemala
#### Facultad de Ingeniería
#### Escuela de Ciencias y Sistemas
#### Área de Ciencias de la Computación
#### Organización de Lenguajes y Compiladores 2 - Sección A
#### Ing. Luis Fernando Espino Barrios
#### Aux. Juan Carlos Maeda    
<br>
<div style="text-align: justify">
<table class="default">
  <tr>
    <th>Nombre</th>
    <th>Carnet</th>
  </tr>
  <tr>
    <td>ROMARIO DAVID CASTILLO ECHEVERRIA</td>
    <td>201314064</td>
  </tr>
  <tr>
    <td>ROBERTO EDUARDO CASEROS REYNOSO</td>
    <td>201314177</td>
  </tr>
  <tr>
    <td>CARLOS ENRIQUE CANTÉ LÓPEZ</td>
    <td>201314448</td>
  </tr>
  <tr>
    <td>CARLOS GABRIEL PERALTA CAMBRAN</td>
    <td>201314556</td>
  </tr>
</table>
</div>
<br>

## Índice
- [SQL PARSER Grupo 7 - TytusDB](#SQL_PARSER_Grupo_7-TytusDB) 
- [Barra de Menú](#Barra_de_Menú)
- [Consola de Salida](#Consola_Salida)
- [Tabla de Errores](#Tabla_Errores)
- [Tabla de Simbolos](#Tabla_Simbolos)
- [Reporte_Gramatical](#Reporte_Gramatical)

<br>

# SQL_PARSER_Grupo_7-TytusDB

<div style="text-align: justify">Cuando se inicia la aplicacion, se podrá ver toda la interfaz QueryTool con todos sus módulos que la componen e igualmente las operaciones encargadas del funcionamiento del proyecto, tales como las opciones siguientes: guardar, guardar como, ver árbol, Analizar, entre otros que se detallaran mas adelante.  
<br>
<br>
<p align="center">
  <img src="img/inicio.PNG" width="600" alt="Inicio SQL PARSER">
</p>
</div>
<br>

## Barra_de_Menú 
<div style="text-align: justify">
<p align="center">
  <img src="img/menu1.png" width="150" alt="Menu">
  <img src="img/menu2.png" width="150" alt="Menu">
  <img src="img/menu3.png" width="150" alt="Menu">
</p>
</div>

* ### Abrir: 
Esta opción permite abrir cualquier archivo que contenga texto plano, y crea una nueva pestaña con el contenido del archivo.
* ### Guardar
Esta opción es para que guarde un archivo donde el contenido de la misma es lo que está en la pestaña seleccionada actualmente.
* ### Guardar Como...
Esta opción nos permite elegir la ubicación donde se guardara el contenido de la pestaña activa.
* ### Tabla de Errores
En Esta tabla se puede abrir el Reporte de Errores Léxicos, Sintácticos y Semanticos que contenga el Archivo de Entrada.
* ### Tabla de Simbolos
Esta opción muestra las variables, funciones y procedimientos con mínimo los siguientes datos: identificador, tipo, dimensión, declarada en, y referencias.
* ### AST
Esta opción muestra el árbol de sintaxis abstracta utilizando Graphviz en una nueva ventana.
* ### Reporte Gramatical
Esta opción genera un reporte de la gramática con Sintaxis BNF
* ### Botón Analizar
Realiza el Análisis Léxico, Sintáctico y Semántico del Archivo de entrada, asi como la ejecucion de las instrucciones.
<br>

## Consola_Salida 
<div style="text-align: justify">
Esta es otra parte de la Interfaz principal se observa una pestaña con un archivo cargado previamente mostrando todo su contenido. Adional se puede apreciar el Log en la Consola de Salida.
<br>
<br>
<p align="center">
  <img src="img/consola.PNG" width="600" alt="Consola de Salida">
</p>
</div>
<br>

## Tabla_Errores 
<div style="text-align: justify">
Así es como se verá un reporte en una página de los errores léxicos y sintácticos que se encontraron en el archivo que se analizó. Se muestra el número de errores encontrados, así como también el tipo, descripción y el carácter que provoco el error en sí.
<br>
<br>
<p align="center">
  <img src="img/tblerrores.PNG" width="600" alt="Tabla Errores">
</p>
</div>
<br>

## Tabla_Simbolos 
<div style="text-align: justify">
En este Reporte se puede apreciar las variables, funciones y procedimientos creatos en el ámbito Global.
<br>
<br>
<p align="center">
  <img src="img/tblsimbolos.PNG" width="600" alt="Tabla Simbolos">
</p>
</div>
<br>

## Reporte_Gramatical 
<div style="text-align: justify">
En este Reporte se puede apreciar la gramatica en formato BNF.
<br>
<br>
<p align="center">
  <img src="img/rg.PNG" width="600" alt="Reporte Gramatical">
</p>
</div>
<br>

## AST 
<div style="text-align: justify">
En este Reporte se genera el AST.
<br>
<br>
<p align="center">
  <img src="img/Arbol.PNG" width="600" alt="Reporte Gramatical">
</p>
</div>
<br>

## TRADUCIR C3D
<div style="text-align: justify">
Con este boton se traduce cualquier instrucción SQL o PL/pgsql a codigo tres direcciones.
<br>
<br>
<p align="center">
  <img src="img/c3d.PNG" width="600" alt="Reporte Gramatical">
</p>
</div>
<br>


## Ejecutar C3D
<div style="text-align: justify">
Se ejecutan las sentencias del codigo 3 direcciones.
<br>
<br>
<p align="center">
  <img src="img/consola.PNG" width="600" alt="Reporte Gramatical">
</p>
</div>
<br>

## Optimizar C3D
<div style="text-align: justify">
Se aplican las reglas de mirilla y se genera un codigo de tres direcciones optimizado.
<br>
<br>
<p align="center">
  <img src="img/c3d_optimizado.PNG" width="600" alt="Reporte Gramatical">
</p>
</div>
<br>

## Reporte de optimizacion
<div style="text-align: justify">
Al aplicarse las reglas de mirilla y generar el codigo optimizado, se genera un reporte de las reglas de mirilla aplicadas en la optimizacion.
<br>
<br>
<p align="center">
  <img src="img/opt_reporte.PNG" width="600" alt="Reporte Gramatical">
</p>
</div>
<br>