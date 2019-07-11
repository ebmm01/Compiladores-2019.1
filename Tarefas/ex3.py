from lark import Lark, Transformer
import re

lang_file =Lark( r"""start: lang
    lang:  A
        | B
        | others
        
    A: "a"
    B: "b"
    others: /(a|b)+/
    %import common.WS
    %ignore WS
"""
)

text = 'aaabbb'


tree = lang_file.parse(text)
print(tree.pretty())
