from tkinter import ttk, filedialog, messagebox
from huffman import pack as pack_hm, unpack as unpack_hm
from lzw import pack as pack_lzw, unpack as unpack_lzw


class UI:
    def __init__(self, root):
        self._root = root

    def show_popup(self, packed_percentage):
        messagebox.showinfo(
            title="pakattu", message=f"Pakattu, pakatun tiedoston koko {packed_percentage} prosenttia alkuperäisestä")

    def pack_hm(self):
        packed_percentage = pack_hm(filedialog.askopenfilename())
        self.show_popup(packed_percentage)

    def unpack_hm(self):
        unpack_hm(filedialog.askopenfilename())

    def pack_lzw(self):
        packed_percentage = pack_lzw(filedialog.askopenfilename())
        self.show_popup(packed_percentage)

    def unpack_lzw(self):
        unpack_lzw(filedialog.askopenfilename())

    def start(self):
        main_label = ttk.Label(master=self._root, text="Pakkausharjoitus")

        compress_to_huff_button = ttk.Button(
            self._root, text="Pakkaa tiedosto huffmanilla", command=self.pack_hm)
        decompress_hm_button = ttk.Button(
            self._root, text="Pura Huffman-tiedosto", command=self.unpack_hm)
        compress_to_lzw_button = ttk.Button(self._root, text="Pakkaa tiedosto LZW:llä", command = self.pack_lzw)
        decompress_lzw_button = ttk.Button(self._root, text="Pura LZW-tiedosto", command = self.unpack_lzw)
        main_label.pack()
        compress_to_huff_button.pack()
        decompress_hm_button.pack()
        compress_to_lzw_button.pack()
        decompress_lzw_button.pack()
