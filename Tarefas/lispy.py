program = "(begin (define r 10) (* pi (* r r)))"

def tokenize(chars):
    return chars.replace('(', ' ( ').replace(')', ' ) ').split()

def lisp_types(val):

    try: return int(val)
    except ValueError:
        try: return float(val)
        except ValueError: return str(val)

def build_ast(tokens):
    
    if tokens[0] == '(':
        result = []
        del tokens[0]

        while tokens[0] != ')':
            result.append(build_ast(tokens))
        del tokens[0]
        return result
    elif tokens[0] == ')':
        raise SyntaxError('unexpected \')\'')
    else:
        return lisp_types(tokens[0])

def lisp_parse(program):
    return build_ast(tokenize(program))

def lisp_eval(program):
    pass



lisp_eval(program)

