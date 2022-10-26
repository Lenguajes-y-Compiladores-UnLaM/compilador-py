# -----------------------------------------------------------------------------------------------------------
#                        === Matriz de Funciones ===
# 
# Matriz de funciones asociadas a los estados del automata. 
# La Mariz esta completa con los punteros a las funciones asociadas correspondientes a cada estado de AF.
#
#   Variables Globales:
#       counter                     - Utilizado para verificar cantidad de caracteres de un id, CTE_STRING, CTE_INT, CTE_REAL
#       string_limit                - limite de la constante string
#       string_id_limit             - limite de un id
#       int_limit                   - limite de un entero
#       real_int_limit              - limite de un real
#       real_decimal_limit          - limite decimal
#       id                          - Utilizado para concatenar los caracteres de un id o CTE_STRING
#       cte_numerica                - Utilizado para concatenar los caracteres de una CTE_INT o CTE_REAL
# 
#   Funciones:
#       do_nothing()                - Función que no hace nada. Sirve para todos los estados donde no se debe concatenar caracteres
#       start_string_id()           - Función que inicializa un ID y inicializa el contador
#       add_string_id()             - Función que concatena caracter siempre que no supere el limite, y incrementa el contador.
#       save_string_id()            - Función que retorna el ID.
#       start_int()                 - Función que inicializa una CTE_INT y inicializa el contador
#       add_int()                   - Función que concatena caracter numerico siempre que no supere el limite, y incrementa el contador.
#       save_int()                  - Función que retorna la CTE_INT
#       start_real()                - Función que inicializa un CTE_REAL y inicializa el contador
#       add_real()                  - Función que concatena caracter numerico siempre que no supere el limite, y incrementa el contador.
#       save_real()                 - Función que retorna la CTE_REAL
#       start_string()              - Función que inicializa un CTE_STRING y inicializa el contador
#       add_string()                - Función que concatena caracter siempre que no supere el limite, y incrementa el contador.
#       save_string()               - Función que retorna la CTE_STRING
# -----------------------------------------------------------------------------------------------------------

from lex import symbols_table as st
from lex import keyword_table as kt

# Global Variables
#Counter
counter = 0

# Limits
string_limit = 144
string_id_limit = 32
int_limit = 6
real_int_limit = 6
real_decimal_limit = 4
lastSymbolIndex = 0


# ID
id = ''

# CTE Entera
cte_numerica = ''


def do_nothing(_):
    return

def start_string_id(char):
    global id, counter
    id = char
    counter = 1
    return

def add_string_id(char):
    global counter
    global id
    if counter <= string_id_limit:
        id += char
        counter += 1
    return

def save_string_id(_):
    global id
    if kt.keyword_token_label(id)["type"] == "ID":
        return st.SymbolsTable().append({ 'value': None, 'name': id, 'typeOf': None, 'length': 0})
    return id

def start_int(char):
    global cte_numerica, counter
    cte_numerica = ''
    cte_numerica = char
    counter = 1
    return

def add_int(char):
    global cte_numerica, counter
    if counter <= int_limit:
        cte_numerica += char
        counter += 1
    return

def save_int(_):
    global cte_numerica
    return st.SymbolsTable().append({ 'value': int(cte_numerica), 'name': f"${cte_numerica}", 'typeOf': 'INT', 'length': len(cte_numerica)})

def start_real(char):
    global cte_numerica, counter
    cte_numerica = ''
    cte_numerica = char
    counter = 1
    return

def add_real(char):
    global cte_numerica, counter
    if counter <= int_limit:
        cte_numerica += char
        counter += 1
    return

def save_real(_):
    global cte_numerica
    return st.SymbolsTable().append({ 'value': float(cte_numerica), 'name': f"${cte_numerica}", 'typeOf': 'REAL', 'length': len(cte_numerica)})

def start_string(char):
    global id, counter
    id = ''
    counter = 1
    return

def add_string(char):
    global counter
    global id
    if counter <= string_limit:
        id += char
        counter += 1
    return

def save_string(_):
    global id
    global lastSymbolIndex
    lastSymbolIndex = st.SymbolsTable().append({ 'value': id, 'name': f"${id}", 'typeOf': 'STRING', 'length': len(id)})
    return lastSymbolIndex

def get_string_index(_):
    global lastSymbolIndex
    return lastSymbolIndex

process_table=[
    [start_string_id, start_int, start_string,do_nothing,do_nothing,do_nothing,do_nothing,	start_real,	do_nothing,	do_nothing,	do_nothing,	do_nothing,	do_nothing,	do_nothing,	do_nothing,	do_nothing,	do_nothing,	do_nothing,	do_nothing,	do_nothing,	do_nothing,	do_nothing,	do_nothing,	do_nothing],
    [add_string_id, add_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id],
    [save_int,	add_int,	save_int, save_int,	save_int, save_int,	save_int, add_real, save_int, save_int, save_int, save_int, save_int, save_int, save_int, save_int, save_int, save_int, save_int, save_int, save_int, save_int, save_int, save_int],
    [save_real,add_real,save_real,save_real,save_real,save_real,save_real,save_real,save_real,save_real,save_real,save_real,save_real,save_real,save_real,save_real,save_real,save_real,save_real,save_real,save_real,save_real,save_real,save_real],
    [add_string,add_string,save_string,add_string,add_string,add_string,add_string,add_string,add_string,add_string,add_string,add_string,add_string,add_string,add_string,add_string,add_string,add_string,add_string,add_string,add_string,add_string,add_string,do_nothing],
    [get_string_index,get_string_index,get_string_index,get_string_index,get_string_index,get_string_index,get_string_index,get_string_index,get_string_index,get_string_index,get_string_index,get_string_index,get_string_index,get_string_index,get_string_index,get_string_index,get_string_index,get_string_index,get_string_index,get_string_index,get_string_index,get_string_index,get_string_index,get_string_index],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing, add_real, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
]