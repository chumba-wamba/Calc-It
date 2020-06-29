from rply import LexerGenerator, ParserGenerator


lexemes = [
    "EXPONENT",
    "PLUS",
    "MINUS",
    "MULTIPLY",
    "DIVIDE",
    # "L_PAREN",
    # "R_PAREN",
    "NUMBER"
]
precedence = [
    ("left", ["PLUS", "MINUS"]),
    ("left", ["MULTIPLY", "DIVIDE"]),
    ("right", ["EXPONENT"]),
    # ("nonassoc", ["L_PAREN", "R_PAREN"]),
]


lexer_generator = LexerGenerator()
parser_generator = ParserGenerator(lexemes, precedence=precedence)
