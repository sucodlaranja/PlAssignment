import ply.lex as lex

literals = ['(', ')', ',', '[', ']', ':', '{', '}', '.']
tokens = ['LEXINIT', 'YACCINIT', 'RETURN', 'ERROR', 'OPERATOR', 'CODELINE', 'OPENCODELINE', 'OPENCODE', 'MCODE',
          'CLOSECODE', 'COMENTARY', 'str', 'id', 'int']
states = [("MULTILINECODE", "exclusive"),
          ("LINECODE", "exclusive")]


def t_LEXINIT(t):
    r"""%%[ ]*LEX[ ]*"""
    return t


def t_YACCINIT(t):
    r"""%%[ ]*YACC[ ]*"""
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
    r"""%\*"""
    t.lexer.begin('MULTILINECODE')
    return t


def t_MULTILINECODE_CLOSECODE(t):
    r"""\*%"""
    t.lexer.begin('INITIAL')
    return t


def t_MULTILINECODE_MCODE(t):
    r"""\n*(.+\n*)+?"""
    return t


def t_OPENCODELINE(t):
    r"""%"""
    t.lexer.begin('LINECODE')
    return t


def t_LINECODE_CODELINE(t):
    r"""[^\n]*\n"""
    t.lexer.begin('INITIAL')
    return t


def t_str(t):
    r"""
    [fr]?
    (\'.*?[^\\]\'|
    \"\"\".*?[^\\]\"\"\"|
    \".*?[^\\]\"|
    ´.*?[^\\]´|
    ’.*?[^\\]’)
    """
    return t


def t_id(t):
    r"""[a-zA-Z_]\w*"""
    return t


def t_int(t):
    r"""\d+(\.\d+)?"""
    return t


t_ignore = " \t\n"
t_MULTILINECODE_ignore = ""
t_LINECODE_ignore = ""


def t_error(t):
    print(f"ERROR: Illegal char '{t.value[0]}' at position IDK")
    t.lexer.skip(1)


def t_MULTILINECODE_error(t):
    print(f"ERROR: Illegal char '{t.value[0]}' at position multiline")
    t.lexer.skip(1)


def t_LINECODE_error(t):
    print(f"ERROR: Illegal char '{t.value[0]}' at position multiline")
    t.lexer.skip(1)


lexer = lex.lex()