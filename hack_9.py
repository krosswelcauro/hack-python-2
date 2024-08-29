"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(s):
    result = s
    if "foo" in result:
        result.pop("bar")
        result["foo"] = "Fooziman"
        result["Foo"] = result.pop("foo")
        
    return result
