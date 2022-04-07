import unittest
import pathlib
import lzw

class TestLzw(unittest.TestCase):

    def test_lzw_list_of_codes(self):
        res = lzw.pack_lzw("TOBEORNOTTOBEORTOBEORNOT")
        self.assertEqual(res, [84, 79, 66, 69, 79, 82, 78, 79, 84, 256, 258, 260, 265, 259, 261, 263])

    def test_lzw_unpacks_list_of_codes(self):
        res = lzw.unpack_lzw([84, 79, 66, 69, 79, 82, 78, 79, 84, 256, 258, 260, 265, 259, 261, 263])
        self.assertEqual(res, "TOBEORNOTTOBEORTOBEORNOT")

def test_files(tmp_path:pathlib.Path):
        d = tmp_path / "test"
        d.mkdir()
        file = d/"test.txt"
        print(file)
        file.write_text("Lorem ipsum dolor sit amet,")
        lzw.pack(f"{tmp_path}/test/test.txt")
        lzw.unpack(f"{tmp_path}/test/test.txt.lzw")
        res = d/"test.txt.lzw.lzw_unpacked"
        assert(res.read_text() == "Lorem ipsum dolor sit amet,")