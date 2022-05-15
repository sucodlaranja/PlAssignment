import ply.lex as lex
import sys

tokens = ['NAME','FP','AP','VIR']

t_ignore = " \t\n"


def t_VIR(t):
    r','
    return t


def t_AP(t):
    r'{'
    return t


def t_FP(t):
    r'}'
    return t


def t_NAME(t):
    r'\w+'
    return t


def t_error(t):
    print(f'Caráter ilegal {t.value[0]}')
    t.lexer.skip(1)

lexer = lex.lex()


