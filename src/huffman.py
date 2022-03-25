
def pack(filename):
    with open(filename) as file:
        read_file = file.read()
        org_length = len(read_file)
        packed_file = pack_algorithm(read_file)
        packed_length = len(packed_file)
        path_parts = filename.split("/")
        new_filename = path_parts[len(path_parts)-1]+".hm"
        new_path = ""
        for i in range(len(path_parts)-1):
            new_path = new_path + path_parts[i]+"/"
        new_path = new_path+new_filename
        with open(new_path, "w") as new_file:
            print(new_path)
            new_file.write(packed_file)

        return org_length/packed_length*100

def pack_algorithm(file):
    return file