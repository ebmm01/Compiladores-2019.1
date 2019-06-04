import re


# ex 1
# (?P<openning><(?P<name>[a-z\-]*?)>)(?P<content>[^<]*?)(?P<closing><\/(?P=name)>)

# ex 2
#  \d{4}-\d{2}-\d{2}T\d{2}:\d{2}-\d{2}:\d{2}

# ex 3
# 0x([0-9,a-f]+_?)*[0-9,a-f]$
