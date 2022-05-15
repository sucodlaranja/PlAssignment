import ply.yacc as yacc
import sys
from testePlySimple_lex import tokens, literals


def p_PlySimple(p):
    "PlySimple : Filename LexGroup YaccGroup"
    parser.filename = p[1]
    lex_content["Code"] = p[2]
    lex_content["Code"] = p[3]
# Filename -> str
#            | 


def p_Filename_Name(p):
    "Filename : str"
    p[0] = p[1]


def p_Filename_Empty(p):
    "Filename : str"
    p[0] = p[1]
#  LexGroup -> LEXINIT LexInput
#              | LEXINIT
#              | 


def p_LexGroup_Input(p):
    "LexGroup : LEXINIT LexInput"
    p[0] = p[2]


def p_LexGroup_Just_Init(p):
    "LexGroup : LEXINIT"
    lex_content["empty"] = True
    p[0] = ""


def p_LexGroup_Empty(p):
    "LexGroup :"
    lex_content["empty"] = True
    p[0] = ""
#  LexInput -> LexInput LexLine
#               | LexLine 


def p_LexInput_List(p):
    "LexInput : LexInput LexLine"
    p[0] = p[1] + p[2]


def p_LexInput_Single(p):
    "LexInput : LexLine"
    p[0] = p[1]
#  LexLine -> PythonCode
#           | MAKE
#           | MAKE_MAIN
#           | str RETURN '(' id ',' ReturnArgs ')'
#           | ERROR '(' ErrorArgs ')'
#           | id ERROR '(' ErrorArgs ')'
#           | LITERALS '=' str
#           | IGNORE '=' str
#           | TOKENS '=' Code
#           | PRECEDENCE '=' Code
#           | STATES '=' '[' StatesArgs ']' 


def p_LexLine_PythonCode(p):
    "LexLine : PythonCode"
    p[0] = p[1]


def p_LexLine_MAKE(p):
    "LexLine : MAKE"
    p[0] = "\nlexer = lex.lex()\n\n"


def p_LexLine_MAKE_MAIN(p):
    "LexLine : MAKE_MAIN"
    "\n" + "for line in sys.stdin:\n" + "    lexer.input(line)\n" + "    for tok in lexer:\n" + "        print(tok)\n\n"


def p_LexLine_Return(p):
    "LexLine : str RETURN '(' id ',' ReturnArgs ')'"
    p[0] = "\n\ndef t_" + p[4] + "(t):\n" + "    r" + p[1] + "\n" + p[6]


def p_LexLine_Error(p):
    "LexLine : ERROR '(' ErrorArgs ')'"
    p[0] = "\n\ndef t_error(t):\n" + p[3]


def p_LexLine_Error_State(p):
    "LexLine : id ERROR '(' ErrorArgs ')'"
    p[0] = "\n\ndef t_error_" + p[1] + "(t):\n" + p[4]


def p_LexLine_Literals(p):
    "LexLine : LITERALS '=' Code"
    lex_content["Literals"] = p[3]
    p[0] = ""
#  Como este elemento é complexo 
# optamos por defini-lo como codigo python normal

def p_LexLine_Ignore(p):
    """LexLine : IGNORE '=' str"""
    p[0] = ""
    ign = p[1].split("_", 1)
    if len(ign) > 1:
        if "IgnoreStates" not in lex_content.keys():
            lex_content["IgnoreStates"] = {}
        lex_content["IgnoreStates"][ign[1]] = p[3]
    else:
        lex_content["Ignore"] = p[3]


def p_LexLine_Tokens(p):
    "LexLine : TOKENS '=' Code"
    lex_content["Tokens"] = p[3]
    p[0] = ""


def p_LexLine_Precedence(p):
    "LexLine : PRECEDENCE '=' Code"
    lex_content["Precedence"] = p[3]
    p[0] = ""


def p_LexLine_States(p):
    "LexLine : STATES '=' '[' StatesArgs ']'"
    p[0] = ""
#  StateArgs -> '(' str ',' str ')' ',' StatesArgs
#              | '(' str ',' str ')'
#              | 

def p_StatesArgs_List(p):
    """StatesArgs : '(' str ',' str ')' ',' StatesArgs"""
    if "States" not in lex_content.keys():
        lex_content["States"] = {}
    lex_content["States"][p[2]] = p[4]
    p[0] = ""


def p_StatesArgs_State(p):
    """StatesArgs : '(' str ',' str ')'"""
    if "States" not in lex_content.keys():
        lex_content["States"] = {}
    lex_content["States"][p[2]] = p[4]
    p[0] = ""


def p_StatesArgs_Empty(p):
    "StatesArgs :"
    p[0] = ""
#  ReturnArgs -> OtherComands ',' Code
#               | OtherComands ','
#               | Code
#               | 


def p_ReturnArgs_Return(p):
    "ReturnArgs : OtherComands ',' Code"
    p[0] = p[1] + "    return " + p[3] + "\n"


def p_ReturnArgs_No_Return(p):
    "ReturnArgs : OtherComands ','"
    p[0] = p[1]


def p_ReturnArgs_Only_Return(p):
    "ReturnArgs : Code"
    p[0] = "    return " + p[1] + "\n"


def p_ReturnArgs_Empty(p):
    "ReturnArgs :"
    p[0] = ""
#  ErrorArgs -> str ',' OtherComands
#              | ',' OtherComands
#              | str
#              | 


def p_ErrorArgs_Print(p):
    "ErrorArgs : str ',' OtherComands"
    p[0] = "    print(" + p[1] + ")\n" + p[3]


def p_ErrorArgs_No_Print(p):
    "ErrorArgs : ',' OtherComands"
    p[0] = p[2]


def p_ErrorArgs_Only_Print(p):
    "ErrorArgs : str"
    p[0] = "    print(" + p[1] + ")\n"


def p_ErrorArgs_empty(p):
    "ErrorArgs :"
    p[0] = ""
# OtherComands -> Code ',' OtherComands
#              | Code


def p_OtherComands_List(p):
    "OtherComands : OtherComands ',' Code"
    p[0] = p[1] + "    " + p[3] + "\n"


def p_OtherComands_Code(p):
    "OtherComands : Code"
    p[0] = "    " + p[1] + "\n"
#  YaccGroup -> YACCINIT YaccInput
#              | YACCINIT
#              | 


def p_YaccGroup_Input(p):
    "YaccGroup : YACCINIT YaccInput"
    p[0] = p[2]


def p_YaccGroup_Just_Init(p):
    "YaccGroup : YACCINIT"
    yacc_content["empty"] = True
    p[0] = ""
