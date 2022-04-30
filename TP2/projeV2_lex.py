import ply.lex as lex

literals = ['(', ')', ',', '[', ']', ':', '{', '}', '.']
tokens = ['LEXINIT', 'YACCINIT', 'RETURN', 'ERROR', 'OPERATOR', 'CODELINE', 'str', 'id', 'int']


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


def t_OPERATOR(t):
    r"""[=\+\*\-/]"""
    return t


def t_CODELINE(t):
    r"""%[^\n]*?\n"""
    return t


def t_str(t):
    r"""[fr]?[\'\"´’].*?[\'\"´’]"""
    return t


def t_id(t):
    r"""[a-zA-Z_]\w*"""
    return t


def t_int(t):
    r"""\d+(\.\d+)?"""
    return t


t_ignore = " \t\n"


def t_error(t):
    print(f"ERROR: Illegal char '{t.value[0]}' at position IDK")
    t.lexer.skip(1)


lexer = lex.lex()
