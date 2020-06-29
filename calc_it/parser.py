from calc_it import parser_generator
from calc_it.ast import *


@parser_generator.production('expression : NUMBER')
def expression(p):
    return Number(int(p[0].getstr()))


@parser_generator.production('expression : expression EXPONENT expression')
@parser_generator.production('expression : expression PLUS expression')
@parser_generator.production('expression : expression MINUS expression')
@parser_generator.production('expression : expression MULTIPLY expression')
@parser_generator.production('expression : expression DIVIDE expression')
def expression_binop(p):
    left = p[0]
    right = p[2]
    if p[1].gettokentype() == 'EXPONENT':
        return Exponent(left, right)
    elif p[1].gettokentype() == 'PLUS':
        return Add(left, right)
    elif p[1].gettokentype() == 'MINUS':
        return Subtract(left, right)
    elif p[1].gettokentype() == 'MULTIPLY':
        return Multiply(left, right)
    elif p[1].gettokentype() == 'DIVIDE':
        return Divide(left, right)
    else:
        raise AssertionError('Oops, this should not be possible!')


parser = parser_generator.build()
