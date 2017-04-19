#!/usr/bin/env python3

def caesar_cipher_encrypt(text, key):
    encrypted = ""
    for i in text:
        if ord(i.upper()) >= 65 and ord(i.upper()) <= 90:
            letter_ascii = ord(i.upper()) + key
            if letter_ascii > 90:
                to_append = chr(ord(i)+key-26)
            else:
                to_append = chr(ord(i)+key)
        else:
            to_append = i
        encrypted += to_append
    return encrypted

def caesar_cipher_decrypt(text, key):
    decrypted = ""
    for i in text:
        if ord(i.upper()) >= 65 and ord(i.upper()) <= 90:
            letter_ascii = ord(i.upper()) - key
            if letter_ascii < 65:
                to_append = chr(ord(i)+key+26)
            else:
                to_append = chr(ord(i)-key)
        else:
            to_append = i
        decrypted += to_append
    return decrypted

print(caesar_cipher_decrypt("efgfoe uif fbtu xbmm pg uif dbtumf",1))
