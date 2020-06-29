from calc_it import lexer_generator


lexer_generator.add("EXPONENT", r"\*\*")
lexer_generator.add("PLUS", r"\+")
lexer_generator.add("MINUS", r"-")
lexer_generator.add("MULTIPLY", r"\*")
lexer_generator.add("DIVIDE", r"/")
# lexer_generator.add("L_PAREN", r"\(")
# lexer_generator.add("R_PAREN", r"\)")
lexer_generator.add("NUMBER", r"\d+")

lexer_generator.ignore(r"\s")


lexer = lexer_generator.build()
