"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [0] output => [0] 
"""


def fn_hack_7(s):
    result = s
    texto = []
    if (len(result) > 0) & (result[0] != 0):
        for ele in range(1,  len(result)+1):
            if ele % 2 == 0:
                texto.append(ele) 
            else:
                texto.append(str(ele))
    else:
        texto.append(0)
    return texto

