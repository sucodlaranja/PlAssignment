from projeV2_lex import lexer
from projV2_sin import parser


def test(a):
    if a == 0:
        f = open("teste2.txt", "r", encoding="utf-8")

        program = f.read()
        lexer.input(program)

        for tok in lexer:
            print(tok)

    elif a == 1:
        # Read line from input and parse it

        f = open("teste2.txt", "r", encoding="utf-8")

        parser.success = True
        program = f.read()
        parser.parse(program)

        if parser.success:
            print("Programa bem estruturado")
        else:
            print("Programa inválido ... Corrija e tente novamente!")


test(0)
