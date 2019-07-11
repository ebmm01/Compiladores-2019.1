from lark import Lark, Transformer
import re

lang_file =Lark( r"""start: lang
    lang: chain
        |"a"lang"b"

    chain: "ab"

    %import common.WS
    %ignore WS
"""
)

text = 'aaabbb'


tree = lang_file.parse(text)
print(tree.pretty())
