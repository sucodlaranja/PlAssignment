from projeV2_lex import lexer

f = open("teste2.txt", "r", encoding="utf-8")

program = f.read()
lexer.input(program)

for tok in lexer:
    print(tok)
