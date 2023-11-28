from src import alphabets as al


def gen_n_and_f(p: int, q: int) -> (int, int):
    n = p * q
    euler_func = (p - 1) * (q - 1)
    return n, euler_func


def gen_privkey(p: int, q: int) -> tuple:
    n, euler_func = gen_n_and_f(p, q)
    d = 0
    for _d in range(2, euler_func):
        if euler_func % _d == 0:
            d = _d
            break
    return d, n


def gen_pubkey(p: int, q: int, d: int) -> tuple:
    n, euler_func = gen_n_and_f(p, q)
    e = 0
    for _e in range(2, euler_func):
        if 25 * _e - 1 % euler_func == 0:
            e = _e
            break
    return e, n


def rsa_encryption(pubkey: tuple, data: str) -> str:
    res = ''
    res_list = []
    for symbol in data:
        res_list.append(chr(al.alphabet[symbol] ** pubkey[0] % pubkey[1]))
    res = ''.join(res_list)
    return res


def rsa_decryption(privkey: tuple, data: str) -> str:
    res = ''
    res_list = []
    for symbol in data:
        res_list.append(chr(al.alphabet[symbol] ** privkey[0] % privkey[1]))
    res = ''.join(res_list)
    return res


def main():
    p, q = 97, 17
    data_for_cipher = input("Введите свои инициалы: ")
    if len(data_for_cipher) != 3:
        print("Больше трех букв, выход из программы...")
        exit(1)
    privkey = gen_privkey(p, q)
    pubkey = gen_pubkey(p, q, privkey[0])
    cipher_result = rsa_encryption(pubkey, data_for_cipher)
    print('Результат шифрования: ' + cipher_result)
    decryption_result = rsa_decryption(privkey, cipher_result)

    print('Результат дешифрования: ' + decryption_result)


if __name__ == "__main__":
    main()
