import ply.yacc as yacc
from lexer import tokens
import os

# Grammar rules

def p_program(p):
    '''program : statements'''
    pass

def p_statements(p):
    '''statements : statements statement
                  | statement'''
    pass

def p_statement(p):
    '''statement : variable_declaration
                 | assignment
                 | print_statement
                 | input_statement
                 | if_statement
                 | for_loop'''
    pass

def p_variable_declaration(p):
    '''variable_declaration : TYPE IDENTIFIER SEMI'''
    pass

def p_assignment(p):
    '''assignment : IDENTIFIER ASSIGN expression SEMI'''
    pass

def p_expression(p):
    '''expression : term
                  | expression PLUS term
                  | expression MINUS term
                  | expression TIMES term
                  | expression DIVIDE term'''
    pass

def p_term(p):
    '''term : NUMBER
            | STRING
            | IDENTIFIER
            | BOOLEAN'''
    pass

def p_print_statement(p):
    '''print_statement : PRINT LPAREN print_args RPAREN SEMI'''
    pass

def p_print_args(p):
    '''print_args : STRING COMMA IDENTIFIER
                  | STRING
                  | IDENTIFIER
                  | empty'''
    pass

def p_input_statement(p):
    '''input_statement : IDENTIFIER ASSIGN INPUT LPAREN TYPE RPAREN SEMI'''
    pass

def p_if_statement(p):
    '''if_statement : IF condition THEN statements else_part ENDIF'''
    pass

def p_else_part(p):
    '''else_part : ELSE statements
                 | empty'''
    pass

def p_condition(p):
    '''condition : IDENTIFIER GREATER NUMBER'''
    pass

def p_for_loop(p):
    '''for_loop : FOR IDENTIFIER ASSIGN NUMBER TO NUMBER STEP NUMBER statements ENDFOR'''
    pass

def p_empty(p):
    '''empty : '''
    pass

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}', line {p.lineno}")
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()

def read_file(file_path):
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist. Please create the file and try again.")
        return None
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except IOError as e:
        print(f"Error reading file '{file_path}': {e}")
        return None

def read_tokens(file_path):
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist. Please create the file and try again.")
        return None
    try:
        with open(file_path, 'r') as file:
            return file.readlines()
    except IOError as e:
        print(f"Error reading file '{file_path}': {e}")
        return None

token_file = 'resultat_lexer.txt'
tokens_string = read_tokens(token_file)

if tokens_string is not None:
    tokens_list = [token.strip().split(' ', 1) for token in tokens_string]

    class Token:
        def __init__(self, type, value):
            self.type = type
            self.value = value

        def __repr__(self):
            return f"LexToken({self.type}, {self.value})"

    def generate_tokens(tokens_list):
        for token_type, token_value in tokens_list:
            if token_type == 'NUMBER':
                token_value = int(token_value) if '.' not in token_value else float(token_value)
            elif token_type == 'BOOLEAN':
                token_value = token_value.lower() == 'vrai'
            yield Token(token_type, token_value)

    # Create a generator for the tokens
    tokens_gen = generate_tokens(tokens_list)

    def token_func():
        try:
            return next(tokens_gen)
        except StopIteration:
            return None

    class MyLexer:
        def token(self):
            return token_func()

    my_lexer = MyLexer()

    result = parser.parse(lexer=my_lexer)

    if result:
        print("Parsing completed successfully.")
    else:
        print("Parsing failed due to syntax errors.")
else:
    print("Failed to read the token file.")
