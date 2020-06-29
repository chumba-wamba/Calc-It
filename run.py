from calc_it.lexer import lexer
from calc_it.parser import parser


if __name__ == "__main__":
    tokens = lexer.lex("1+1**2*3")
    print(parser.parse(tokens).eval())
