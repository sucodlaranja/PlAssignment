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


def p_LexLine_Codeline(p):
    """LexLine : CODELINE"""
   

def p_LexLine_MultiCode(p):
    """LexLine : MultiCode"""
    
    
def p_LexLine_Return(p):
    """LexLine : str RETURN '(' str ',' Code ')'"""
    


def p_LexLine_Error(p):
    """LexLine : ERROR '(' str ',' Code ')'"""
    print(p[3])


def p_YaccGroup(p):
    """YaccGroup : YACCINIT YaccInput"""


def p_YaccInput_List(p):
    """YaccInput : YaccInput YaccLine"""


def p_YaccInput_Single(p):
    """YaccInput : YaccLine"""


def p_YaccLine_Codeline(p):
    """YaccLine : CODELINE"""
    
    
def p_YaccLine_MultiCode(p):
    """YaccLine : MultiCode"""
    

def p_YaccLine_Exp(p):
    """YaccLine : id ':' Grammar '{' Code '}'"""


def p_Grammar_List(p):
    """Grammar : Grammar Elem"""


def p_Grammar_Empty(p):
    """Grammar : """


def p_Elem_id(p):
    """Elem : id"""


def p_Elem_str(p):
    """Elem : str"""
    
    
    
def p_MultiCode(p):
    """MultiCode : OPENCODE MCode CLOSECODE"""
    

def p_MCode(p):
    """MCode : MCode MCODE """
    
    
def p_MCode_empty(p):
    """MCode : """
    

def p_Code_exp(p):
    """Code : Exp """


def p_Code_Point(p):
    """Code : Code '.' Exp"""


def p_Code_Operator(p):
    """Code : Code OPERATOR Exp"""
 

def p_Exp_Function(p):
    """Exp : id '(' Code ')'"""


def p_Exp_List(p):
    """Exp : id '[' Code ']'"""


def p_Exp_id(p):
    """Exp : id"""


def p_Exp_int(p):
    """Exp : int"""


def p_error(p):
    print('Erro sintático: ', p)
    parser.success = False


# Build the parser
parser = yacc.yacc()

# Read line from input and parse it

f = open("teste2.txt", "r", encoding="utf-8")

parser.success = True
program = f.read()
parser.parse(program)

if parser.success:
    print("Programa bem estruturado")
else:
    print("Programa inválido ... Corrija e tente novamente!")
