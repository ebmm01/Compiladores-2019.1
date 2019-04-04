import math
import operator as op
from collections import ChainMap

def tokenize(chars: str) -> list:
    """
    Converte uma string de caracteres em uma lista de tokens.
    """
    return chars.replace("(", " ( ").replace(")", " ) ").split()

Symbol = str              # Um símbolo Scheme, implementado como uma string Python
Number = (int, float)     # Um símbolo Scheme, implementado como int ou float
Atom   = (Symbol, Number) # Um átomo pode ser um símbolo ou um número
List   = list             # Uma lista Scheme representada como uma lista Python
Exp    = (Atom, List)     # Expressão Scheme, que pode ser um átomo ou uma lista

def parse(program: str) -> Exp:
    """
    Lê uma expressão Scheme de uma string e retorna a árvore sintática correspondente.
    """
    return read_from_tokens(tokenize(program))

def read_from_tokens(tokens: list) -> Exp:
    """
    Monta árvore sintática a partir de uma lista de tokens.
    """
    if len(tokens) == 0:
        raise SyntaxError('EOF')
    token = tokens.pop(0)
    if token == '(':
        L = []
        while tokens[0] != ')':
            L.append(read_from_tokens(tokens))
        tokens.pop(0)
        return L
    elif token == ")":
        raise SyntaxError('Erro de fim de lista')
    else:
        try:
            isinstance(int(token),int)
            return int(token)
        except ValueError:
            try:
                isinstance(float(token), float)
                return float(token)
            except ValueError:
                return str(token)


def standard_env():
    """
    Retorna ambiente de execução (dicionário) que mapeia os nomes com
    as implementações das principais funções do Scheme.
    """
    env = {}
    env.update(vars(math)) # sin, cos, sqrt, pi, ...
    env.update({
        'abs': op.abs,
        '+':op.add,
        '-':op.sub, 
        '*':op.mul, 
        '/':op.truediv,
        '>':op.gt, 
        '<':op.lt,
        '>=': op.ge,
        '<=':op.le, 
        '=':op.eq, 
        'append': op.add,
        'apply': lambda proc, args: proc(*args),
        'begin': lambda *x: x[-1],
        'car': lambda x: x[0],
        'cdr': lambda x: x[1:], 
        'cons': lambda x,y: [x] + y,
        'eq?': lambda x,y: x is y,
        'equal?': lambda x,y: x == y,
        'length': lambda x: len(x),
        'list': lambda *args: [arg for arg in args],
        'list?': lambda x: isinstance(x, list),
        'map': lambda fx,lst: map(fx, lst),
        'max': lambda x,y: max(x,y),
        'min': lambda x,y: min(x,y),
        'not': lambda x: not x,
        'null?': lambda lst: len(lst)==0,
        'number?': lambda x: isinstance(x, Number),
        'round': lambda x: int(round(x)),        
        'procedure?': lambda x: callable(x),
        'symbol?': lambda x: isinstance(x, Symbol),
    })
    env.update({
        'even?': lambda x: (x % 2)==0,
        'odd?': lambda x: (x % 2)!=0,
        'quotient': lambda x,y: math.trunc(x/y),
        'modulo': lambda x,y: x%y,
        'remainder': lambda x,y: x - y*math.trunc(x/y),
    })
    return env
    
global_env = standard_env()

def eval(x: Exp, env = None) -> Exp:
    """
    Avalia expressão no ambiente dado.
    """
    if env is None:
        env = global_env.copy()
        
    # Caso seja somente um símbolo, char ou algo assim
    if isinstance(x, Symbol):
        try:
            return env[x]
        except KeyError:
            raise NameError(f'unknown variable: {x}')
    
    # Caso seja um número sozinho
    if isinstance(x, Number):
        return x
    
    # Se for condicional
    if x[0] == 'if':
        _,condicao, verdadeiro, falso = x
        return eval(verdadeiro,env) if eval(condicao, env) else eval(falso,env)
    
    # Definindo uma variável
    if x[0] == 'define':
        (_, variable, value) = x
        env[variable] = result = eval(value, env)
        return result
    
    # Quote (será melhorado futuramente)
    if x[0] == 'quote':
        _, value = x
        return value
    
    if x[0] == 'lambda':
        
        _ ,var, exp = x
        
        def lambda_function(*args_value):
            local = dict(zip(var, args_value))
            new_env = ChainMap(local, env)
            return eval(exp, new_env)
        return lambda_function
    
    # Qualquer outro que não acima:
    else:
        
        func = eval(x[0], env)
        """
        o env abaixo é obrigatório porque ele pode se alterar na recursão.
        Se não estiver explícito, pode levar a erros na compilição de certos lips
        Ex.: Tente rodar eval(parse("(begin (define r 10) (* pi (* r r)))")) sem o env
        E veja o erro acontecer.
        """
        args = [eval(arg, env) for arg in x[1:]]
        return func(*args)
        

def repl(prompt='lis.py> '):
    """
    Executa o console no modo "read-eval-print loop"
    Deve interromper a execução se o usuário digitar "exit"
    """
    while True:
      output = input(prompt)
      if output != "exit":
        print(eval(parse(show_scheme(output))))
      else: 
          return


def show_scheme(exp):
    """
    Converte expressão para sua representação em Scheme.
    """
    if isinstance(exp, List):
        return '(' + ' '.join(map(show_scheme, exp)) + ')' 
    else:
        return str(exp)