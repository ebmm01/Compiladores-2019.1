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


###########################################
# Teste Lambda
print("\n Teste Lambda \n")
print(eval(parse('(lambda (x) (+ x 1))'))(41))
###########################################

###########################################
# Teste even, odd
_is_even = global_env['even?']
_is_odd = global_env['odd?']
print("\n Teste even, odd\n (se nenhum erro for apresentado, o teste passou) \n")
print(_is_even(42))
print( not _is_even(21))
assert _is_even(42) and not _is_even(21)
assert not _is_odd(42) and _is_odd(21)

###########################################

###########################################
# Teste quotient
_quotient = global_env['quotient']
print("\n Teste Quotient (se nenhum erro for apresentado, o teste passou) \n")
assert _quotient(10, 3) == 3
print(_quotient(-10.0, 3))
assert _quotient(-10.0, 3) == -3.0
assert _quotient(13, -5) == -2
assert _quotient(-13, -5) == 2
###########################################

###########################################
# Teste modulo, remainder
print("\n Teste mod, rem (se nenhum erro for apresentado, o teste passou) \n")

_modulo = global_env['modulo']
assert _modulo(10, 3) == 1
print("Modulo", _modulo(-10.0, 3))
assert _modulo(-10.0, 3) == 2.0
assert _modulo(10.0, -3) == -2.0
assert _modulo(-10, -3) == -1

_remainder = global_env['remainder']
assert _remainder(10, 3) == 1
print("Remainder", _remainder(-10.0, 3))
assert _remainder(-10.0, 3) == -1.0
assert _remainder(10.0, -3) == 1.0
assert _remainder(-10.0, -3) == -1.0
assert isinstance(_remainder(13, 4), int)
###########################################

###########################################
# Testes Complexos
scheme_factorial = '''
(define fat (lambda (n) 
    (if (< n 2) 
        1
        (* n (fat (- n 1))))))
'''

scheme_fib = '''
(define fib (lambda (n) 
    (if (< n 2) 
        1
        (+ (fib (- n 2)) (fib (- n 1))))))
'''

cmd = '''
(begin 
    (define collatz (lambda (n) 
        (cons 1 (list 2 3))))
    
    (define auxiliary-function (lambda (n) n)))
'''
# (escreva sua solução aqui...)

fat = eval(parse(scheme_factorial))
fib = eval(parse(scheme_fib))
collatz = eval(parse(cmd), e)
print("\nTestes Complexos \n")
print("Fatorial:")
print(fat(5))
print("Fib:")
print(fib(5))
collatz = e['collatz']
print("Collatz:")
print(collatz(13))
###########################################