import sys
from parser import yacc
from lex import lexico, symbols_table

st = symbols_table.SymbolsTable()

debug = False
info = True
        
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
ifConditionAux = None
ifEndAux = []

# ------------------------- Rules
## ------------------------------ Program 
def p_program_with_variables(p):
    ''' program : variables_block statements '''
    if debug: print(''' program : variables_block statements ''')
    if info: print(f'program: {p[1]}')
    p[0] = p[1]

def p_program(p):
    ''' program : statements '''
    if debug: print(''' program : statements ''')
    if info: print(f'program: {p[1]}')
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
    if debug: print(''' variable_type : int ''')
    p[0] = 'int'

def p_variable_type_real(p):
    ''' variable_type : real '''
    if debug: print(''' variable_type : real ''')
    pass

def p_variable_type_string(p):
    ''' variable_type : string '''
    if debug: print(''' variable_type : string ''')
    pass

def p_variable_type_bool(p):
    ''' variable_type : bool '''
    if debug: print(''' variable_type : bool ''')
    pass


## ------------------------------ Statements
def p_statements(p):
    ''' statements : statement '''
    if debug: print(''' statements : statement ''')
    if info: print(f'statements : {p[1]}')
    p[0] = p[1]
    
def p_statements_r(p):
    ''' statements : statements statement '''
    if debug: print(''' statements : statements statement ''')
    p[0] = p[1]

def p_statement_assignment(p):
    ''' statement : assignment_statement '''
    if debug: print(f''' statement : assignment_statement[{p[1]}]''')
    if info: print(f'statement : {p[1]}')
    p[0] = p[1]

def p_statement_select(p):
    ''' statement : select_statement '''
    if debug: print(''' statement : select_statement ''')
    # p[0] = p[1]
    pass

def p_statement_while(p):
    ''' statement : while_statement '''
    if debug: print(''' statement : while_statement ''')
    # p[0] = p[1]
    pass

def p_statement_in(p):
    ''' statement : in_statement '''
    if debug: print(''' statement : in_statement ''')
    # p[0] = p[1]
    pass

def p_statement_out(p):
    ''' statement : out_statement '''
    if debug: print(''' statement : out_statement ''')
    # p[0] = p[1]
    pass

### ----------------------------------- While Statement
def p_while_statement(p):
    ''' while_statement : while logical_statement LLAVE_ABRE statements LLAVE_CIERRA '''
    if debug: print(f''' while_statement : while logical_statement[{p[2]}] LLAVE_ABRE statements LLAVE_CIERRA ''')
    pass

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
    if debug: print(f''' if_statement :  if logical_statement[{p[2]}] LLAVE_ABRE statements LLAVE_CIERRA ''')
    polaca.append("logicalAux")
    polaca.append("CMP")
    polaca.append("JZ")
    ifConditionAux = len(polaca)
    polaca.append("_")
    print(ifConditionAux)
    print(polaca)  

def p_if_statement(p):
    ''' if_statement :  if if_condition LLAVE_ABRE statements LLAVE_CIERRA '''
    global ifConditionAux
    if debug: print(f''' if_statement :  if logical_statement[{p[2]}] LLAVE_ABRE statements LLAVE_CIERRA ''')
    polaca.append("J")
    ifEndAux.append(len(polaca))
    polaca.append("_")
    polaca[ifConditionAux] = len(polaca)

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
        polaca[e] = len(polaca)
    ifEndAux = []


### ----------------------------------- Out Statement
def p_out_statement(p):
    ''' out_statement : out str_expression PUNTO_COMA '''
    if debug: print(f''' out_statement : out str_expression[{p[2]}] PUNTO_COMA ''')
    # p[0] = p[1]
    pass

### ----------------------------------- In Statement
def p_in_statement(p):
    ''' in_statement : in ID PUNTO_COMA '''
    if debug: print(f''' in_statement : in ID[{p[2]}] PUNTO_COMA ''')
    # p[0] = p[1]
    pass

## ------------------------------ Arithmetic Operations
### ----------------------------------- Expression
def p_expression_plus(p):
    ''' expression : expression OP_SUMA term '''
    if debug: print(f''' expression : expression[{p[1]}] OP_SUMA term[{p[3]}] ''')
    if info: print(f'expression: {p[1]},  {p[3]}, +')
    polaca.append("+")
    
def p_expression_minus(p):
    ''' expression : expression OP_RESTA term '''
    if debug: print(f''' expression : expression[{p[1]}] OP_RESTA term[{p[3]}] ''')
    if info: print(f'expression: {p[1]}, {p[3]}, -')
    polaca.append("-")

def p_expression(p):
    ''' expression : term '''
    if debug: print(f''' expression : term[{p[1]}] ''')
    if info: print(f'expression: {p[1]}')

### ----------------------------------- Term
def p_term_multp(p):
    ''' term : term OP_MULTIPLICACION factor '''
    if debug: print(f''' term : term[{p[1]}] OP_MULTIPLICACION factor[{p[3]}] ''')
    if info: print(f'term: {p[1]} * {p[3]}')
    polaca.append("*")
    
def p_term_div(p):
    ''' term : term OP_DIVISION factor '''
    if debug: print(f''' term : term[{p[1]}] OP_DIVISION factor[{p[3]}] ''')
    if info: print(f'term: {p[1]} / {p[3]}')
    polaca.append("/")
    
def p_term(p):
    ''' term : factor '''
    if debug: print(f''' term : factor[{p[1]}] ''')
    if info: print(f'term: {p[1]}')
    
### ----------------------------------- Factor
def p_factor_num(p):
    ''' factor : CTE_NUMERICA '''
    if debug: print(f''' factor : CTE_NUMERICA[{p[1]}] ''') 
    if info: print(f'factor: {p[1]}')
    polaca.append(st.getByIndex(p[1]).value)
    
def p_factor_real(p):
    ''' factor : CTE_REAL '''
    if debug: print(f''' factor : CTE_REAL[{p[1]}] ''') 
    if info: print(f'factor: {p[1]}')
    polaca.append(st.getByIndex(p[1]).value)
    
def p_factor_id(p):
    ''' factor : ID ''' 
    if debug: print(f''' factor : ID[{p[1]}] ''' )
    if info: print(f'factor: {p[1]}')
    polaca.append(st.getByIndex(p[1]))
    
def p_factor_expression(p):
    ''' factor : PARENTESIS_ABRE expression PARENTESIS_CIERRA ''' 
    if debug: print(f''' factor : PARENTESIS_ABRE expression[{p[2]}] PARENTESIS_CIERRA ''' )
    if info: print(f'factor: ({p[2]})')
    
def p_factor_negative(p):
    ''' factor : OP_RESTA factor '''
    if debug: print(f''' factor : OP_RESTA term[{p[2]}] ''')
    if info: print(f'factor: {-p[2]}')
    polaca.append("-")

## ------------------------------ String Expression
def p_str_expression_concat(p):
    ''' str_expression : str_term OP_CONCAT str_term '''
    if debug: print(f''' str_expression : str_term[{p[1]}] OP_CONCAT str_term[{p[3]}] ''')
    if info: print(f''' str_expression : {st.getByIndex(p[1])}, {st.getByIndex(p[3])}, ++ ''')
    p[0] = f'{p[1]}, {p[3]}, ++'

def p_str_expression(p):
    ''' str_expression : str_term '''
    if debug: print(f''' str_expression : str_term[{p[1]}] ''')
    if info: print(f''' str_expression : {st.getByIndex(p[1])} ''')
    p[0] = p[1]

def p_str_term_cte(p):
    ''' str_term : CTE_STRING '''
    if debug: print(f''' str_term : CTE_STRING[{p[1]}] ''')
    if info: print(f''' str_term : {st.getByIndex(p[1])} ''')
    p[0] = p[1]
    
def p_str_term_id(p):
    ''' str_term : ID '''
    if debug: print(f''' str_term : ID[{p[1]}] ''')
    if info: print(f''' str_term : {p[1]} ''')
    p[0] = p[1]


## ------------------------------ Comparision Operations
def p_comparision(p):
    ''' comparision : expression op_comparision expression '''
    if debug: print(f''' comparision : expression[{p[1]}] op_comparision[{p[2]}] expression[{p[3]}] ''')
    polaca.append("CMP")
    polaca.append(p[2])

def p_comparision_str(p):
    ''' comparision : str_expression op_comparision str_expression '''
    if debug: print(f''' comparision : str_expression[{p[1]}] op_comparision[{p[2]}] str_expression[{p[3]}] ''')
    polaca.append("CMP")
    polaca.append(p[2])

### ----------------------------------- Comparision Operators
def p_op_comparision_minor(p):
    ''' op_comparision : COMP_MENOR '''
    if debug: print(''' op_comparision : COMP_MENOR ''')
    if info: print(f'comparision: {p[1]}')
    p[0] = "JGE"

def p_op_comparision_major(p):
    ''' op_comparision : COMP_MAYOR '''
    if debug: print(f''' op_comparision : {p[1]} COMP_MAYOR ''')
    if info: print(f'comparision: {p[1]}')
    p[0] = "JLE"

def p_op_comparision_minor_eq(p):
    ''' op_comparision : COMP_MENOR_IGUAL '''
    if debug: print(''' op_comparision : COMP_MENOR_IGUAL ''')
    if info: print(f'comparision: {p[1]}')
    p[0] = "JG"

def p_op_comparision_major_eq(p):
    ''' op_comparision : COMP_MAYOR_IGUAL '''
    if debug: print(''' op_comparision : COMP_MAYOR_IGUAL ''')
    if info: print(f'comparision: {p[1]}')
    p[0] = "JL"

def p_op_comparision_equal(p):
    ''' op_comparision : COMP_IGUAL '''
    if debug: print(''' op_comparision : COMP_IGUAL ''')
    if info: print(f'comparision: {p[1]}')
    p[0] = "JNE"

def p_op_comparision_distinct(p):
    ''' op_comparision : COMP_DISTINTO '''
    if debug: print(''' op_comparision : COMP_DISTINTO ''')
    if info: print(f'comparision: {p[1]}')
    p[0] = "JE"


## ------------------------------ Logical Expressions
### ----------------------------------- Logical Statement
def p_logical_statement(p):
    ''' logical_statement : logical_expression '''
    if debug: print(f''' logical_statement : logical_expression[{p[1]}] ''')
    polaca.append("+6")
    polaca.append("1")
    polaca.append("logicalAux")
    polaca.append(":=")
    polaca.append("J")
    polaca.append("+4")
    polaca.append("0")
    polaca.append("logicalAux")
    polaca.append(":=")

def p_logical_statement_or_operator(p):
    ''' logical_statement : logical_expression OP_OR logical_expression '''
    if debug: print(f''' logical_statement : logical_expression[{p[1]}] OR logical_expression[{p[3]}] ''')
    if info: print(f'logical_statement: {p[1]}, OR, {p[2]}')
    polaca.append("or")

def p_logical_statement_and_operator(p):
    ''' logical_statement : logical_expression OP_AND logical_expression '''
    if debug: print(f''' logical_statement : logical_expression[{p[1]}] AND logical_expression[{p[3]}] ''')
    if info: print(f'logical_statement: {p[1]}, AND, {p[2]}')
    polaca.append("and")

### ----------------------------------- Logical Expression
def p_logical_expression_not(p):
    ''' logical_expression : OP_NOT logical_term '''
    if debug: print(f''' logical_expression : OP_NOT[{p[1]}] logical_term[{p[2]}] ''')
    if info: print(f'logical_expression: {p[1]}, {p[2]}')
    polaca.append("not")

def p_logical_expression(p):
    ''' logical_expression : logical_term '''
    if debug: print(f''' logical_expression : logical_term[{p[1]}] ''')

### ----------------------------------- Logical Term
def p_logical_term_comparision(p):
    ''' logical_term : comparision '''
    if debug: print(f''' logical_term : comparision[{p[1]}] ''')

def p_logical_term_between(p):
    ''' logical_term : between_statement '''
    if debug: print(f''' logical_term : between_statement[{p[1]}] ''')

def p_logical_term_cte(p):
    ''' logical_term : cte_logic '''
    if debug: print(f''' logical_term : cte_logic[{p[1]}] ''')
    if info: print(f'logical_term :{p[1]}')

### ----------------------------------- Logical Constants
def p_cte_logic_true(p):
    ''' cte_logic : true '''
    if debug: print(f''' cte_logic : true[{p[1]}] ''')
    if info: print(f'cte_logic: {p[1]}')
    polaca.append("1")

def p_cte_logic_false(p):
    ''' cte_logic : false '''
    if debug: print(f''' cte_logic : false[{p[1]}] ''')
    if info: print(f'cte_logic: {p[1]}')
    polaca.append("0")

### ----------------------------------- Between Statement
def p_between_statement(p):
    ''' between_statement : between PARENTESIS_ABRE ID COMA expression DOS_PUNTOS expression PARENTESIS_CIERRA '''
    if debug: print(f''' between_statement : between PARENTESIS_ABRE ID[{p[3]}] COMA expression[{p[5]}] DOS_PUNTOS expression[{p[7]}] PARENTESIS_CIERRA ''')
    if info: print(f'between: {p[3]}, {p[5]}, >=, {p[3]}, {p[7]}, <=, &&')
    p[0] = f'{p[3]}, {p[5]}, >=, {p[3]}, {p[7]}, <=, &&'


## ------------------------------ Assignment Statement
def p_assignment_statement(p):
    ''' assignment_statement : ID OP_ASIGNACION assignment_value PUNTO_COMA '''
    if debug: print(f''' assignment_statement : ID[{p[1]}] OP_ASIGNACION assignment_value[{p[3]}] PUNTO_COMA ''')
    if info: print(f'assignment_statement: {p[3]}, {p[1]}, =')
    # semantica de asignar valor a la variable
    polaca.append(st.getByIndex(p[1]).name)
    polaca.append(":=")

def p_assignment_value_ternary(p):
    ''' assignment_value : ternary '''
    if debug: print(f''' assignment_value : ternary[{p[1]}] ''')
    pass

def p_assignment_value_expression(p):
    ''' assignment_value : expression '''
    if debug: print(f''' assignment_value : expression[{p[1]}] ''')
    if info: print(f'assignment_value: {p[1]}')

def p_assignment_value_str(p):
    ''' assignment_value : str_expression '''
    if debug: print(f''' assignment_value : str_expression[{p[1]}] ''')
    pass

def p_assignment_value_logical(p):
    ''' assignment_value : logical_statement '''
    if debug: print(f''' assignment_value : logical_statement[{p[1]}] ''')
    if info: print(f'assignment_value: {p[1]}')
    polaca.append("logicalAux")

### ----------------------------------- Ternary Operator
def p_ternary_num(p):
    ''' ternary : logical_statement CONDICION_TERNARIA expression DOS_PUNTOS expression '''
    if debug: print(f''' ternary : logical_statement[{p[1]}] CONDICION_TERNARIA expression[{p[3]}] DOS_PUNTOS expression[{p[5]}] ''')
    pass

def p_ternary_str(p):
    ''' ternary : logical_statement CONDICION_TERNARIA str_expression DOS_PUNTOS str_expression '''
    if debug: print(f''' ternary : logical_statement[{p[1]}] CONDICION_TERNARIA str_expression[{p[3]}] DOS_PUNTOS str_expression[{p[5]}] ''')
    pass


## ------------------------------ Error Rule
def p_error(e):
    print(f"\n[ERROR: ${e}]\n")


def parse(source):
    parser = yacc.yacc()  
    res = parser.parse(input=source, lexer=lexico.Lexer())
    print(st)
    return res
