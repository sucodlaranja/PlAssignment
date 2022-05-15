import ply.lex as lex
import sys

tokens = ['NUM','MAI','MEN','MUL','DIV']

t_ignore = ""

def t_NUM(t):
    r'\d+'
    return t


def t_MAI(t):
    r'\+'
    return t


def t_MEN(t):
    r'\-'
    return t


def t_MUL(t):
    r'\*'
    return t


def t_DIV(t):
    r'/'
    return t


def t_error(t):
    print(f'Caráter ilegal: t.value[0]')
    t.lexer.skip(1)

lexer = lex.lex()


