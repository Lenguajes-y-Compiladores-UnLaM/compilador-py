# -----------------------------------------------------------------------------------------------------------
#                        === Clase Lexer (Motor Lexico) ===
# 
# Clase que representa al analizador lexico. 
# Se realiza como una clase ya que así debe ser llamada desde el parser PLY. 
#
# Restricciones impuestas por el parser del PLY:
#   . Metodo Token()
#   . Metodo Input()
#
#   Funciones:
#       input()                     - Función que almacena archivo de entrada.
#       token()                     - Función que consulta caracteres hasta obtener un token
#       unread()                    - Función que retorna el cursor luego de etregar token.
#       get_column()                - Función que devuelve la columna correspondiente al caracter leido para definir función asociada y proximo estado.

# -----------------------------------------------------------------------------------------------------------

from lex import process_table as pt, states_table as st, token_table as tt, keyword_table as kt, symbols_table
from flags import debug
sym = symbols_table.SymbolsTable()


class LexToken(object):
    def __init__(self, type, value, lineno, lexpos):
        self.type = type
        self.value = value
        self.lineno = lineno
        self.lexpos = lexpos
        
    def __str__(self):
        return 'LexToken(type: %s; value: %r)' % (self.type, self.value)

    def __repr__(self):
        return str(self)

class Lexer: 
    def __init__(self):
        self.source = None
        self.lexpos = None
        

    def get_column(self, char):
        if not char: return 23
        if char == '': return 23
        if char >= 'A' and char <= 'Z': return 0
        if char >= 'a' and char <= 'z': return 0
        if char >= '0' and char <= '9': return 1
        if char == '"': return 2
        if char == '{': return 3
        if char == '}': return 4
        if char == '(': return 5
        if char == ')': return 6
        if char == '.': return 7
        if char == ';': return 8
        if char == ',': return 9
        if char == '-': return 10
        if char == '+': return 11
        if char == '/': return 12
        if char == '*': return 13
        if char == '<': return 14
        if char == '>': return 15
        if char == '|': return 16
        if char == '&': return 17
        if char == '!': return 18
        if char == '=': return 19
        if char == ':': return 20
        if char == '?': return 21
        if char == ' ': return 22
        if char == '\t': return 22
        if char == '\n': return 22
        if char == '\r': return 22
        

    def unread(self):
        if self.lexpos >= 0:
            self.lexpos -= 1
        
    def read(self):
        if self.lexpos >= self.maxpos:
            return None
        char = self.source[self.lexpos]
        self.lexpos += 1
        return char
        
        
    def input(self, s):
        self.source = s
        self.lexpos = 0
        self.maxpos = len(s)
        
# -----------------------------------------------------------------------------------------------------------
#                        === Metodo Token ===
# 
# 1. Define Estado inicial, estado final y estado de error 
# 2. Lee el primer caracter
# 3. Mientras no se llegue a un estado final, se itera
# 4. Se obtiene columna asociada al primer caracter leido.
# 5. Se ejecuta funcion asociada al estado actual gracias a la Matriz de Funciones
# 6. Se guarda el estado actual
# 7. Se consulta siguiente estado
# 8. Si no hay siguiente estado, se retorna NULL
# 9. Si el estado es Final, se obtiene token gracias a la Matriz de Tokens. Si el token es ID, se obtiene el label
# 10. Si el estado no es final, leo el siguiente caracter.
# 11. Llegado al estado final, Si no es el EOF, vuelvo el cursor una posicion atras.
# 12. Retorno el Token.
# -----------------------------------------------------------------------------------------------------------

    def token(self):
        state = 0
        final_state = -1
        error_state = -2
        char = self.read()
        
        while state != final_state:
            column = self.get_column(char)
            if not char and state == 0:
                break
            
            response = pt.process_table[state][column](char)
            
            last = state
            state = st.next_state[state][column]
            
            if state == error_state:
                if debug: print(f"STATE ERROR")
                return None
            
            if state == final_state:
                token = tt.get_token_label(last, column)
                if token["type"] == "ID":
                    token = kt.keyword_token_label(response)
                if token["type"] in ["ID", "CTE_NUMERICA", "CTE_REAL", "CTE_STRING"]:
                    token["value"] = response
                break
            
            char = self.read()
                
        if column != 23:
            self.unread()
        if not char and state == 0:
            if debug: print(f"EOF")
            return None
        res_token = LexToken(token["type"], token["value"], 0, 0)
        if debug: print(res_token)
        return res_token
