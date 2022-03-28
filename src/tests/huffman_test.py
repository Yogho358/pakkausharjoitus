import unittest
import huffman

class TestHuffman(unittest.TestCase):
    
    def test_symbols_with_weights_converted_to_binary(self):
        symbols = [("A",0.38), ("B",0.18), ("C",0.15), ("D",0.15), ("E",0.13)]
        res = huffman.encode_tuples_to_binary(symbols)
        answer = {
            "A": "1",
            "B": "000",
            "C": "010",
            "D": "001",
            "E": "011"
            }
        self.assertEqual(res,answer)