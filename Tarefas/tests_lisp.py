from lisp import *

###########################################
# Teste parser:
program = "(begin (define r 10) (* pi (* r r)))"
assert parse(program) ==  ['begin', ['define', 'r', 10], ['*', 'pi', ['*', 'r', 'r']]]
print("\nTeste parser:" + "\n")
print(parse(program))
###########################################

###########################################
# Teste functions (env):
functions = (
    'abs, sin, cos, sqrt, pi, tan, log, +, -, *, /, >, <, >=, <=, =, append, apply, begin, car, cdr, '
    'cons, eq?, equal?, length, list, list?, map, max, min, not, null?, number?, procedure?, '
    'round, symbol?').split(', ')
print("\nTeste functions:" + "\n")
e = global_env
_sqrt, _cons, _append = e['sqrt'], e['cons'], e['append']
_car, _cdr = e['car'], e['cdr']
_list = e['list']
assert _sqrt(4) == 2
assert _cons(1, [2, 3]) == [1, 2, 3]
assert _append([1, 2], [3, 4]) == [1, 2, 3, 4]
assert _car([1, 2, 3]) == 1
assert _cdr([1, 2, 3]) == [2, 3]
assert _list(1, 2, 3) == [1, 2, 3]
assert all(f in global_env for f in functions)
print(tuple(f in global_env for f in functions))
###########################################

###########################################
# Teste eval:
assert eval(parse('(+ 40 2)')) == 42
assert eval(parse('42')) == 42
assert eval(parse('sqrt'))(4) == 2
assert eval(parse('(sqrt 4)'))  == 2
assert eval(parse('(if (< 1 2) 42 0)')) == 42

ns = {}
assert eval(parse('(define x 42)'), ns) == 42
assert ns == {'x': 42}
print("\n Teste eval \n")
print(eval(parse('(+ 40 2)')))
print(eval(parse('42')))
print(eval(parse('sqrt'))(4))
print(eval(parse('(if (< 1 2) 42 0)')))
print(eval(parse('(define x 42)'), ns))
###########################################

###########################################
# Teste Quote
print("\n Teste Quote \n")
print(eval(parse('(quote (sin x))')))
###########################################