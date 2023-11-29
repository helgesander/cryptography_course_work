from hash import hash
from RSA import gen_pubkey, gen_privkey
import sys


def gen_eds(privatekey: tuple, msg_hash: int):
    return (msg_hash ** privatekey[0]) % privatekey[1]


def check_eds(publickey: tuple, msg_hash: int, eds: int) -> bool:
    return (eds ** publickey[0]) % publickey[1] == msg_hash


def main():
    if len(sys.argv) == 4:
        p, q, h = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    else:
        p, q, h = 47, 41, 9
    data = input("Введите фамилию: ")
    print("p = {}\nq = {}\nh = {}".format(p, q, h))
    data_hash = hash(data, p, q, h)
    print("Хеш-образ: {}".format(data_hash))
    privkey = gen_privkey(p, q)
    print("Закрытый ключ: {}".format(privkey))
    pubkey = gen_pubkey(p, q, privkey[0])
    print("Открытый ключ: {}".format(pubkey))
    eds = gen_eds(privkey, data_hash)
    print("Сгенерированная подпись: {}".format(eds))
    ok = check_eds(pubkey, data_hash, eds)
    print("Подпись подлинная" if ok else "Подпись не подлинная")


if __name__ == "__main__":
    main()
