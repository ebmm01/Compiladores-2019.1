
ERROR_STATE = -1

rules = {
    ('0', 0): 1,
    ('1', 0): 2,
    ('0', 1): ERROR_STATE,
    ('1', 1): ERROR_STATE,
    ('0', 2): 3,
    ('1', 2): 2,
    ('0', 3): 4,
    ('1', 3): 2,
    ('0', 4): 4,
    ('1', 4): 2,
    ('0', ERROR_STATE): ERROR_STATE,
    ('1', ERROR_STATE): ERROR_STATE
}

valid_states = [1, 4]


def define_state(current_state, token, rules=rules):
    try:
        return rules[token, current_state]
    except KeyError:
        print("Valor fora do alfabeto: ({})".format(token))
        return ERROR_STATE


def run(tokens, rules=rules, valid_states=valid_states):

    current_state = 0

    for t in tokens:
        current_state = define_state(current_state, t)
        if current_state == ERROR_STATE:
            break

    return current_state in valid_states


while True:
    print(str(run(input())) + "\n")
