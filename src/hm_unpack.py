

def unpack_algorithm(codes, data):
    
    res = ""
    character_code = ""
    codes = dict((v, k) for k, v in codes.items())


    for digit in data:
        character_code += digit
        if character_code in codes.keys():
            res += codes[character_code]
            character_code = ""
    return res