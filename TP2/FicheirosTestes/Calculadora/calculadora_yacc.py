import ply.yacc as yacc
import sys
from calculadora_lex import tokens
precedence = (('left','MAI','MEN'),('left','DIV','MUL'),)

def p_Frase(p):
    "Frase : Elementos"
    print(p[1])
#Parte das operações


def p_Elementos_mais(p):
    "Elementos : Elementos MAI Elementos"
    p[0] = float(p[1]) + float(p[3])


def p_Elementos_menos(p):
    "Elementos : Elementos MEN Elementos"
    p[0] = float(p[1]) - float(p[3])


def p_Elementos_vezes(p):
    "Elementos : Elementos MUL Elementos"
    p[0] = float(p[1]) * float(p[3])


def p_Elementos_div(p):
    "Elementos : Elementos DIV Elementos"
    p[0] = float(p[1]) / float(p[3])
#Expressoes


def p_Elementos_expressao(p):
    "Elementos : Expressao"
    p[0] = p[1]


def p_Expressao(p):
    "Expressao : NUM"
    p[0] = p[1]


def p_error(p):
    print(f'Erro sintatico: {p}')
    parser.sucess = False

parser = yacc.yacc()


for line in sys.stdin:
    parser.success = True
    parser.parse(line)
    if parser.success:
        print("Valid sentence!")
    else:
        print("Invalid sentence... Redo and try again")

