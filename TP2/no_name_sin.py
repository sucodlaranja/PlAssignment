import ply.yacc as yacc
from no_name_lex import tokens, literals

#Este trabalho foi 
#feito em 
#yacccc
# symboltable : dictionary of variables
ts = { }


def p_stat_0(p):
    "stat : VAR '=' exp"
    ts[p[1]]=p[3]


def p_stat_1(p):
    "stat : exp"
    print(p[1])


def p_exp_2(p):
    "exp : exp '+' exp"
    p[0]=p[1]+p[3]


def p_exp_3(p):
    "exp : exp '-' exp"
    p[0]=p[1]-p[3]


def p_exp_4(p):
    "exp : exp '*' exp"
    p[0]=p[1]*p[3]


def p_exp_5(p):
    "exp : exp '/' exp"
    p[0]=p[1]/p[3]


def p_exp_6(p):
    "exp : '-' exp"
    p[0]=p[2]


def p_exp_7(p):
    "exp : '(' exp ')'"
    p[0]=p[2]


def p_exp_8(p):
    "exp : NUMBER"
    p[0]=p[1]


def p_exp_9(p):
    "exp : VAR"
    p[0]=getval(p[1])
#Esta funcao define UM
#error

def p_error(t):
    print(f"Syntax error at '{t.value}', [{t.lexer.lineno}]")

#Esta funcao define UM
#get value

def getval(n):
    if n not in ts:
        print(f"Undefined name '{n}'")
    return ts.get(n, 0)


#inicializacao do 
#yacc

y = yacc.yacc()
y.parse("3+4*7")

