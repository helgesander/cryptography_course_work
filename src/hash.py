import common as al
import sys


def hash(data: str, p: int, q: int, h: int) -> int:
    i = 1
    for symbol in data:
        n = p * q
        first_part = (h + al.alphabet[symbol]) ** 2
        h = first_part % n
        if __name__ == "__main__":
            print("H{} = (H{}+M{}) ^ 2 mod {} = {} mod {} = {}".format(i, i - 1, i, n, first_part, n, h))
        i += 1
    return h


def main():
    if len(sys.argv) == 4:
        p, q, h = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    else:
        p, q, h = 97, 17, 9
    data_for_hash = input("Введите фамилию: ")
    print('Хеш образ сообщения: {}'.format(hash(data_for_hash, p, q, h)))


if __name__ == "__main__":
    main()
