import unittest
from lex import token_table as tt

class TestTokenTable(unittest.TestCase):
    
    def test_get_token_id(self):
        cases = {
            0: [
                { "events": range(0, 23), "expected": -2 },
                { "events": [23],  "expected": -1 }
            ],
            1: [
                { "events": [0, 1], "expected": -2 },
                { "events": range(2, 24), "expected": 256 }
            ],
            2: [
                { "events": [1, 7], "expected": -2 },
                { "events": [0, 2, 3, 4, 5, 6], "expected": 257 },
                { "events": range(8, 24), "expected": 257 }
            ],
            3: [
                { "events": [1], "expected": -2 },
                { "events": range(2, 24), "expected": 258 },
                { "events": [2], "expected": 258 }
            ],
            4: [
                { "events": range(0, 24), "expected": -2 }
            ]
        }
        
        for last, allCases in cases.items():
            with self.subTest(last):
                for case in allCases:
                    for event in case["events"]:
                        self.assertEqual(tt.get_token_id(last, event), case["expected"])


if __name__ == '__main__':
    unittest.main()