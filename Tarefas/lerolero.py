import random

C_SUJEITO = [
    'Professores',
    'Cientistas',
    'Analistas',
    'Coachs',
    'Terraplanistas',
    'Advogados',
    'Dentistas',
    'Analistas do IBGE'
]

C_VERBO = [
    'alertam',
    'avisam',
    'declaram',
    'denunciam',
    'expõem',
    'proclamam',
    'declamam'
]

ACAO = [
    'engorda',
    'explode',
    'queima',
    'reprova',
    'cura',
    'causa acidentes',
    'faz capotar',
    'é triste',
    'é legal',
    'faz mal',
    'molha',
    'dá cadeia',
    'enlouquece',
    'faz chorar'
]

VERBO1 = [
    'abraçar',
    'derrubar',
    'correr',
    'matar',
    'reprovar',
    'caçar',
    'chorar',
    'jubilar'
]

VERBO2 = [
    'comer',
    'vender',
    'entender',
    'estudar',
    'politicar',
    'criar'
]

SUBS = [
    'uma árvore',
    'árvores',
    'corruptos',
    'galinhas',
    'água',
    'bolsominions',
    'oculos',
    'código',
    'ocultismo'
]

def random_chamada():
    return str(random.choice(C_SUJEITO) + " " + random.choice(C_VERBO))

def random_FV():
    
    def option1():
        return random.choice(VERBO1)

    def option2():
        return str(random.choice(VERBO2) + " " + random.choice(SUBS))

    return random.choice([option1, option2])()

def random_acao():
    return random.choice(ACAO)


def random_titulo():
    return str(random_FV() + " " + random_acao())


for i in range(0,10):
    result = random_chamada() + ": " + random_titulo()

    print(result)