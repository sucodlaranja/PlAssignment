import ply.lex as lex

states = [("MULTILINECODE", "exclusive"),
          ("LINECODE", "exclusive"),
          ("MULTICOMMENT", "exclusive")]

literals = ['(', ')', ',', '[', ']', ':', '{', '}', '.', '=']

tokens = ['MAKE', 'MAKE_MAIN', 'LITERALS', 'IGNORE', 'TOKENS', 'LEXINIT', 'YACCINIT', 'RETURN', 'ERROR', 'OPERATOR',
          'CODELINE', 'OPENCODELINE', 'OPENCODE', 'TEXT', 'CLOSECODE', 'OPENCOMMENT', 'MCOMMENT', 'CLOSECOMMENT',
          'PRECEDENCE', 'STATES', 'COMENTARY', 'str', 'id', 'num']


def t_MAKE_MAIN(t):
    r"""make[ ]*main[ ]*"""
    return t


def t_MAKE(t):
    r"""make"""
    return t


def t_LITERALS(t):
    r"""literals"""
    return t


def t_IGNORE(t):
    r"""ignore(_[a-zA-Z_]\w*)?"""
    return t


def t_STATES(t):
    r"""states"""
    return t


def t_PRECEDENCE(t):
    r"""precedence"""
    return t


def t_TOKENS(t):
    r"""tokens"""
    return t


def t_LEXINIT(t):
    r"""%%[ ]*LEX"""
    return t


def t_YACCINIT(t):
    r"""%%[ ]*YACC"""
    return t


def t_RETURN(t):
    r"""return"""
    return t


def t_ERROR(t):
    r"""error"""
    return t


def t_OPERATOR(t):
    r"""([\+\*\-/]=|[><]=|[\+\*\-/<>])"""
    return t


def t_OPENCODE(t):
    r"""%\*"""
    t.lexer.begin('MULTILINECODE')
    return t


def t_MULTILINECODE_CLOSECODE(t):
    r"""\*%"""
    t.lexer.begin('INITIAL')
    return t


def t_MULTILINECODE_OPENCOMMENT(t):
    r"""\#\*"""
    lexer.laststate = 'MULTILINECODE'
    t.lexer.begin('MULTICOMMENT')
    return t


def t_MULTILINECODE_TEXT(t):
    r"""([^\#\%](\*)+[^\#\%]|[^\*](\#)+[^\*]|[^\*](\%)+[^\*]|
    ^[\#\%][^\*]|[^\*][\#\%]$|^[\*][^\#\%]|[^\#\%](\*)$|
    [^\*\%\#])+"""
    return t


def t_OPENCODELINE(t):
    r"""%"""
    t.lexer.begin('LINECODE')
    return t


def t_LINECODE_CODELINE(t):
    r"""[^\n]*\n+|.+$"""
    t.lexer.begin('INITIAL')
    return t


def t_OPENCOMMENT(t):
    r"""\#\*"""
    t.lexer.begin('MULTICOMMENT')
    return t


def t_MULTICOMMENT_CLOSECOMMENT(t):
    r"""\*\#"""
    t.lexer.begin(lexer.laststate)
    lexer.laststate = 'INITIAL'
    return t


def t_MULTICOMMENT_MCOMMENT(t):
    r"""(\*[^\#]|\*$|^\#|[^\*]\#|[^\*\#])+"""
    return t


def t_COMENTARY(t):
    r"""\#([^\n]*\n+|.+$)"""
    return t


def t_str(t):
    r"""
    [fr]?
    (\"\"|\"\"\"\"\"\"|``|\'\'|??????|\'.*?[^\\]\'|
    \"\"\".*?[^\\]\"\"\"|
    \".*?[^\\]\"|
    ??.*?[^\\]??|
    ???.*?[^\\]???)
    """
    return t


def t_id(t):
    r"""[a-zA-Z_]\w*"""
    return t


def t_num(t):
    r"""\d+(\.\d+)?"""
    return t


t_ignore = " \t\n"
t_MULTILINECODE_ignore = ""
t_LINECODE_ignore = ""
t_MULTICOMMENT_ignore = "\n"


def t_error(t):
    print(f"ERROR: Illegal char '{t.value[0]}' at position IDK")
    t.lexer.skip(1)


def t_MULTILINECODE_error(t):
    print(f"ERROR: Illegal char '{t.value[0]}' at position multiline")
    t.lexer.skip(1)


def t_LINECODE_error(t):
    print(f"ERROR: Illegal char '{t.value[0]}' at position linecode")
    t.lexer.skip(1)


def t_MULTICOMMENT_error(t):
    print(f"ERROR: Illegal char '{t.value[0]}' at position multicomment")
    t.lexer.skip(1)


lexer = lex.lex()
lexer.laststate = "INITIAL"
