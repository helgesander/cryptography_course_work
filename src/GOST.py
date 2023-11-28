import alphabets as al

def gost_cipher(data: str, key: str) -> (int, int):
    pass


def from_char_to_int_ascii(char: chr) -> int:
    return ord(char) - 848


def main():
    data_for_cipher = input("Введите 8 первых букв ФИО: ")
    key_cipher = input("Введите ключ из 4 букв: ")
    l1, r1 = gost_cipher(data_for_cipher, key_cipher)
    print('L1: '.format(bin(l1)[2:], bin(r1)[2:]))


if __name__ == '__main__':
    main()
