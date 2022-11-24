import sys
from parser import yacc
from lex import lexico, symbols_table
from flags import debug

st = symbols_table.SymbolsTable()

        
tokens = ("ID", "CTE_NUMERICA", "CTE_REAL", "CTE_STRING",
          "LLAVE_ABRE", "LLAVE_CIERRA", "PARENTESIS_ABRE", "PARENTESIS_CIERRA",
          "PUNTO_COMA","COMA",
          "OP_RESTA", "OP_SUMA", "OP_DIVISION", "OP_MULTIPLICACION", "OP_CONCAT",
          "COMP_MENOR", "COMP_MAYOR", "COMP_MENOR_IGUAL", "COMP_MAYOR_IGUAL", 
          "COMP_IGUAL", "COMP_DISTINTO",
          "OP_OR", "OP_AND", "OP_NOT",
          "OP_ASIGNACION", "CONDICION_TERNARIA", "DOS_PUNTOS",
          "while", "if", "else", "between", "out", "in", 
          "var", "string", "int", "real", "bool", "true", "false")

polaca = []

betweenId = None
betweenMinJmp = None
betweenMaxJmp = None

ifConditionAux = []
ifEndAux = []

ternaryJmpToFalsAux = None
ternaryJmpToEndAux = None

whileConditionAux = []
whileStartAux = []

andJmpAux = None
orJmpAux = None

variableTypeAux = None
defaultValueAux = None

operantionTypeAux = None
def validOperationType(operand):
    global operantionTypeAux
    if not operantionTypeAux:
        operantionTypeAux = operand.typeOf
        return True
    if operantionTypeAux != operand.typeOf:
        thrown(f"Cant operate {operantionTypeAux} with {operand.typeOf}")
        
def validAssignmentType(operand):
    global operantionTypeAux
    if operantionTypeAux != operand.typeOf:
        thrown(f"Cant assign value of type {operantionTypeAux} to {operand.typeOf}")
        
def definedVariable(symbol):
    if not symbol.typeOf: 
        thrown(f"Variable {symbol.name} not defined")

def thrown(error):
    print(f'\n[ERROR: {error}]\n')
    raise SyntaxError(error)

def appendVars():
    st.append({ 'value': 1, 'name': "_TRUE", 'typeOf': 'BOOL', 'length': 1})
    st.append({ 'value': 0, 'name': "_FALSE", 'typeOf': 'BOOL', 'length': 1})
    st.append({ 'value': 0, 'name': "@logicalAux", 'typeOf': 'BOOL', 'length': 1})
    st.append({ 'value': '', 'name': "@strAux", 'typeOf': 'STRING', 'length': 0})

# ------------------------- Rules
## ------------------------------ Program 
def p_program_with_variables(p):
    ''' program : variables_block statements '''
    if debug: print(''' program : variables_block statements ''')
    appendVars()
    p[0] = polaca

def p_program(p):
    ''' program : statements '''
    if debug: print(''' program : statements ''')
    appendVars()
    p[0] = polaca


## ------------------------------ Declaration of Variables
def p_variables_block(p):
    ''' variables_block : var LLAVE_ABRE variables_list LLAVE_CIERRA '''
    if debug: print(''' variables_block : var LLAVE_ABRE variables_list LLAVE_CIERRA ''')
    pass

def p_variables_list_r(p):
    ''' variables_list : variables_list variable_declaration '''
    if debug: print(''' variables_list : variables_list variable_declaration ''')
    pass

def p_variables_list(p):
    ''' variables_list : variable_declaration '''
    if debug: print(''' variables_list : variable_declaration ''')
    pass

def p_variable_declaration(p):
    ''' variable_declaration : variable_type variables_names PUNTO_COMA '''
    if debug: print(''' variable_declaration : variable_type variables_names PUNTO_COMA ''')
    pass

def p_variables_names_r(p):
    ''' variables_names : variables_names COMA ID '''
    global variableTypeAux, defaultValueAux
    symbol = st.getByIndex(p[3])
    if debug: print(f''' variables_names : variables_names COMA ID[{symbol.name}] ''')
    symbol.typeOf = variableTypeAux
    symbol.value = defaultValueAux

def p_variables_names(p):
    ''' variables_names : ID '''
    global variableTypeAux, defaultValueAux
    symbol = st.getByIndex(p[1])
    if debug: print(f''' variables_names : ID[{symbol.name}] ''')
    symbol.typeOf = variableTypeAux
    symbol.value = defaultValueAux
=======
    if info: print(f''' variable_declaration : {p[1]} {st.getByIndex(p[2])} ''')
    p[0] = p[1]

def p_variables_names_r(p):
    ''' variables_names : variables_names COMA ID '''
    if debug: print(f''' variables_names : variables_names COMA ID[{p[3]}] ''')
    if info: print(f''' variables_names : {st.getByIndex(p[1])}, {st.getByIndex(p[3])} ''')
    p[0] = p[1]

def p_variables_names(p):
    ''' variables_names : ID '''
    if debug: print(f''' variables_names : ID[{p[1]}] ''')
    if info: print(f''' variables_names : {st.getByIndex(p[1])} ''')
    p[0] = p[1]

### ----------------------------------- Variable Types
def p_variable_type_int(p):
    ''' variable_type : int '''
    global variableTypeAux, defaultValueAux
    if debug: print(''' variable_type : int ''')
    variableTypeAux = 'INT'
    defaultValueAux = 0

def p_variable_type_real(p):
    ''' variable_type : real '''
    global variableTypeAux, defaultValueAux
    if debug: print(''' variable_type : real ''')
    variableTypeAux = 'REAL'
    defaultValueAux = 0.0

def p_variable_type_string(p):
    ''' variable_type : string '''
    global variableTypeAux, defaultValueAux
    if debug: print(''' variable_type : string ''')
    variableTypeAux = 'STRING'
    defaultValueAux = ""

def p_variable_type_bool(p):
    ''' variable_type : bool '''
    global variableTypeAux, defaultValueAux
    if debug: print(''' variable_type : bool ''')
    variableTypeAux = 'BOOL'
    defaultValueAux = 1


## ------------------------------ Statements
def p_statements(p):
    ''' statements : statement '''
    if debug: print(''' statements : statement ''')
    pass
    
def p_statements_r(p):
    ''' statements : statements statement '''
    if debug: print(''' statements : statements statement ''')
    pass

def p_statement_assignment(p):
    ''' statement : assignment_statement '''
    if debug: print(f''' statement : assignment_statement''')
    pass

def p_statement_select(p):
    ''' statement : select_statement '''
    if debug: print(''' statement : select_statement ''')
    pass

def p_statement_while(p):
    ''' statement : while_statement '''
    if debug: print(''' statement : while_statement ''')
    pass

def p_statement_in(p):
    ''' statement : in_statement '''
    if debug: print(''' statement : in_statement ''')
    pass

def p_statement_out(p):
    ''' statement : out_statement '''
    if debug: print(''' statement : out_statement ''')
    pass

### ----------------------------------- While Statement
def p_while_keyword(p):
    ''' while_keyword : while '''
    if debug: print(f''' while_keyword : while ''')
    polaca.append("START_WHILE")
    whileStartAux.append(len(polaca))

def p_while_condition(p):
    ''' while_condition : logical_statement '''
    global whileConditionAux
    if debug: print(f''' while_condition : logical_statement ''')
    polaca.append("_TRUE")
    polaca.append("@logicalAux")
    polaca.append("CMP")
    polaca.append("JZ")
    whileConditionAux.append(len(polaca))
    polaca.append("_")

def p_while_statement(p):
    ''' while_statement : while_keyword while_condition LLAVE_ABRE statements LLAVE_CIERRA '''
    global whileEndAux
    if debug: print(f''' while_statement : while_keyword while_copndition LLAVE_ABRE statements LLAVE_CIERRA ''')
    polaca.append("J")
    polaca.append(f'[{whileStartAux.pop()}]')
    polaca[whileConditionAux.pop()] = f'[{len(polaca)}]'

### ----------------------------------- Select Statement
def p_select_statement_with_else_if(p):
    ''' select_statement : if_statement else_if_statement '''
    if debug: print(''' select_statement : if_statement else_if_statement ''')
    pass

def p_select_statement_with_else(p):
    ''' select_statement : if_statement else_statement'''
    if debug: print(''' select_statement : if_statement else_statement''')
    pass

def p_select_statement(p):
    ''' select_statement : if_statement '''
    if debug: print(''' select_statement : if_statement ''')
    pass

def p_if_condition(p):
    ''' if_condition :  logical_statement '''
    global ifConditionAux
    if debug: print(f''' if_condition :  logical_statement ''')
    polaca.append("_TRUE")
    polaca.append("@logicalAux")
    polaca.append("CMP")
    polaca.append("JZ")
    ifConditionAux.append(len(polaca))
    polaca.append("_") 

def p_if_statement(p):
    ''' if_statement :  if if_condition LLAVE_ABRE statements LLAVE_CIERRA '''
    global ifConditionAux
    if debug: print(f''' if_statement :  if if_condition LLAVE_ABRE statements LLAVE_CIERRA ''')
    polaca.append("J")
    ifEndAux.append(len(polaca))
    polaca.append(f"[{len(polaca) + 1}]")
    polaca[ifConditionAux.pop()] = f"[{len(polaca)}]"

def p_else_if_statement(p):
    ''' else_if_statement : else if_statement '''
    if debug: print(''' else_if_statement : else if_statement ''')
    pass

def p_else_if_statement_r(p):
    ''' else_if_statement : else_if_statement else if_statement '''
    if debug: print(''' else_if_statement : else_if_statement else if_statement ''')
    pass

def p_else_if_statement_r_with_else(p):
    ''' else_if_statement : else_if_statement else_statement '''
    if debug: print(''' else_if_statement : else_if_statement else_statement ''')
    pass

def p_else_statement(p):
    ''' else_statement : else LLAVE_ABRE statements LLAVE_CIERRA '''
    global ifEndAux
    if debug: print(''' else_statement : else LLAVE_ABRE statements LLAVE_CIERRA ''')
    for e in ifEndAux:
        polaca[e] = f"[{len(polaca)}]"
    ifEndAux = []


### ----------------------------------- Out Statement
def p_out_statement(p):
    ''' out_statement : out str_expression PUNTO_COMA '''
    global operantionTypeAux
    if debug: print(f''' out_statement : out str_expression PUNTO_COMA ''')
    operantionTypeAux = None
    polaca.append('PUT')

### ----------------------------------- In Statement
def p_in_statement(p):
    ''' in_statement : in ID PUNTO_COMA '''
    symbol = st.getByIndex(p[2])
    if debug: print(f''' in_statement : in ID[{symbol.name}] PUNTO_COMA ''')
    definedVariable(symbol)
    polaca.append(symbol.name)
    polaca.append('GET')

## ------------------------------ Arithmetic Operations
### ----------------------------------- Expression
def p_expression_plus(p):
    ''' expression : expression OP_SUMA term '''
    if debug: print(f''' expression : expression OP_SUMA term ''')
    polaca.append("+")
    
def p_expression_minus(p):
    ''' expression : expression OP_RESTA term '''
    if debug: print(f''' expression : expression OP_RESTA term ''')
    polaca.append("-")

def p_expression(p):
    ''' expression : term '''
    if debug: print(f''' expression : term ''')
    pass

### ----------------------------------- Term
def p_term_multp(p):
    ''' term : term OP_MULTIPLICACION factor '''
    if debug: print(f''' term : term OP_MULTIPLICACION factor ''')
    polaca.append("*")
    
def p_term_div(p):
    ''' term : term OP_DIVISION factor '''
    if debug: print(f''' term : term OP_DIVISION factor ''')
    polaca.append("/")
    
def p_term(p):
    ''' term : factor '''
    if debug: print(f''' term : factor ''')
    pass
    
### ----------------------------------- Factor
def p_factor_num(p):
    ''' factor : CTE_NUMERICA '''
    global operantionTypeAux
    symbol = st.getByIndex(p[1])
    if debug: print(f''' factor : CTE_NUMERICA[{symbol.name}] ''') 
    validOperationType(symbol)
    polaca.append(symbol.name)
    
def p_factor_real(p):
    ''' factor : CTE_REAL '''
    global operantionTypeAux
    symbol = st.getByIndex(p[1])
    if debug: print(f''' factor : CTE_REAL[{symbol.name}] ''') 
    validOperationType(symbol)
    polaca.append(symbol.name)
    
def p_factor_id(p):
    ''' factor : ID ''' 
    global operantionTypeAux
    symbol = st.getByIndex(p[1])
    if debug: print(f''' factor : ID[{symbol.name}] ''' )
    definedVariable(symbol)
    validOperationType(symbol)
    polaca.append(symbol.name)
    
def p_factor_expression(p):
    ''' factor : PARENTESIS_ABRE expression PARENTESIS_CIERRA ''' 
    if debug: print(f''' factor : PARENTESIS_ABRE expression PARENTESIS_CIERRA ''' )
    pass
    
def p_factor_negative(p):
    ''' factor : OP_RESTA factor '''
    if debug: print(f''' factor : OP_RESTA term ''')
    polaca.append("NEGATIVE")
    

## ------------------------------ String Expression
def p_str_expression_concat(p):
    ''' str_expression : str_term OP_CONCAT str_term '''
    global operantionTypeAux
    if debug: print(f''' str_expression : str_term OP_CONCAT str_term ''')
    operantionTypeAux = "STRING"
    polaca.append("CONCAT")

def p_str_expression(p):
    ''' str_expression : str_term '''
    global operantionTypeAux
    if debug: print(f''' str_expression : str_term ''')
    operantionTypeAux = "STRING"
    pass

def p_str_term_cte(p):
    ''' str_term : CTE_STRING '''
    symbol = st.getByIndex(p[1])
    if debug: print(f''' str_term : CTE_STRING[{symbol.name}] ''')
    polaca.append(symbol.name)
    
def p_str_term_id(p):
    ''' str_term : ID '''
    symbol = st.getByIndex(p[1])
    if debug: print(f''' str_term : ID[{symbol.name}] ''')
    definedVariable(symbol)
    polaca.append(symbol.name)


## ------------------------------ Comparision Operations
def p_comparision(p):
    ''' comparision : expression op_comparision expression '''
    if debug: print(f''' comparision : expression op_comparision[{p[2]}] expression ''')
    polaca.append("CMP")
    polaca.append(p[2])

def p_comparision_str(p):
    ''' comparision : str_expression op_comparision str_expression '''
    if debug: print(f''' comparision : str_expression op_comparision[{p[2]}] str_expression ''')
    polaca.append("CMP")
    polaca.append(p[2])

### ----------------------------------- Comparision Operators
def p_op_comparision_minor(p):
    ''' op_comparision : COMP_MENOR '''
    if debug: print(''' op_comparision : COMP_MENOR ''')
    p[0] = "JGE"

def p_op_comparision_major(p):
    ''' op_comparision : COMP_MAYOR '''
    if debug: print(f''' op_comparision : COMP_MAYOR ''')
    p[0] = "JLE"

def p_op_comparision_minor_eq(p):
    ''' op_comparision : COMP_MENOR_IGUAL '''
    if debug: print(''' op_comparision : COMP_MENOR_IGUAL ''')
    p[0] = "JG"

def p_op_comparision_major_eq(p):
    ''' op_comparision : COMP_MAYOR_IGUAL '''
    if debug: print(''' op_comparision : COMP_MAYOR_IGUAL ''')
    p[0] = "JL"

def p_op_comparision_equal(p):
    ''' op_comparision : COMP_IGUAL '''
    if debug: print(''' op_comparision : COMP_IGUAL ''')
    p[0] = "JNE"

def p_op_comparision_distinct(p):
    ''' op_comparision : COMP_DISTINTO '''
    if debug: print(''' op_comparision : COMP_DISTINTO ''')
    p[0] = "JE"


## ------------------------------ Logical Expressions
### ----------------------------------- Logical Statement
def p_logical_statement(p):
    ''' logical_statement : logical_expression '''
    if debug: print(f''' logical_statement : logical_expression ''')
    polaca.append(f"[{len(polaca) + 6}]")
    polaca.append("_TRUE")
    polaca.append(":=")
    polaca.append("@logicalAux")
    polaca.append("J")
    polaca.append(f"[{len(polaca) + 4}]")
    polaca.append("_FALSE")
    polaca.append(":=")
    polaca.append("@logicalAux")
    
# def p_logical_expression_not(p):
#     ''' logical_statement : OP_NOT logical_expression '''
#     if debug: print(f''' logical_expression : OP_NOT[{p[1]}] logical_term[{p[2]}] ''')
#     if info: print(f'logical_expression: {p[1]}, {p[2]}')
#     polaca.append(len(polaca) + 6)
#     polaca.append(0)
#     polaca.append("@logicalAux")
#     polaca.append(":=")
#     polaca.append("J")
#     polaca.append(len(polaca) + 4)
#     polaca.append(1)
#     polaca.append("@logicalAux")
#     polaca.append(":=")
# ''' logical_statement : left_or_expression OP_OR OP_NOT logical_expression '''
# ''' logical_statement : OP_NOT left_or_expression OP_OR logical_expression '''
# ''' logical_statement : OP_NOT left_or_expression OP_OR OP_NOT logical_expression '''

def p_logical_statement_or_operator(p):
    ''' logical_statement : left_or_expression OP_OR logical_expression '''
    global orJmpAux
    if debug: print(f''' logical_statement : left_or_expression OR logical_expression ''')
    polaca.append(f"[{len(polaca) + 4}]")
    polaca[orJmpAux] = f"[{len(polaca)}]"
    polaca.append("_TRUE")
    polaca.append('J')
    polaca.append(f"[{len(polaca) + 2}]")
    polaca.append("_FALSE")
    polaca.append(':=')
    polaca.append('@logicalAux')

def p_logical_left_or_expression(p):
    ''' left_or_expression : logical_expression '''
    global orJmpAux
    if debug: print(f''' left_or_expression : logical_expression ''')
    polaca.append(f"[{len(polaca) + 3}]")
    polaca.append('J')
    orJmpAux = len(polaca)
    polaca.append('_')

def p_logical_statement_and_operator(p):
    ''' logical_statement : left_and_expression OP_AND logical_expression '''
    global andJmpAux
    if debug: print(f''' logical_statement : left_and_expression AND logical_expression ''')
    polaca.append(f"[{len(polaca) + 4}]")
    polaca.append("_TRUE")
    polaca.append("J")
    polaca.append(f"[{len(polaca) + 2}]")
    
    polaca[andJmpAux] = f"[{len(polaca)}]"
    polaca.append("_FALSE")
    
    polaca.append(":=")
    polaca.append("@logicalAux")

def p_logical_left_and_expression(p):
    ''' left_and_expression : logical_expression '''
    global andJmpAux
    if debug: print(f''' left_and_expression : logical_expression ''')
    andJmpAux = len(polaca)
    polaca.append("_")

### ----------------------------------- Logical Expression
def p_logical_not_expression(p):
    ''' logical_expression : OP_NOT logical_term '''
    global operantionTypeAux
    if debug: print(f''' logical_expression : logical_term ''')
    operantionTypeAux = None
    polaca.append('NOT')
    
def p_logical_expression(p):
    ''' logical_expression : logical_term '''
    global operantionTypeAux
    if debug: print(f''' logical_expression : logical_term ''')
    operantionTypeAux = None
    pass

### ----------------------------------- Logical Term
def p_logical_term_comparision(p):
    ''' logical_term : comparision '''
    if debug: print(f''' logical_term : comparision ''')
    pass

def p_logical_term_between(p):
    ''' logical_term : between_statement '''
    if debug: print(f''' logical_term : between_statement ''')
    pass

def p_logical_term_cte(p):
    ''' logical_term : cte_logic '''
    if debug: print(f''' logical_term : cte_logic ''')
    pass
    

### ----------------------------------- Logical Constants
def p_cte_logic_true(p):
    ''' cte_logic : true '''
    if debug: print(f''' cte_logic : true ''')
    polaca.append("_TRUE")
    polaca.append("_TRUE")
    polaca.append("CMP")
    polaca.append("JZ")

def p_cte_logic_false(p):
    ''' cte_logic : false '''
    if debug: print(f''' cte_logic : false ''')
    polaca.append("_TRUE")
    polaca.append("_FALSE")
    polaca.append("CMP")
    polaca.append("JZ")

### ----------------------------------- Between Statement
def p_between_statement(p):
    ''' between_statement : between PARENTESIS_ABRE between_id COMA between_min DOS_PUNTOS between_max PARENTESIS_CIERRA '''
    global betweenMinJmp, betweenMaxJmp, operantionTypeAux
    if debug: print(f''' between_statement : between PARENTESIS_ABRE between_id COMA between_min DOS_PUNTOS between_max PARENTESIS_CIERRA ''')
    polaca.append("_TRUE")
    polaca.append("J")
    polaca.append(f"[{len(polaca) + 2}]")
    
    polaca[betweenMinJmp] = f"[{len(polaca)}]"
    polaca[betweenMaxJmp] = f"[{len(polaca)}]"
    polaca.append("_FALSE")
    
    polaca.append("_TRUE")
    polaca.append("CMP")
    polaca.append("JZ")
    operantionTypeAux = "BOOL"
    
def p_between_id(p):
    ''' between_id : ID '''
    global betweenId
    symbol = st.getByIndex(p[1])
    if debug: print(f''' between_id : ID[{symbol.name}] ''')
    definedVariable(symbol)
    validOperationType(symbol)
    betweenId = symbol.name
    
def p_between_min(p):
    ''' between_min : expression '''
    global betweenId, betweenMinJmp
    if debug: print(f''' between_min : expression ''')
    polaca.append(betweenId)
    polaca.append("CMP")
    polaca.append("JL")
    betweenMinJmp = len(polaca)
    polaca.append('_') # salto al final del between para asignar false
    
def p_between_max(p):
    ''' between_max : expression '''
    global betweenId, betweenMaxJmp
    if debug: print(f''' between_max : expression ''')
    polaca.append(betweenId)
    polaca.append("CMP")
    polaca.append("JG")
    betweenMaxJmp = len(polaca)
    polaca.append('_') # salto al final del between para asignar false


## ------------------------------ Assignment Statement
def p_assignment_statement(p):
    ''' assignment_statement : ID OP_ASIGNACION assignment_value PUNTO_COMA '''
    global operantionTypeAux
    symbol = st.getByIndex(p[1])
    if debug: print(f''' assignment_statement : ID[{symbol.name}] OP_ASIGNACION assignment_value PUNTO_COMA ''')
    definedVariable(symbol)
    validAssignmentType(symbol)
    operantionTypeAux = None
    
    if symbol.typeOf == "STRING":
        polaca.append("STRCPY")
    else: polaca.append(":=")
    polaca.append(symbol.name)

def p_assignment_value_ternary(p):
    ''' assignment_value : ternary '''
    if debug: print(f''' assignment_value : ternary ''')
    pass

def p_assignment_value_expression(p):
    ''' assignment_value : expression '''
    if debug: print(f''' assignment_value : expression ''')
    pass

def p_assignment_value_str(p):
    ''' assignment_value : str_expression '''
    if debug: print(f''' assignment_value : str_expression ''')
    pass

def p_assignment_value_logical(p):
    ''' assignment_value : logical_statement '''
    global operantionTypeAux
    if debug: print(f''' assignment_value : logical_statement ''')
    operantionTypeAux = "BOOL"
    polaca.append("@logicalAux")

### ----------------------------------- Ternary Operator
def p_ternary_condition(p):
    ''' ternary_condition : logical_statement '''
    global ternaryJmpToFalseAux
    if debug: print(f''' ternary_condition : logical_statement ''')
    polaca.append("_TRUE")
    polaca.append("@logicalAux")
    polaca.append("CMP")
    polaca.append("JZ")
    ternaryJmpToFalseAux = len(polaca)
    polaca.append("_")
    
def p_ternary_true_num_value(p):
    ''' ternary_true_value : expression '''
    global ternaryJmpToFalseAux, ternaryJmpToEndAux
    if debug: print(f''' ternary_true_value : expression ''')
    polaca.append("J")
    ternaryJmpToEndAux = len(polaca)
    polaca.append("_")
    polaca[ternaryJmpToFalseAux] = f"[{len(polaca)}]"
    
def p_ternary_true_str_value(p):
    ''' ternary_true_value : str_expression '''
    global ternaryJmpToFalseAux, ternaryJmpToEndAux
    if debug: print(f''' ternary_true_value : str_expression ''')
    polaca.append("J")
    ternaryJmpToEndAux = len(polaca)
    polaca.append("_")
    polaca[ternaryJmpToFalseAux] = f"[{len(polaca)}]"

def p_ternary_num(p):
    ''' ternary : ternary_condition CONDICION_TERNARIA ternary_true_value DOS_PUNTOS expression '''
    global ternaryJmpToEndAux
    if debug: print(f''' ternary : ternary_condition CONDICION_TERNARIA ternary_true_value DOS_PUNTOS expression ''')
    polaca[ternaryJmpToEndAux] = f"[{len(polaca)}]"

def p_ternary_str(p):
    ''' ternary : ternary_condition CONDICION_TERNARIA ternary_true_value DOS_PUNTOS str_expression '''
    global ternaryJmpToEndAux
    if debug: print(f''' ternary : ternary_condition CONDICION_TERNARIA ternary_true_value DOS_PUNTOS str_expression ''')
    polaca[ternaryJmpToEndAux] = f"[{len(polaca)}]"


## ------------------------------ Error Rule
def p_error(e):
    print(f"\n[ERROR: ${e}]\n")


def parse(source):
    print("Comienzo de Sintactico...\n")
    parser = yacc.yacc()  
    res = parser.parse(input=source, lexer=lexico.Lexer())
    print(f'\n- Polaca: \n{res}\n')
    if debug and res:
        print(f'- Simbolos: \n{st}')
        print(f'- Polaca Detallada:')
        for i, c in enumerate(res):
            print(f'[{i}] \t{c}')
    print("\n...Fin de Sintactico")
    return res
