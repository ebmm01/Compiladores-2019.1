import os
import re
import math
import operator as op

from collections import deque, ChainMap
from lark import Lark, Transformer


def tokenize(chars: str) -> list:
    """
    Converte uma string de caracteres em uma lista de tokens.
    """
    chars = re.sub('\s{2,}', ' ', chars).strip()
    return chars.replace('(', '( ').replace(')', ' )').replace('\n', '').split(" ")
    

Symbol = str              # Um símbolo Scheme, implementado como uma string Python
Number = (int, float)     # Um símbolo Scheme, implementado como int ou float
Atom   = (Symbol, Number) # Um átomo pode ser um símbolo ou um número
List   = list             # Uma lista Scheme representada como uma lista Python
Exp    = (Atom, List)     # Expressão Scheme, que pode ser um átomo ou uma lista


def parse(program: str) -> Exp:
    """
    Lê uma expressão Scheme de uma string e retorna a árvore sintática correspondente.
    """
    return read_from_tokens(deque(tokenize(program)))


def read_from_tokens(tokens: list) -> Exp:
    """
    Monta árvore sintática a partir de uma lista de tokens.
    """
    
    if tokens[0] == '(':
        del tokens[0] # deleta o primeiro item da lista - tokens[1] passa a ser tokens[0] 
        result = []
        while tokens[0] != ')':
            result.append(read_from_tokens(tokens))
        del tokens[0]
        return result
    
    try:
        result = float(tokens[0])
        del tokens[0]
        return result
    except ValueError:
        return tokens.popleft()
        


def standard_env():
    """
    Retorna ambiente de execução (dicionário) que mapeia os nomes com
    as implementações das principais funções do Scheme.
    """
    
    
    def cons(x, y):
        if y is None:
            y = []

        return [x] + y
    
    env = {}
    env.update(vars(math)) # sin, cos, sqrt, pi, ...
    env.update({
        '+':op.add, '-':op.sub, '*':op.mul, '/':op.truediv, 
        '>': op.gt,
        '<': op.lt,
        '>=': op.ge,
        '<=': op.le,
        '=': op.eq,
        'abs': abs,      
        'append': op.add,
        'apply': lambda proc, args: proc(*args),
        'begin': lambda *x: x[-1],
        'car': lambda x: x[0],
        'cdr': lambda x: x[1:], 
        'cons': lambda x,y: cons(x, y),
        'eq?': op.is_,
        'equal?': op.eq,
        'length': len,
        'list': lambda *x: list(x),
        'list?': lambda x: isinstance(x,list),
        'map':  lambda *args: list(map(*args)),
        'max': max,
        'min': min,
        'not': op.not_,
        'null?': lambda x: x == [],
        'null': None,
        'number?': lambda x: isinstance(x, Number),
        'procedure?': callable,
        'round': round,
        'symbol?': lambda x: isinstance(x, Symbol),
    })
    return env
    
def repl(prompt='lis.py> '):
    """
    Executa o console no modo "read-eval-print loop"
    
    Deve interromper a execução se o usuário digitar "exit"
    """
    current_env = global_env.copy()
    while True:
        code = input(prompt)
        
        if code == 'exit':
            break
        
        val = eval(parse(code), env=current_env)
        if val is not None: 
            print(show_scheme(val))

def show_scheme(exp):
    """
    Converte expressão para sua representação em Scheme.
    """
    if isinstance(exp, List):
        return '(' + ' '.join(map(schemestr, exp)) + ')' 
    else:
        return str(exp)

def eval(x: Exp, env = None) -> Exp:
    """
    Avalia expressão no ambiente dado.
    """
    if env is None:
        env = global_env.copy()
        
    if isinstance(x, (float, int)):
        return x
    elif isinstance(x, Symbol):
        try:
            return env[x]
        except KeyError:
            raise NameError('unknown variable')
    
    head, *args = x
    if head == 'define':
        name, value = args
        env[name] = result = eval(value, env)
        return result

    elif head == 'if':
        cond, true, false = args
        cond = eval(cond, env)
        if cond:
            return eval(true, env)
        else:
            return eval(false, env)
        
    elif head == 'lambda':
        arg_names, body = args
        
        def function(*arg_values):
            local = dict(zip(arg_names, arg_values))
            new_env = ChainMap(local, env)
            return eval(body, new_env)
        return function
    
    elif head == 'quote':
        return args[-1]
    
    else:
        func = eval(head, env)
        args = [eval(arg, env) for arg in args]
        return func(*args)

def standard_env_ext():
    env = standard_env()
    
    def integer_rule(x, y, ret):
        if not isinstance(x, int) or not isinstance(y, int):
            return ret
        
        return int(ret)
    
    def quotient(x, y):
        r = x / y
        
        return math.ceil(r) if r <= 0 else math.floor(r)
    
    env.update({
        'even?': lambda x: x % 2 == 0,
        'odd?': lambda x: x % 2 == 1,
        'quotient': lambda x, y: integer_rule(x, y, quotient(x, y)),
        'modulo': op.mod,
        'remainder': lambda x, y: integer_rule(x, y, math.remainder(x, y)),        
    })
    return env


#####################################

lang_file = open("json_lang.lark")
lispy_parser = Lark(lang_file.read(), start='value')

# cmd = '''
# (define collatz (lambda (n) 
#   (if (= n 1)
#     (cons 1 null)  
#     (if (even? n) 
#       (cons n (collatz (/ n 2)))
#       (cons n (collatz (+ 1 (* 3 n))))))))
# '''

cmd = "(+ 1 2)"
tree = lispy_parser.parse(cmd)
print(tree.pretty())

global_env = standard_env_ext()

ns = standard_env_ext()
eval(parse(cmd), ns)
collatz = ns['collatz']


print(collatz(13) == [13, 40, 20, 10, 5, 16, 8, 4, 2, 1])
print(collatz(5) == [5, 16, 8, 4, 2, 1])
