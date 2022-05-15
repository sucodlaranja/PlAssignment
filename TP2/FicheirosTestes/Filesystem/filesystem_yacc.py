import ply.yacc as yacc
import sys
from filesystem_lex import tokens
# Input : PL { doc {} , aulas { 06-04 { f1,f2,f3} } }
# Output : mkdir PL; mkdir doc; mkdir aulas; mkdir 06-04;touch aulas/f1;touch aulas/f2;touch aulas/f3 
# 


def p_Frase(p):
    "Frase : Path"
    print(p[1])


def p_Path(p):
    "Path : Filesystem"
    p[0] = p[1]


def p_Path_2(p):
    "Path : Filesystem VIR Path"
    p[0] = p[1] + p[3]


def p_Filesystem(p):
    "Filesystem : NAME AP Path FP"
    p[0] = "mkdir " + p[1] + "; " + "cd " + p[1] + "/; " + p[3] + " cd ..; "


def p_Filesystem_File(p):
    "Filesystem : NAME"
    p[0] = "touch " + p[1] + "; "


def p_Path_none(p):
    "Path :"
    p[0] = ""


def p_error(p):
    print(f'Erro sintático {p}')
    parser.sucess = False

parser = yacc.yacc()


for line in sys.stdin:
    parser.success = True
    parser.parse(line)
    if parser.success:
        print("Valid sentence!")
    else:
        print("Invalid sentence... Redo and try again")

