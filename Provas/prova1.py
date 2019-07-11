from lark import Lark, InlineTransformer
from pprint import pprint

#
# Gramática para expressões regulares
#
grammar = r"""
?start : expr

?expr  : rule

?rule  : single
        | concat
        | alt

?op : alt | concat

alt : letter ALT letter
ALT: /\|/

?single : atom

?atom   : letter
    
concat : letter | letter concat    

letter  : LETTER
LETTER  : /a|b|c/
%ignore /\s+/
"""
parser = Lark(grammar, parser='lalr')

#
# Transforma para S-expressions
#
class Transformer(InlineTransformer):
    def alt(self, a, b):
        if isinstance(b, tuple) and b[0] == 'alt':
            return ('alt', a, *b[1:])
        return ('alt', a, b)

    def concat(self, a, b):
        if isinstance(b, tuple) and b[0] == 'concat':
            return ('concat', a, *b[1:])
        return ('concat', a, b)

    def power(self, a):
        return ('power', a)

    def letter(self, c):
        return str(c)


transformer = Transformer()

#
# Testes
#
examples = {
    'a': 'a',
    'ab': ('concat', 'a', 'b'),
    
    'a|b': ('alt', 'a', 'b'),
    'abc': ('concat', 'a', 'b', 'c'),
    'a*': ('power', 'a'),
    'ab*': ('concat', 'a', ('power', 'b')),
    'a|bc*': ('alt', 'a', ('concat', 'b', ('power', 'c'))),
    'ab|c(ab*)*|a': ('alt',
        ('concat', 'a', 'b'),
        ('concat', 'c', ('power', ('concat', 'a', ('power', 'b')))),
        'a'),
}

for expr, sexpr_ in examples.items():
    print('\n', '-' * 40, sep='')
    
    print('Expressão:', expr)
    
    print('\nLark:')
    print(parser.parse(expr).pretty())
    
    print('S-Expr')
    sexpr = transformer.transform(parser.parse(expr))
    pprint(sexpr)
    
    assert sexpr == sexpr_, 'esperado ' + str(sexpr_)

print('\n\nTodos testes passaram. PARABÉNS!')
