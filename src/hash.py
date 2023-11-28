import alphabets as al

def hash(data: str) -> int:
    p, q, h = 97, 17, 9
    i = 1
    for symbol in data:
        h = (h + al.alphabet[symbol]) ** 2 % (p * q)
        if __name__ == "__main__":
            print("H{}: {}".format(i, h))
        i += 1
    return h


def main():
    data_for_hash = input("Введите фамилию: ")
    print('Хеш образ сообщения: {}'.format(hash(data_for_hash)))


if __name__ == "__main__":
    main()
