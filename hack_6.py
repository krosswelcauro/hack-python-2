"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(s):
    result = s
    texto = []
    if len(result) > 0:
        for ele in range(1,  len(result)+1):
            if ele % 2 == 0:
                texto.append("-") 
            else:
                texto.append(str(ele))
    else:
        texto.append("0")
    return texto
