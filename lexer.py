import ply.lex as lex
import os

tokens = (
    'IDENTIFIER',
    'NUMBER',
    'STRING',
    'TYPE',
    'ASSIGN',
    'SEMI',
    'COMMA',
    'LPAREN',
    'RPAREN',
    'GREATER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'IF',
    'ELSE',
    'ENDIF',
    'FOR',
    'TO',
    'STEP',
    'ENDFOR',
    'PRINT',
    'INPUT',
    'BOOLEAN',
    'THEN',
)

reserved = {
    'entier': 'TYPE',
    'reel': 'TYPE',
    'booleen': 'TYPE',
    'caractere': 'TYPE',
    'chaineCaracteres': 'TYPE',
    'si': 'IF',
    'sinon': 'ELSE',
    'finSi': 'ENDIF',
    'pour': 'FOR',
    'jsq': 'TO',
    'pas': 'STEP',
    'finPour': 'ENDFOR',
    'afficher': 'PRINT',
    'saisir': 'INPUT',
    'vrai': 'BOOLEAN',
    'faux': 'BOOLEAN',
    'alors': 'THEN',
}

def t_IDENTIFIER(t):
    r'[a-z][A-Z0-9]+'
    t.type = reserved.get(t.value, 'IDENTIFIER')  # Check for reserved words
    return t

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

def t_STRING(t):
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ASSIGN = r'='
t_SEMI = r';'
t_COMMA = r','
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_GREATER = r'>'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

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

def write_tokens(file_path, tokens):
    try:
        with open(file_path, 'w') as file:
            for token in tokens:
                file.write(f"{token.type} {token.value}\n")
    except IOError as e:
        print(f"Error writing to file '{file_path}': {e}")

input_file = 'preprocessed_code.txt'
output_file = 'resultat_lexer.txt'

source_code = read_file(input_file)

if source_code is not None:
    lexer.input(source_code)
    tokens = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append(tok)

    write_tokens(output_file, tokens)
    print(f"Lexing is complete. The tokens are written to '{output_file}'.")
else:
    print("Failed to read the preprocessed code.")