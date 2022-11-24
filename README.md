# [Grupo 3] Compilador 
## Universidad Nacional del Oeste  
### Desarrollo de Compiladores  

Profesores:
- Jorge Doorn
- Hernan Pablo Villareal

Integrantes:
- Pablo Hernan Rechimon
- Ignacio Agustin Garcia Ravlic

Tema del Grupo:  
```BETWEEN(variable1, [expresion1; expresion2])```

Repositorio:
https://github.com/IgnaGarcia/compilador-py

## Ejecucion
Dependencias:
``` pip install -r requirements.txt ```
Nota: se debe haber instalado previamente `python 3.10`

Compilador:  
```py main.py {path del sourcefile}```  
*Nota*: En el archivo `flags` podra configurar el log level y si guardara los logs en un archivo

Tests:  
```py -m pytest -v --continue-on-collection-errors --no-header```  
```py -m pytest -v --continue-on-collection-errors --no-header --self-contained-html --html=report.html```  


## Funcionamiento
El flujo del programa comienza en el archivo `main.py`, lo primero que hace es abrir el archivo recibido por argumentos, una vez abierto lo lee por completo y lo pasa por parametros al `sintactico`.
El `sintactico` respondera con una `polaca` y esta sera usada como parametro para el `asembler`.
### Sintactico
El `sintactico` tiene el conjunto de reglas validas en forma de funcion, la regla se especifica en el primer string de esa funcion. Ademas posee una serie de variables globales, como la polaca que se ira generando, variables auxiliares y banderas, la tabla de simbolos y otras funciones auxiliares. En la carpeta del parser ademas hay otros archivos, `yacc` es la dependencia del ply, y otros autogeneradors como `parser.out` y `parsetab.py`.
El punto de entrada al `sintactico` es el metodo `parse`, el cual recibe como parametro el contenido del archivo, este metodo crea una instancia del `yacc` y ejecuta el parser pasandole el contenido del archivo y una instancia del lexico.
El parser comenzara a leer `tokens` e ira aplicando las reglas y estas reglas realizaran una accion(o no) sobre la `polaca` y/o la `tabla de simbolos`, una vez llegue a la regla de program volvera al comieno del metodo `parse` y retornara la `polaca`.
### Lexico
El `lexico` se compone de varios archivos, siendo `lexico.py` el principal, cuenta con una clase para representar a los `Tokens` y otra para la identificacion de estos en el archivo de entrada. El metodo principal de esto es el `token`, el cual leera un caracter del archivo, en base a este caracter y al estado en el automata de lectura realizara una accion y evalua cual es el siguiente estado, esto se repite hasta que ya no haya siguiente estado, en este momento se evalua cual es el token a generar. 
Para realizar esto se apoya sobre estos archivos:
- `probress_table`: contiene las acciones que hay que realizar para cada transicion entre caracteres, como ir generando una constante o guardar esta en la tabla de simbolos.
- `states_table`: contiene cual es el siguiente estado dentro del automata de lectura, el siguiente se calcula en base al estado actual y el caracter leido.
- `token_table`: contiene el token a generar en base a lo leido y el ultimo estado(previo al estado de cierre).
- `keyword_table`: contiene un subconjunto de tokens a generar, se evalua si un nombre de variable en realidad no sea una palabra reservada.
- `symbols-table`: singleton que almacena los simbolos que usara el programa cuando se ejecute, estos simbolos tienen informacion basica de cada variable y constante.
### Asembler
El `asembler` se compone del archivo `asembler`, el cual realiza la tarea de transformar la `polaca` en `codigo maquina`, esto lo hace en partes, en un principio crea el archivo de salida, escribe la cabecera de asembler, escribe las variables a usar y procede a escribir el codigo fuente. El metodo principal es `writeCode`, el cual lee celda por celda, evalua si es un operador o si hay algun flag activado para determinar la accion a realizar y el codigo a escribir.
Para hacer esto se apoya de los `helpers`, que son constantes y funciones que tienen templates de codigo asembler para distintas instrucciones.


## Temas Pendientes:
- Compilacion y ejecucion en el flujo general
### Sintactico
- Menos unario para constantes numericas
- Operador NOT logico
### Lexico
- 
### Asembler
- Operaciones aritmeticas con resultados negativos
- Concatenacion de Strings con Numeros
- Comparacion de Strings
- Bug en between