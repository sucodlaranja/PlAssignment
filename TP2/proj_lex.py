import ply.lex as lex

literals = ['"', '#', '\n', '%', '(', '’', ')', ':', '{', '}']
tokens = ['ID', 'OPENCODE', 'CLOSECODE', 'OPENPLY', 'RETURN', 'ERROR']

t_ID = r'.'
t_OPENCODE = r'%*'
t_CLOSECODE = r'*%'
t_OPENPLY = r'*%'


def t_num(t):
    r'\d+'
    t.value = int(t.value)
    return t


t_ignore = " \t\n"


def t_error(t):
    print(f"ERROR: Illegal char '{t.value[0]}' at position IDK")
    t.lexer.skip(1)


lexer = lex.lex()