from lark import Lark, Transformer
import re


class JsonTransformer(Transformer):

    def list(self, items):
        return list(items)

    def pair(self, x: tuple):
        return x[0], x[1]

    def dict(self, items):
        return dict(items)

class TreeToJson(Transformer):

    # def string(self, s=lambda x: x[1:-1]):
    #     return s
    
    # def number(self, n=lambda x: float(x)):
    #     return n

    def string(self, s):
        return s[1:-1]

    def number(self, n):
        return float(n[-1])

    list = list
    pair = tuple
    dict = dict

    null = lambda self, _: None
    true = lambda self, _: True
    false = lambda self, _: False



lang_file = open("json_lang.lark")

json_parser = Lark(lang_file.read(), start='value')


text = '{"key": ["item0", "item1", 12, 0, 3.14]}'
tree = json_parser.parse(text)
print(tree.pretty())

transf = JsonTransformer().transform(tree)
print(transf.pretty())

json = TreeToJson().transform(tree)
print(json.pretty())
