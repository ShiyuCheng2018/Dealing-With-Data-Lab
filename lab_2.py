def hash_code(string, int):
    sum = 0;
    for i in string:
        sum += ord(i)

    return sum % int


def my_hex(int):
   return hex(int)

def hex_ch(string):
    return my_hex(ord(string))[2:].upper()

def hex_str(string):

    str = "0x"
    for i in string:
        str += hex_ch(i)
    print(str)


def main():
    print(hash_code(" aA", 127))
    print(my_hex(63))
    print(hex_ch("?"))
    hex_str("why?")

main()



