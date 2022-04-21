import ply.lex as lex

literals = ['"', '#', '%', '(', '’', ')', ':', '{', '}']
tokens = ['ID', 'OPENCODE', 'CLOSECODE', 'OPENPLY', 'RETURN', 'ERROR', 'NLINE']

t_ID = r'.'
t_OPENCODE = r'%\*'
t_CLOSECODE = r'\*%'
t_OPENPLY = r'%% \w+'
t_RETURN = r'return'
t_ERROR = r'error'
t_NLINE = r'\n'


t_ignore = " \t\n"


def t_error(t):
    print(f"ERROR: Illegal char '{t.value[0]}' at position IDK")
    t.lexer.skip(1)


lexer = lex.lex()
