import ply.lex as lex

literals = ['(', ')', ',', '[', ']', ':', '{', '}', '.']
tokens = ['LEXINIT', 'YACCINIT', 'RETURN', 'ERROR', 'OPERATOR', 'CODELINE', 'OPENCODE', 'MCODE','CLOSECODE', 'str', 'id', 'int']
states = [("MULTILINECODE","exclusive")]

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


def t_OPENCODE(t):
    r"""%\* \s*"""
    t.lexer.begin('MULTILINECODE')
    return t


def t_CODELINE(t):
    r"""%[^\n]*?\n"""
    return t

def t_MULTILINECODE_CLOSECODE(t):
    r"""\*%"""
    t.lexer.begin('INITIAL')
    return t

def t_MULTILINECODE_MCODE(t):
    r"""(.+\n*)+?"""
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
t_MULTILINECODE_ignore = ""


def t_error(t):
    print(f"ERROR: Illegal char '{t.value[0]}' at position IDK")
    t.lexer.skip(1)


def t_MULTILINECODE_error(t):
    print(f"ERROR: Illegal char '{t.value[0]}' at position multiline")
    t.lexer.skip(1)


lexer = lex.lex()
