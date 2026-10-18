#!/usr/bin/env python3
def uppercase(str):
    resultado = ""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            resultado = resultado + chr(ord(c) - 32)
        else:
            resultado = resultado + c
    print(resultado)
