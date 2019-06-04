from lark import Lark, Transformer
import re
import operator as op

precedences = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3,
}

def evaluate(left, operation, right):
    

    ops = {
        '+':op.add,
        '-':op.sub,
        '*':op.mul,
        '/':op.truediv, 
        '^': lambda x, y: x ** y
    }
    

    return (
        ops[operation](int(left), int(right)),
        'NUMBER'
    )

def find_highest_precedence(lexed):

    high_index = (None, 0)
    for lex in lexed:
        precedence = 0
        
        if lex[0] in precedences:
            precedence = precedences[lex[0]]
        
        if precedence > high_index[1]:
            high_index = (lex, precedence)

    return high_index[0]




lang_file = open("calculator.lark")
calc_parser = Lark(lang_file.read(), start='chain')

values = [10, '+', 3, '*', 2, '^', 5, '+', 2]


#text = '10 + 3 * 2 ^ 5 + 2'
text = '9 ^ 3 ^ 2 ^ 2'

# for tk in calc_parser.lex('10 + 2 + 3'):
#     print(repr(tk))


tree = calc_parser.parse(text)
print(tree.pretty())

lexed = []
for tk in calc_parser.lex(text):
    lexed.append(
        (tk[0:], tk.type)
    )

while len(lexed) > 1:

    print(lexed)
    higher = find_highest_precedence(lexed)
    idx = lexed.index(higher)
    res = evaluate(
        lexed[idx-1][0],
        lexed[idx][0],
        lexed[idx+1][0]
    )

    lexed.insert(idx-1, res)
    for i in range(3):
        lexed.pop(idx)

print(lexed[0][0])