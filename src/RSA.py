from common import alphabet as al
import sys


def gen_n_and_f(p: int, q: int) -> (int, int):
    n = p * q
    euler_func = (p - 1) * (q - 1)
    return n, euler_func


def gen_privkey(p: int, q: int) -> tuple:
    n, euler_func = gen_n_and_f(p, q)
    d = 0
    for _d in range(2, euler_func):
        if euler_func % _d != 0:
            d = _d
            break
    return d, n


def gen_pubkey(p: int, q: int, d: int) -> tuple:
    n, euler_func = gen_n_and_f(p, q)
    e = 0
    for _e in range(2, euler_func):
        if (d * _e - 1) % euler_func == 0:
            e = _e
            break
    return e, n


def rsa_encryption(pubkey: tuple, data: str) -> list:
    res_list = []
    for symbol in data:
        res_list.append(al[symbol] ** pubkey[0] % pubkey[1])
    return res_list


def rsa_decryption(privkey: tuple, data: list) -> list:
    res_list = []
    for symbol in data:
        res_list.append(symbol ** privkey[0] % privkey[1])
    return res_list


def main():
    if len(sys.argv) == 3:
        p, q = int(sys.argv[1]), int(sys.argv[2])
    else:
        p, q = 97, 17
    data_for_cipher = input("Введите свои инициалы: ").strip()
    if len(data_for_cipher) != 3:
        print("Больше трех букв, выход из программы...")
        exit(1)
    print('p = {}\nq = {}'.format(p, q))
    tmp = []
    for symbol in data_for_cipher:
        tmp.append(al[symbol])
    print("Сообщение в цифровом виде:", end=' ')
    print(tmp)
    privkey = gen_privkey(p, q)
    print('Приватный ключ: {}'.format(privkey))
    pubkey = gen_pubkey(p, q, privkey[0])
    print('Публичный ключ: {}'.format(pubkey))
    cipher_result = rsa_encryption(pubkey, data_for_cipher)
    print('Результат шифрования:', end=' ')
    print(cipher_result)
    decryption_result = rsa_decryption(privkey, cipher_result)
    print('Результат дешифрования:', end=' ')
    print(decryption_result)


if __name__ == "__main__":
    main()
