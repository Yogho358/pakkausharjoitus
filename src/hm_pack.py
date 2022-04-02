import heapq
from collections import Counter

class Node:
    def __init__(self, symbol = None, weight = None, left = None, right = None):
        self.symbol = symbol
        self.weight = weight
        self.left = left
        self.right = right

def pack_algorithm(file):
    weights = find_weights(file)
    codes = encode_tuples_to_binary(weights)
    code_string = create_code_string(file, codes)
    bytes = string_to_bytes(code_string)

    return (codes, bytes[0], bytes[1])

def find_weights(file):
    characters = Counter(file)
    res = []
    total = len(file)
    for character in characters:
        res.append((character, characters[character]/total))
    return res

def encode_tuples_to_binary(tuple_list):
    tree = create_tree(tuple_list)
    res = {}
    create_dictionary(tree, "", res)
    return res
    
def create_code_string(file, codes):
    res = ""
    for character in file:
        res += codes[character]
    return res

def string_to_bytes(string):
    barray = bytearray()
    offset = 0 if len(string) % 8 == 8 else 8 - (len(string)%8)
    string = offset * "0" + string
    for i in range(0, len(string), 8):
        barray.append(int(string[i:i+8], 2))
    
    return (bytes(barray), offset)

def create_tree(tuple_list):
    heap = []

    for i in range (len(tuple_list)):
        heapq.heappush(heap, (tuple_list[i][1],i,Node(tuple_list[i][0],tuple_list[i][1])))


    j = len(tuple_list)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)[2]
        node2 = heapq.heappop(heap)[2]

        heapq.heappush(heap, (node1.weight+node2.weight, j, Node(weight=node1.weight+node2.weight, right=node1, left=node2)))
        j += 1
    
    return heapq.heappop(heap)[2]



def create_dictionary(node, path, dictionary):

    if node.symbol:
        dictionary[node.symbol] = path
        return

    create_dictionary(node.left, path+"0", dictionary)
    create_dictionary(node.right, path+"1", dictionary)