from common import gost_alphabet as al
from common import table


def conversion_function(bin_sum: str) -> str:
    f = []
    res_bin_str = ""
    start, end = 0, 4
    for i in range(8):
        elem_str = bin_sum[start:end]
        elem = int(elem_str, 2)
        f.append(table[elem][i]) # debug
        res_bin_str += format(table[elem][i], '04b')
        start += 4
        end += 4
    return res_bin_str


def gost_cipher(data: str, key: str) -> (str, str, str, str, str):
    l0_str = data[:4]
    r0_str = data[4:]
    l0_str, r0_str = ''.join(format(al[x], 'b') for x in l0_str), ''.join(format(al[x], 'b') for x in r0_str)
    x0_str = ''.join(format(al[x], 'b') for x in key)
    x0 = int(x0_str, 2)
    l0, r0 = int(l0_str, 2), int(r0_str, 2)
    summ = (r0 + x0) % (2 ** 32)
    bin_sum = bin(summ)
    bin_sum = bin_sum[2:]
    f = conversion_function(bin_sum)
    cyclic = f[11:] + f[:11]
    r1 = l0 ^ int(cyclic, 2)
    r1_str = format(r1, 'b')
    return l0_str, r0_str, x0_str, cyclic, r1_str


def main():
    data_for_cipher = input("Введите 8 первых букв ФИО: ")
    key_cipher = input("Введите ключ из 4 букв: ")
    l0, r0, x0, f, r1 = gost_cipher(data_for_cipher, key_cipher)
    print('L0: {}\nR0: {}\nX0: {}\nf(R0,X0): {}\nL1=R0: {}\nR1: {}'.format(l0, r0, x0, f, r0,
                                                                           r1))


if __name__ == '__main__':
    main()
