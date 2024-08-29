"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(s):
    result = s
    lista_nueva = []
    conta = 1
    for ele in range(len(result)):
        lista_nueva.append({
                str(conta): str(conta + 1)
            })
        conta += 2
    return lista_nueva
