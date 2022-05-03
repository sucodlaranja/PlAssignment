import ply.yacc as yacc
from projeV2_lex import tokens, literals


def p_PlySimple(p):
    """PlySimple : Filename LexGroup YaccGroup"""
    if p[1] != "":
        parser.name = p[1]
    parser.lex = "import ply.lex as lex\n\n" + p[2] + "\n\nlexer = lex.lex()"
    parser.sin = "import ply.yacc as yacc\n" \
                 "from " + parser.name + "_lex import tokens, literals\n\n"\
                 + p[3]


def p_Filename_Name(p):
    """Filename : str"""
    p[0] = p[1]


def p_Filename_Empty(p):
    """Filename : """
    p[0] = ""


def p_LexGroup(p):
    """LexGroup : LEXINIT LexInput"""
    p[0] = p[2]


def p_LexInput_List(p):
    """LexInput : LexInput LexLine"""
    p[0] = p[1] + p[2]


def p_LexInput_Single(p):
    """LexInput : LexLine"""
    p[0] = p[1]


def p_LexLine_Codeline(p):
    """LexLine : Codeline"""
    p[0] = p[1]


def p_LexLine_MultiCode(p):
    """LexLine : MultiCode"""
    p[0] = p[1]


def p_LexLine_MultiComment(p):
    """LexLine : MultiComment"""
    p[0] = p[1]


def p_LexLine_Return(p):
    """LexLine : str RETURN '(' str ',' Code ')'"""
    p[0] = "\n\ndef t_" + p[4][1:-1] + "(t):\n" \
           + "    r" + p[1] + "\n" \
           + "    return " + p[6] + "\n"


def p_LexLine_Error(p):
    """LexLine : ERROR '(' str ',' Code ')'"""
    p[0] = "\n\ndef t_error(t):\n" \
           + "    print(" + p[3] + ")\n" \
           + "    " + p[5] + "\n"


def p_LexLine_Comentary(p):
    """LexLine : COMENTARY"""
    p[0] = p[1]


def p_YaccGroup(p):
    """YaccGroup : YACCINIT YaccInput"""
    p[0] = p[2]


def p_YaccInput_List(p):
    """YaccInput : YaccInput YaccLine"""
    p[0] = p[1] + p[2]


def p_YaccInput_Single(p):
    """YaccInput : YaccLine"""
    p[0] = p[1]


def p_YaccLine_Codeline(p):
    """YaccLine : Codeline"""
    p[0] = p[1]


def p_YaccLine_MultiCode(p):
    """YaccLine : MultiCode"""
    p[0] = p[1]
    
def p_YaccLine__MultiComment(p):
    """YaccLine : MultiComment"""
    p[0] = p[1]


def p_YaccLine_Exp(p):
    """YaccLine : id ':' Grammar '{' Code '}'"""
    p[0] = "\n\ndef p_" + p[1] + "_" + str(parser.cc) + "(p):\n" \
           + "    \"" + p[1] + " :" + p[3] + "\"\n" \
           + "    " + p[5] + "\n"
    parser.cc += 1


def p_YaccLine_Comentary(p):
    """YaccLine : COMENTARY"""
    p[0] = p[1]


def p_Grammar_List(p):
    """Grammar : Grammar Elem"""
    p[0] = p[1] + " " + p[2]


def p_Grammar_Empty(p):
    """Grammar : """
    p[0] = ""


def p_Elem_id(p):
    """Elem : id"""
    p[0] = p[1]


def p_Elem_str(p):
    """Elem : str"""
    p[0] = p[1]


def p_MultiCode(p):
    """MultiCode : OPENCODE MCode CLOSECODE"""
    p[0] = p[2]


def p_Codeline(p):
    """Codeline : OPENCODELINE CODELINE"""
    p[0] = p[2]


def p_MCode(p):
    """MCode : MCode CodeOrComment """
    p[0] = p[1] + p[2]
    
    
def p_CodeOrComment_Comment(p):
    """CodeOrComment : MultiComment"""
    p[0] = p[1]

def p_CodeOrComment_Code(p):
    """CodeOrComment : MCODE"""
    p[0] = p[1]
    
    
def p_MCode_empty(p):
    """MCode : """
    p[0] = ""
    
    
def p_MultiComment(p):
    """MultiComment : OPENCOMMENT MComment CLOSECOMMENT"""
    p[0] = p[2]


def p_MComment(p):
    """MComment : MComment MCOMMENT"""
    p[0] =  p[1] + "#" + p[2]

def p_MComment_empty(p):
    """MComment : """
    p[0] = ""


def p_Code_exp(p):
    """Code : Exp """
    p[0] = p[1]


def p_Code_Point(p):
    """Code : Code '.' Exp"""
    p[0] = p[1] + p[2] + p[3]


def p_Code_Operator(p):
    """Code : Code OPERATOR Exp"""
    p[0] = p[1] + p[2] + p[3]


def p_Exp_Function(p):
    """Exp : id '(' Code ')'"""
    p[0] = p[1] + p[2] + p[3] + p[4]


def p_Exp_List(p):
    """Exp : id '[' Code ']'"""
    p[0] = p[1] + p[2] + p[3] + p[4]


def p_Exp_id(p):
    """Exp : id"""
    p[0] = p[1]


def p_Exp_int(p):
    """Exp : int"""
    p[0] = p[1]


def p_error(p):
    print('Erro sintático: ', p)
    parser.success = False


# Build the parser
parser = yacc.yacc()

# Read line from input and parse it

f = open("teste2.txt", "r", encoding="utf-8")

parser.success = True
parser.name = "no_name"
parser.lex = ""
parser.sin = ""
parser.cc = 0
program = f.read()
parser.parse(program)

if parser.success:

    lex_file = open(parser.name + "_lex.py", "w")
    lex_file.write(parser.lex)

    sin_file = open(parser.name + "_sin.py", "w")
    sin_file.write(parser.sin)

else:
    print("Programa inválido ... Corrija e tente novamente!")
