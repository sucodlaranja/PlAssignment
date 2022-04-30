import ply.yacc as yacc
from projeV2_lex import tokens, literals


def p_PlySimple(p):
    """PlySimple : LexGroup YaccGroup"""


def p_LexGroup(p):
    """LexGroup : LEXINIT LexInput"""


def p_LexInput_List(p):
    """LexInput : LexInput LexLine"""


def p_LexInput_Single(p):
    """LexInput : LexLine"""


def p_LexLine_Code(p):
    """LexLine : Code"""


def p_LexLine_Return(p):
    """LexLine : EXP RETURN '(' '’' ID '’' ',' EXP ')' NEWLINE"""


def p_LexLine_Error(p):
    """LexLine : '.' ERROR '(' PRINTSTRING ',' EXP ')' NEWLINE"""


def p_LexLine_Newline(p):
    """LexLine : NEWLINE"""


def p_Code_CODEUNILINE(p):
    """Code : CODEUNILINE"""


def p_Code_CODEBLOCK(p):
    """Code : CODEBLOCK"""


def p_YaccGroup(p):
    """YaccGroup : YACCINIT YaccInput"""


def p_YaccInput_List(p):
    """YaccInput : YaccInput YaccLine"""


def p_YaccInput_Single(p):
    """YaccInput : YaccLine"""


def p_YaccLine_Code(p):
    """YaccLine : Code"""


def p_YaccLine_Exp(p):
    """YaccLine : ID ':' EXP '{' EXP '}'"""


def p_YaccLine_Newline(p):
    """YaccLine : NEWLINE"""


def p_error(p):
    print('Erro sintático: ', p)
    parser.success = False


# Build the parser
parser = yacc.yacc()

# Read line from input and parse it

f = open("teste1.txt", "r")

parser.success = True
program = f.read()
parser.parse(program)

if parser.success:
    print("Programa bem estruturado")
else:
    print("Programa inválido ... Corrija e tente novamente!")
