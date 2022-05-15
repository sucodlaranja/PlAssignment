import ply.yacc as yacc
from plySimple_Lex import tokens, literals


# PlySimple -> Filename LexGroup YaccGroup
def p_PlySimple(p):
    """PlySimple : Filename LexGroup YaccGroup"""
    parser.filename = p[1]
    lex_content["Code"] = p[2]
    yacc_content["Code"] = p[3]


# Filename -> str
#           |
def p_Filename_Name(p):
    """Filename : str"""
    p[0] = p[1]


def p_Filename_Empty(p):
    """Filename : """
    p[0] = ""


# LexGroup -> LEXINIT LexInput
#           | LEXINIT
#           |
def p_LexGroup_Input(p):
    """LexGroup : LEXINIT LexInput"""
    p[0] = p[2]


def p_LexGroup_Just_Init(p):
    """LexGroup : LEXINIT"""
    lex_content["empty"] = True
    p[0] = ""


def p_LexGroup_Empty(p):
    """LexGroup : """
    lex_content["empty"] = True
    p[0] = ""


# LexInput -> LexInput LexLine
#           | LexLine
def p_LexInput_List(p):
    """LexInput : LexInput LexLine"""
    p[0] = p[1] + p[2]


def p_LexInput_Single(p):
    """LexInput : LexLine"""
    p[0] = p[1]


# LexLine -> PythonCode
#          | MAKE
#          | MAKE_MAIN
#          | str RETURN '(' id ',' ReturnArgs ')'
#          | ERROR '(' ErrorArgs ')'
#          | id ERROR '(' ErrorArgs ')'
#          | LITERALS '=' str
#          | IGNORE '=' str
#          | TOKENS '=' Code
#          | PRECEDENCE '=' Code
#          | STATES '=' '[' StatesArgs ']'
def p_LexLine_PythonCode(p):
    """LexLine : PythonCode"""
    p[0] = p[1]


def p_LexLine_MAKE(p):
    """LexLine : MAKE"""
    p[0] = "\nlexer = lex.lex()\n\n"


def p_LexLine_MAKE_MAIN(p):
    """LexLine : MAKE_MAIN"""
    p[0] = "\n" \
           "for line in sys.stdin:\n" \
           "    lexer.input(line)\n" \
           "    for tok in lexer:\n" \
           "        print(tok)\n\n"


def p_LexLine_Return(p):
    """LexLine : str RETURN '(' id ',' ReturnArgs ')'"""
    p[0] = "\n\ndef t_" + p[4] + \
        "(t):\n" + "    r" + p[1] + "\n" + p[6]


def p_LexLine_Error(p):
    """LexLine : ERROR '(' ErrorArgs ')'"""
    p[0] = "\n\ndef t_error(t):\n" + p[3]


def p_LexLine_Error_State(p):
    """LexLine : id ERROR '(' ErrorArgs ')'"""
    p[0] = "\n\ndef t_" + p[1] + "_error(t):\n" + p[4]


def p_LexLine_Literals(p):
    """LexLine : LITERALS '=' Code"""
    p[0] = ""
    lex_content["Literals"] = p[3]


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
    """LexLine : TOKENS '=' Code"""
    p[0] = ""
    lex_content["Tokens"] = p[3]


def p_LexLine_Precedence(p):
    """LexLine : PRECEDENCE '=' Code"""
    p[0] = ""
    lex_content["Precedence"] = p[3]


def p_LexLine_States(p):
    """LexLine : STATES '=' '[' StatesArgs ']'"""
    p[0] = ""


# StateArgs -> '(' str ',' str ')' ',' StatesArgs
#            | '(' str ',' str ')'
#            |
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
    """StatesArgs : """
    p[0] = ""


# ReturnArgs -> OtherComands ',' Code
#             | OtherComands ','
#             | Code
#             |
def p_ReturnArgs_Return(p):
    """ReturnArgs : OtherComands ',' Code"""
    p[0] = p[1] + "    return " + p[3] + "\n"


def p_ReturnArgs_No_Return(p):
    """ReturnArgs : OtherComands ','"""
    p[0] = p[1]


def p_ReturnArgs_Only_Return(p):
    """ReturnArgs : Code"""
    p[0] = "    return " + p[1] + "\n"


def p_ReturnArgs_Empty(p):
    """ReturnArgs : """
    p[0] = ""


# ErrorArgs -> str ',' OtherComands
#            | ',' OtherComands
#            | str
#            |
def p_ErrorArgs_Print(p):
    """ErrorArgs : str ',' OtherComands"""
    p[0] = "    print(" + p[1] + ")\n" + p[3]


def p_ErrorArgs_No_Print(p):
    """ErrorArgs : ',' OtherComands"""
    p[0] = p[2]


def p_ErrorArgs_Only_Print(p):
    """ErrorArgs : str"""
    p[0] = "    print(" + p[1] + ")\n"


def p_ErrorArgs_empty(p):
    """ErrorArgs : """
    p[0] = ""


# OtherComands -> Code ',' OtherComands
#              | Code
def p_OtherComands_List(p):
    """OtherComands : OtherComands ',' Code"""
    p[0] = p[1] + "    " + p[3] + "\n"


def p_OtherComands_Code(p):
    """OtherComands : Code"""
    p[0] = "    " + p[1] + "\n"


# YaccGroup -> YACCINIT YaccInput
#            | YACCINIT
#            |
def p_YaccGroup_Input(p):
    """YaccGroup : YACCINIT YaccInput"""
    p[0] = p[2]


def p_YaccGroup_Just_Init(p):
    """YaccGroup : YACCINIT"""
    yacc_content["empty"] = True
    p[0] = ""


def p_YaccGroup_Empty(p):
    """YaccGroup : """
    yacc_content["empty"] = True
    p[0] = ""


# YaccInput -> YaccInput YaccLine
#           | YaccLine
def p_YaccInput_List(p):
    """YaccInput : YaccInput YaccLine"""
    p[0] = p[1] + p[2]


def p_YaccInput_Single(p):
    """YaccInput : YaccLine"""
    p[0] = p[1]


# YaccLine -> PythonCode
#           | MAKE
#           | MAKE_MAIN
#           | PRECEDENCE '=' Code
#           | id ':' Grammar '{' GrammarComands '}'
#           | id ':' Grammar '{' GrammarComands '}' id
#           |
def p_YaccLine_PythonCode(p):
    """YaccLine : PythonCode"""
    p[0] = p[1]


def p_YaccLine_MAKE(p):
    """YaccLine : MAKE"""
    p[0] = "\nparser = yacc.yacc()\n\n"


def p_YaccLine_MAKE_MAIN(p):
    """YaccLine : MAKE_MAIN"""
    p[0] = "\n" \
           "for line in sys.stdin:\n" \
           "    parser.success = True\n" \
           "    parser.parse(line)\n" \
           "    if parser.success:\n" \
           "        print(\"Valid sentence!\")\n" \
           "    else:\n" \
           "        print(\"Invalid sentence... Redo and try again\")\n\n"


def p_YaccLine_Precedence(p):
    """YaccLine : PRECEDENCE '=' Code"""
    p[0] = ""
    yacc_content["Precedence"] = p[3]


def p_YaccLine_Exp(p):
    """YaccLine : id ':' Grammar '{' GrammarComands '}'"""
    grammar_id = p[1]
    if grammar_id in parser.grammar_entries.keys():
        parser.grammar_entries[grammar_id] += 1
        cc = '_' + str(parser.grammar_entries[grammar_id])
    else:
        parser.grammar_entries[grammar_id] = 1
        cc = ""

    p[0] = "\n\ndef p_" + p[1] + cc + "(p):\n" \
           + "    \"" + p[1] + " :" + p[3] + "\"\n" \
           + p[5]


def p_YaccLine_Exp_Name(p):
    """YaccLine : id id ':' Grammar '{' GrammarComands '}'"""
    grammar_id = p[2] + "_" + p[1]
    if grammar_id in parser.grammar_entries.keys():
        parser.grammar_entries[grammar_id] += 1
        cc = grammar_id + '_' + str(parser.grammar_entries[grammar_id])
    else:
        parser.grammar_entries[grammar_id] = 1
        cc = grammar_id

    p[0] = "\n\ndef p_" + cc + "(p):\n" \
           + "    \"" + p[2] + " :" + p[4] + "\"\n" \
           + p[6]


def p_YaccLine_Error(p):
    """YaccLine : ERROR '(' ErrorArgs ')'"""
    p[0] = "\n\ndef p_error(p):\n" + p[3]


# GrammarComands -> Code ',' GrammarComands
#                 | Code
#                 |


def p_GrammarComands_List(p):
    """GrammarComands : GrammarComands ',' Code"""
    p[0] = p[1] + "    " + p[3] + "\n"


def p_GrammarComands_Code(p):
    """GrammarComands : Code"""
    p[0] = "    " + p[1] + "\n"


def p_GrammarComands_Empty(p):
    """GrammarComands :"""
    p[0] = ""


# PythonCode -> Codeline
#             | MultiCode
#             | COMENTARY
#             | MultiComment
def p_PythonCode_Codeline(p):
    """PythonCode : Codeline"""
    p[0] = p[1]


def p_PythonCode_MultiCode(p):
    """PythonCode : MultiCode"""
    p[0] = p[1]


def p_PythonCode_Comentary(p):
    """PythonCode : COMENTARY"""
    p[0] = p[1]


def p_PythonCode_MultiComment(p):
    """PythonCode : MultiComment"""
    p[0] = p[1]


# Grammar -> Grammar Elem
#          |
def p_Grammar_List(p):
    """Grammar : Grammar Elem"""
    p[0] = p[1] + " " + p[2]


def p_Grammar_Empty(p):
    """Grammar : """
    p[0] = ""


# Elem -> id
#       | str
def p_Elem_id(p):
    """Elem : id"""
    p[0] = p[1]


def p_Elem_str(p):
    """Elem : str"""
    p[0] = p[1]


# Codeline -> OPENCODELINE CODELINE
def p_Codeline(p):
    """Codeline : OPENCODELINE CODELINE"""
    p[0] = p[2]


# MultiCode -> OPENCODE MCode CLOSECODE
def p_MultiCode(p):
    """MultiCode : OPENCODE MCode CLOSECODE"""
    p[0] = p[2]


# MCode -> MCode CodeOrComment
#        |
def p_MCode(p):
    """MCode : MCode CodeOrComment"""
    p[0] = p[1] + p[2]


def p_MCode_empty(p):
    """MCode : """
    p[0] = ""


# CodeOrComment -> MultiComment
#                |  TEXT
def p_CodeOrComment_Comment(p):
    """CodeOrComment : MultiComment"""
    p[0] = p[1]


def p_CodeOrComment_Code(p):
    """CodeOrComment : TEXT"""
    p[0] = p[1]


# MultiComment -> OPENCOMMENT MCOMMENT CLOSECOMMENT
#               | OPENCOMMENT CLOSECOMMENT
def p_MultiComment_Coment(p):
    """MultiComment : OPENCOMMENT MCOMMENT CLOSECOMMENT"""
    p[0] = ""
    for line in p[2].split('\n'):
        p[0] += "# " + line + "\n"


def p_MultiComment_Empty(p):
    """MultiComment : OPENCOMMENT CLOSECOMMENT"""
    p[0] = ""


# Code -> Code OPERATOR Exp
#       | Code '=' Exp
#       | Code '.' Exp
#       | '[' ListContent ']'
#       | '(' ListContent ')'
#       | id '(' Code ')'
#       | id '[' Code ']'
#       | Exp
def p_Code_Operator(p):
    """Code : Code OPERATOR Exp"""
    p[0] = p[1] + " " + p[2] + " " + p[3]


def p_Code_Equal(p):
    """Code : Code '=' Exp"""
    p[0] = p[1] + " " + p[2] + " " + p[3]


def p_Code_Point(p):
    """Code : Code '.' Exp"""
    p[0] = p[1] + p[2] + p[3]


def p_Code_List(p):
    """Code : '[' ListContent ']' """
    p[0] = p[1] + p[2] + p[3]


def p_Code_Tupple(p):
    """Code : '(' ListContent ')' """
    p[0] = p[1] + p[2] + p[3]


def p_Code_Function(p):
    """Code : Code '(' Code ')'"""
    p[0] = p[1] + p[2] + p[3] + p[4]


def p_Code_Acess(p):
    """Code : Code '[' Code ']'"""
    p[0] = p[1] + p[2] + p[3] + p[4]


def p_Code_exp(p):
    """Code : Exp """
    p[0] = p[1]


# ListContent -> ListContent ',' Exp
#              | Exp
#              |
def p_ListContent_List(p):
    r"""ListContent : Code ',' ListContent  """
    p[0] = p[1] + p[2] + p[3]


def p_ListContent_Exp(p):
    r"""ListContent : Code"""
    p[0] = p[1]


def p_ListContent_Empty(p):
    r"""ListContent : """
    p[0] = ""


# Exp -> OPERATOR Exp
#      | id
#      | num
#      | str
def p_Exp_Operator_exp(p):
    """Exp : OPERATOR Exp """
    p[0] = p[1] + p[2]


def p_Exp_id(p):
    """Exp : id"""
    p[0] = p[1]


def p_Exp_num(p):
    """Exp : num"""
    p[0] = p[1]


def p_Exp_str(p):
    """Exp : str"""
    p[0] = p[1]


def p_error(p):
    print('Erro sintático: ', p)
    parser.success = False


# Build the parser
parser = yacc.yacc()


# Lex content dictionary
lex_content = {}

# Yacc content dictionary
yacc_content = {}

# Name of the project
parser.filename = ""


# Dic to construct grammar
parser.grammar_entries = {}


# Booleans to certify "emptyness"
lex_content["empty"] = False
yacc_content["empty"] = False


parser.success = True


def readFile(filename):

    # Read line from input and parse it
    f = open(filename, "r", encoding="utf-8")
    program = f.read()
    parser.parse(program)
    if parser.filename == "":
        parser.filename = filename.split(".")[0]
    else:
        parser.filename = parser.filename.replace("\"", "")
    if parser.success:
        return parser.filename, lex_content, yacc_content
    else:
        print("Programa inválido ... Corrija e tente novamente!")
