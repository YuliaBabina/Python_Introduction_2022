def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    out = ""
    upp, down = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', "abcdefghijklmnopqrstuvwxyz"
    keyword = (keyword * len(keyword))[:len(plaintext)]
    for i in range(len(plaintext)):
        if plaintext[i] in down:
            out += down[(down.find(plaintext[i]) + down.find(keyword[i])) % 26]
        elif plaintext[i] in upp:
            out += upp[(upp.find(plaintext[i]) + upp.find(keyword[i])) % 26]
        else:
            out += plaintext[i]
    return out


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    out = ""
    upp, down = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', "abcdefghijklmnopqrstuvwxyz"
    keyword = (keyword * len(ciphertext))[:len(ciphertext)]
    for i in range(len(ciphertext)):
        if ciphertext[i] in down:
            out += down[(down.find(ciphertext[i]) - down.find(keyword[i]) + 26) % 26]
        elif ciphertext[i] in upp:
            out += upp[(upp.find(ciphertext[i]) - upp.find(keyword[i]) + 26) % 26]
        else:
            out += ciphertext[i]
    return out
