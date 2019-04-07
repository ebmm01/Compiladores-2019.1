def simple_solve(token, lst_result = []):
    if len(token) == 1:
        return token
    for item in range(len(token)):
        try:
            isinstance(int(token[item]), int)
        except ValueError:
            lst_result = [token[item-2], token[item] , token[item-1]]
            lst_result = ' '.join(lst_result)
            token[item-2] = str(eval(lst_result))
            del token[(item-1):(item+1)]
            
            return simple_solve(token)
            
def tokenize(token):
    return token.split()
 
