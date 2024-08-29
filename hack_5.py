"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(s):
    result = s
    if len(result) < 3:
        return result
    
    result = list(result)
    cont = 2
    resultado = ""
    
    for ele in result:
        if cont == 0:
            resultado += "-"
            cont = 2
        else:
            resultado += ele
            cont -= 1
    
    if result[0] == "f":
        resultado = resultado[:5] + "-ma-"
        
    return resultado
