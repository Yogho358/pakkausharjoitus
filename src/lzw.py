from array import array


def create_table():
    table = {}
    for i in range(256):
        table[chr(i)] = i

    return table

def create_unpack_table():
    table = {}
    for i in range(256):
        table[i] = chr(i)

    return table

def pack(filename):
    with open(filename) as file:
        content = file.read()
        codes = pack_lzw(content)
        path_parts = filename.split("/")
        new_filename = path_parts[len(path_parts)-1]+".lzw"
        new_path = ""
        for i in range(len(path_parts)-1):
            new_path = new_path + path_parts[i]+"/"
        new_path = new_path+new_filename
        new_file = open(new_path, "wb")
        code_array = array("i", codes)
        code_array.tofile(new_file)
        new_file.close()
            
def unpack(filename):
    with open(filename, "rb") as file:
        code_array = array("i")
        code_array.frombytes(file.read())
        path_parts = filename.split("/")
        new_filename = path_parts[len(path_parts)-1]+".lzw_unpacked"
        new_path = ""
        for i in range(len(path_parts)-1):
            new_path = new_path + path_parts[i]+"/"
        new_path = new_path+new_filename
        with open(new_path, "w") as new_file:
            new_file.write(unpack_lzw(code_array))

def pack_lzw(content):
    table = create_table()
    p = content[0]
    c = ""
    code = 256
    res = []
    for i in range(len(content)):
        if(i != len(content)-1):
            c += content[i+1]
        
        if(p+c in table.keys()):
            p = p+c
        else:
            res.append(table[p])
            table[p+c] = code
            code += 1
            p = c

        c = ""

    res.append(table[p])
    return res

def unpack_lzw(list):
    table = create_unpack_table()
    old = list[0]
    s = table[old]
    c = s
    count = 256
    res = s
    for i in range(len(list)-1):
        n = list[i+1]
        if(n not in table.keys()):
            s = table[old]
            s = s+c
        else:
            s = table[n]
        res += s
        c = ""
        c += s[0]
        table[count] = table[old]+c
        count += 1
        old = n
    return res