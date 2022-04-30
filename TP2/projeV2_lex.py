import ply.lex as lex

literals = ['(', '’', ')', ',', '.', ':', '{', '}']
tokens = ['LEXINIT', 'YACCINIT', 'CODEUNILINE','CODEBLOCK', 'ID','RETURN', 'ERROR'
    , 'PRINTSTRING', 'STRING', 'NEWLINE', 'freespech']


def t_LEXINIT(t):
    r"""%%[ ]*LEX[ ]*\n"""
    return t


def t_YACCINIT(t):
    r"""%%[ ]*YACC[ ]*\n"""
    return t


def t_RETURN(t):
    r"""return"""
    return t


def t_ERROR(t):
    r"""error"""
    return t


def t_CODEBLOCK(t):
    r"""%\*.+\*%"""
    return t


def t_CODEUNILINE(t):
    r"""%[^\n]*?\n"""
    return t


def t_ID(t):
    r"""[a-zA-Z_]\w*"""
    return t


def t_STRING(t):
    r"""[fr]?[\'\"].*[\'\"]"""
    return t


def t_freespech(t):
    r"""[^\n]+"""
    return t


def t_NEWLINE(t):
    r"""\n"""
    return t


t_ignore = " \t"


def t_error(t):
    print(f"ERROR: Illegal char '{t.value[0]}' at position IDK")
    t.lexer.skip(1)


lexer = lex.lex()

f = open("teste1.txt", "r")

program = f.read()
lexer.input(program)

for tok in lexer:
    print(tok)
