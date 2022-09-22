import unittest
from lex import lexico, keyword_table as kt


class TestLexico(unittest.TestCase):

    def test_get_event(self):
        cases = {
            "a": 0,
            "z": 0,
            "p": 0,
            "A": 0,
            "Z": 0,
            "J": 0,
            "0": 1,
            "9": 1,
            "4": 1,
            '"': 2,
            "{": 3,
            "}": 4,
            "(": 5,
            ")": 6,
            ".": 7,
            ";": 8,
            ",": 9,
            "-": 10,
            "+": 11,
            "/": 12,
            "*": 13,
            "<": 14,
            ">": 15,
            "|": 16,
            "&": 17,
            "!": 18,
            "=": 19,
            ":": 20,
            "?": 21,
            " ": 22,
            "\t": 22,
            "\n": 22,
            "\r": 22
        }

        for character, expected in cases.items():
            with self.subTest(character):
                self.assertEqual(lexico.get_event(character), expected)

    def test_source_file(self):
        cases = [
            {
                "path": "./files/source.txt",
                "expected": ["out", "CTE_STRING", "PUNTO_COMA"]
            },
            {
                "path": "./files/source1.txt",
                "expected": ["var", "LLAVE_ABRE", "string", "ID", "PUNTO_COMA", "LLAVE_CIERRA", "in", "ID", "PUNTO_COMA",
                             "out", "ID", "OP_CONCAT", "CTE_STRING", "PUNTO_COMA"]
            },
            {
                "path": "./files/source2.txt",
                "expected": ["var", "LLAVE_ABRE", "string", "ID", "PUNTO_COMA", "int", "ID", "PUNTO_COMA",
                             "LLAVE_CIERRA", "in", "ID", "PUNTO_COMA", "ID", "OP_ASIGNACION", "CTE_STRING", "PUNTO_COMA",
                             "if", "ID", "COMP_MAYOR", "CTE_NUMERICA", "LLAVE_ABRE", "ID", "OP_ASIGNACION", "ID",
                             "OP_CONCAT", "CTE_STRING", "PUNTO_COMA", "LLAVE_CIERRA", "else", "LLAVE_ABRE", "ID",
                             "OP_ASIGNACION", "ID", "OP_CONCAT", "CTE_STRING", "PUNTO_COMA", "LLAVE_CIERRA",
                             "out", "ID", "PUNTO_COMA"]
            }
        ]

        for case in cases:
            with self.subTest(case["path"]):
                with open(case["path"]) as source:
                    while True:
                        character = source.read(1)
                        if not character:
                            break

                        response = lexico.yylex(source, character)
                        #print(f'{response["token"]} --> {case["expected"][0]}')
                        self.assertEqual(response['token'], case["expected"].pop(0))
                source.close()


if __name__ == '__main__':
    unittest.main()
