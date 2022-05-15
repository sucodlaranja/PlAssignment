import ply.lex as lex
import sys

tokens = ["ON","OFF","NUM","PRINT"]

t_ignore = " \n\t"


def t_ON(t):
    r'[oO][nN]'
    lexer.on_off = True


def t_OFF(t):
    r'[oO][fF][fF]'
    lexer.on_off = False


def t_PRINT(t):
    r'='
    print(f'soma {lexer.sum}')

def t_NUM(t):
    r'(\d+)'
    if lexer.on_off:
        lexer.sum += int(t.value)


def t_error(t):
    print(f"ERROR: Illegal char '{t.value[0]}' at position IDK")
    t.lexer.skip(1)

lexer = lex.lex()

lexer.sum = 0
lexer.on_off = True


for line in sys.stdin:
    lexer.input(line)
    for tok in lexer:
        print(tok)


