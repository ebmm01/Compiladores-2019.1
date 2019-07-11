from lark import Lark, Transformer
import re

lang_file =Lark( r"""start: lang
    lang:  letter
        | doubleletter
        |"a"lang"a"
        | "b"lang"b"
        
    letter: /a|b/
    doubleletter: /aa|bb/
    %import common.WS
    %ignore WS
"""
)

text = 'bbaabb'


tree = lang_file.parse(text)
print(tree.pretty())
