import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    upp, down = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', "abcdefghijklmnopqrstuvwxyz"
    d = {}
    for i in plaintext:
        if i in down:
            d.update(str.maketrans(i, down[(down.find(i) + shift) % 26]))
        elif i in upp:
            d.update(str.maketrans(i, upp[(upp.find(i) + shift) % 26]))
        else:
            d.update(str.maketrans(i, i))
    return plaintext.translate(d)


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    upp, down = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', "abcdefghijklmnopqrstuvwxyz"
    d = {}
    for i in ciphertext:
        if i in down:
            d.update(str.maketrans(i, down[(down.find(i) - shift) % 26]))
        elif i in upp:
            d.update(str.maketrans(i, upp[(upp.find(i) - shift) % 26]))
        else:
            d.update(str.maketrans(i, i))
    return ciphertext.translate(d)


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
