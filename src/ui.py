from tkinter import ttk, filedialog, messagebox
from huffman import pack as pack_hm, unpack as unpack_hm

class UI:
    def __init__(self, root):
        self._root = root

    def pack_hm(self):
        packed_percentage = pack_hm(filedialog.askopenfilename())
        messagebox.showinfo(title = "pakattu", message = f"Pakattu, pakatun tiedoston koko {packed_percentage} prosenttia alkuperäisestä")

    def unpack_hm(self):
        unpack_hm(filedialog.askopenfilename())

    def start(self):
        main_label = ttk.Label(master=self._root, text="Pakkausharjoitus")
        
        compress_to_huff_button = ttk.Button(self._root, text="Pakkaa tiedosto huffmanilla", command=self.pack_hm)
        decompress_hm_button = ttk.Button(self._root, text="Pura Huffman-tiedosto", command=self.unpack_hm)
        main_label.pack()
        compress_to_huff_button.pack()
        decompress_hm_button.pack()