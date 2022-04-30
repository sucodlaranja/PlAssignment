import ply.lex as lex

literals = ['(', '’', ')', ',', '.', ':', '{', '}']
tokens = ['LEXINIT', 'YACCINIT', 'CODEUNILINE', 'OPENCODE', 'CLOSECODE','CODEBLOCK',
          'REGEXP', 'ID','RETURN', 'ERROR', 'PRINTSTRING', 'EXP', 'NEWLINE']


def t_LEXINIT(t):
    r"""%% *LEX *\n"""
    return t


def t_YACCINIT(t):
    r"""%% *YACC *\n"""
    return t


def t_OPENCODE(t):
    r"""%\*"""
    return t


def t_CLOSECODE(t):
    r"""\*%"""
    return t


def t_RETURN(t):
    r"""return"""
    return t


def t_ERROR(t):
    r"""error"""
    return t


def t_ID(t):
    r"""[a-zA-Z_]\w*"""
    return t


def t_PRINTSTRING(t):
    r"""[f|r]?\"[\"]+\""""
    return t


def t_CODEUNILINE(t):
    r""".+?\n"""
    return t


def t_CODEBLOCK(t):
    r"""[^\n]+?"""
    return t


def t_EXP(t):
    r"""[^\n]+?"""
    return t


def t_REGEXP(t):
    r"""[^\n]+?"""
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
