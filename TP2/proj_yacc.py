import ply.yacc as yacc
import sys
from proj_lex import tokens
from proj_lex import literals


def p_Calc(p):
     'Calc : Comandos FIM'


def p_Comandos_List(p):
     'Comandos : Comandos Comando'

def p_Comandos_Simples(p):
    'Comandos : Comando'

def p_Comando_Atrib(p):
     "Comando : id '=' Exp"
     p.parser.registos[p[1]] = p[3]

def p_Comando_Escrita(p):
    "Comando : '!' Exp"
    print(p[2])

def p_Comando_Leitura(p):
    "Comando : '?' Exp"
    valor = input("Introduza uma valor inteiro: ")
    p.parser.registos[p[2]] = int(valor)

def p_Comando_dump(p):
    "Comando : DUMP"
    print(p.parser.registos)


def p_Exp_ad(p):
    "Exp : Exp '+' Termo"
    p[0] = p[1] + p[3]

def p_Exp_sub(p):
    "Exp : Exp '-' Termo"
    p[0] = p[1] - p[3]

def p_Exp_termo(p):
    "Exp : Termo"
    p[0] = p[1]

def p_Termo_mult(p):
    "Termo : Termo '*' Fator"
    p[0] = p[1] * p[3]

def p_Termo_sub(p):
    "Termo : Termo '/' Fator"
    if p[3] != 0:
        p[0] = p[1] / p[3]
    else:
        print("Erro divisão por 0!!!!!!!!")

def p_Termo_fator(p):
    "Termo : Fator"
    p[0] = p[1]

def p_Fator_num(p):
    "Fator : num"
    p[0] = p[1]

def p_Fator_grupo(p):
    "Fator : '(' Exp ')'"
    p[0] = p[2]

def p_Fator_id(p):
    "Fator : id"
    p[0] = p.parser.registos[p[1]]


def p_error(p):
    print(f"ERROR: Illegal char ", p, " at position IDK")
    parser.success = False


parser = yacc.yacc()
parser.registos = {}

for line in sys.stdin:
    parser.success = True
    parser.parse(line)
    if parser.success:
        print('Valid', line)
    else:
        print('Invalid')