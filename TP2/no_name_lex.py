import ply.lex as lex

literals = "+-/*=()" ## a single char
ignore = " \t\n"
#Tokens 
#simples
tokens = [ 'VAR','NUMBER' ]


def t_VAR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t.value


def t_NUMBER(t):
    r'\d+(\.\d+)?'
    return float(t.value)


def t_error(t):
    print(f"Illegal character '{t.value[0]}', [{t.lexer.lineno}]")
    t.lexer.skip(1)


lexer = lex.lex()