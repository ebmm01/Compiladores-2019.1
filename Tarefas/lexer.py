import tokenize
import io

BLACKLIST = {
    tokenize.NL,
    tokenize.INDENT,
    tokenize.DEDENT,
    tokenize.NEWLINE,
    tokenize.ENDMARKER,
    tokenize.ENCODING
}


REGEX_EXP = [
    ('STRING', r'".*"'),
    ('NUMBER', ''),
    ('NAME', '')


]


def tokens(code):
    fd = io.BytesIO(code.encode('utf8'))
    tks = tokenize.tokenize(fd.__next__)
    next(tks)
    for tk in tks:
        if tk.type not in BLACKLIST:
            yield (tk.string, tokenize.tok_name[tk.type])



def make_lexer(defs, ignore=(), keywords=()):
    """
    Retorna um lexer a partir de um dicionario com
    definicoes de tokens
    """
    defs['error'] = r'.+?'
    named = [r'(?P<%s>%s)' % (k, v) 
             for (k, v) in defs.items()]
    regex = re.compile('|'.join(named))
    
    def lexer(code):
        tokens = []
        line_no = 1
        indent = 0
        
        for m in regex.finditer(code):
            i, j = m.span()
            data = m.string[i:j]
            kind = m.lastgroup
            
            if kind == 'space':
                line_no += data.count('\n')
            if data in keywords:
                tokens.append(Token(data, 'keyword'))
            elif kind == 'error':
                raise ValueError(f'invalido: {data!r}')
            elif kind not in ignore:
                tokens.append(data, kind)
            
        return tokens
        
    return lexer
    
    
defs = {
    'NAME': r'[a-zA-Z_]\w*',
}

def analyze_token(tk):



    return None


while True:
    tk = tokens(input())

    [print(x) for x in tk]
    print('\n')


