import unittest
import pathlib
import hm_pack
import hm_unpack
import huffman


class TestHuffman(unittest.TestCase):

    def test_symbols_with_weights_converted_to_binary(self):
        symbols = [("A", 0.38), ("B", 0.18), ("C", 0.15),
                   ("D", 0.15), ("E", 0.13)]
        res = hm_pack.encode_tuples_to_binary(symbols)
        answer = {
            "A": "1",
            "B": "000",
            "C": "010",
            "D": "001",
            "E": "011"
        }
        self.assertEqual(res, answer)

    def test_create_code_string(self):
        codes = {
            "A": "1",
            "B": "000",
            "C": "010",
            "D": "001",
            "E": "011"
        }

        string = "BACCAED"
        res = hm_pack.create_code_string(string, codes)
        self.assertEqual(res, "00010100101011001")

    def test_unpacking(self):
        data = "00010100101011001"
        codes = {
            "A": "1",
            "B": "000",
            "C": "010",
            "D": "001",
            "E": "011"
        }

        res = hm_unpack.unpack_algorithm(codes, data)
        self.assertEqual(res, "BACCAED")

def test_files(tmp_path:pathlib.Path):
        d = tmp_path / "test"
        d.mkdir()
        file = d/"test.txt"
        file.write_text("Lorem ipsum dolor sit amet,")
        huffman.pack(f"{tmp_path}/test/test.txt")
        huffman.unpack(f"{tmp_path}/test/test.txt.hm")
        res = d/"test.txt.hm.hm_unpacked"
        assert(res.read_text() == "Lorem ipsum dolor sit amet,")