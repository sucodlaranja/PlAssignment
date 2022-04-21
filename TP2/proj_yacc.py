import ply.yacc as yacc
import sys
from proj_lex import tokens, literals


def p_frase(p):
    """Frase : String 
       Frase : Comentario 
       Frase : CodeInLine 
       Frase : CodeIn 
       Frase : CodeOut 
       Frase : Ply 
       Frase : YACC 
       Frase : Lexer 
       Frase : Func 
    """


def p_String(p):
    "String :  Texto "


def p_Comentario(p):
    "Comentario : '#' Texto"
    print(p[2])


def p_CodeInLine(p):
    "CodeInLine : '%' Texto"


def p_CodeIn(p):
    "CodeIn : OPENCODE Texto"


def p_CodeOut(p):
    "CodeOut : Texto CLOSECODE"


def p_Texto_rec(p):
    "Texto : ID Texto"


def p_Texto_vazio(p):
    "Texto : "


def p_OpenPly(p):
    "Ply : OPENPLY ID"


def p_Lexer(p):
    "Lexer : Texto Func"


def p_Func_Return(p):
    "Func : RETURN '(' '’' Texto '’' ',' Texto ')'"


def p_Func_Error(p):
    "Func : ERROR '(' '’' Texto '’' ',' Texto ')'"


def p_Yacc(p):
    "YACC : Texto ':' Texto '{' Texto '}'"


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
