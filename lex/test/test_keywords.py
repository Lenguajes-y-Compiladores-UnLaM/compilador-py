import unittest
from lex import keyword_table as kt

class TestKeywordTable(unittest.TestCase):
    
    def test_get_keyword_token_id(self):
        cases = {
            "some": 256,
            "num1": 256,
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
        
        for keyword, token in cases.items():
            with self.subTest(keyword):
                self.assertEqual(kt.keyword_token_id(keyword), token)
                
    def test_get_keyword_token_label(self):
        cases = {
            "some": "ID",
            "num1": "ID",
            "while": "while",
            "if": "if",
            "else": "else",
            "between": "between",
            "out": "out",
            "in": "in",
            "var": "var",
            "string": "string",
            "int": "int",
            "real": "real",
            "bool": "bool",
            "true": "true",
            "false": "false"
        }
        
        for keyword, label in cases.items():
            with self.subTest(keyword):
                self.assertEqual(kt.keyword_token_label(keyword), label)


if __name__ == '__main__':
    unittest.main()