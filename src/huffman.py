import json
from hm_pack import pack_algorithm
from hm_unpack import unpack_algorithm


def pack(filename):
    with open(filename) as file:
        read_file = file.read()
        org_length = len(read_file)
        packed = pack_algorithm(read_file)
        offset = packed[2]
        packed_file = packed[1]
        code_in_string = json.dumps(packed[0])
        codes_length = len(code_in_string)
        packed_length = len(packed_file)
        path_parts = filename.split("/")
        new_filename = path_parts[len(path_parts)-1]+".hm"
        new_path = ""
        for i in range(len(path_parts)-1):
            new_path = new_path + path_parts[i]+"/"
        new_path = new_path+new_filename
        with open(new_path, "wb") as new_file:
            new_file.write(str(offset).encode())
            new_file.write(str(codes_length).encode())
            new_file.write(code_in_string.encode())
        with open(new_path, "ab") as new_file:
            new_file.write(packed_file)

        return (packed_length+len(code_in_string))/org_length*100


def unpack(filename):

    with open(filename, "rb") as file:
        offset = int(file.read(1))
        dict_length = ""
        chunk = file.read(1)

        while chunk != b'{':
            dict_length += chunk.decode()
            chunk = file.read(1)

        codes = "{"+file.read(int(dict_length)-1).decode()

        data_binary = file.read()
        data = ""
        for x in data_binary:
            data = data+f"{x:08b}"

        unpacked_data = unpack_algorithm(json.loads(codes), data[offset:])

        path_parts = filename.split("/")
        new_filename = path_parts[len(path_parts)-1]+".hm_unpacked"
        new_path = ""
        for i in range(len(path_parts)-1):
            new_path = new_path + path_parts[i]+"/"
        new_path = new_path+new_filename
        with open(new_path, "w") as new_file:
            new_file.write(unpacked_data)
