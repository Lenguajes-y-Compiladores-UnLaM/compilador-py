keywords = {
    "while": 260,
    "if": 261,
    "else": 262,
    "between": 263,
    "out": 264,
    "in": 265,
    "var": 266,
    "string": 267,
    "int": 268,
    "real": 269,
    "bool": 293,
    "true": 294,
    "false": 295
}

def keyword_token_id(string_id):
    if string_id in keywords:
        return keywords[string_id]
    return 256

def keyword_token_label(string_id):
    if string_id in keywords:
        return string_id
    return "ID"