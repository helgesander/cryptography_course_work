from hash import hash
from RSA import gen_pubkey


def generate_eds(data: str) -> int:
    pubkey = gen_pubkey()


def check_eds(private_key: int, public_key: int, msg_hash: int) -> bool:
    pass


def main():
    data = input("Введите фамилию: ")
    data_hash = hash(data)


if __name__ == "__main__":
    main()
