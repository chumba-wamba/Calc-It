from calc_it.lexer import lexer
from calc_it.parser import parser


if __name__ == "__main__":
    input_string = "1+5**(2*3)"
    tokens = lexer.lex(input_string)
    print(parser.parse(tokens).eval())
