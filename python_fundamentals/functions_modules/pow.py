#!/usr/bin/env python3
def pow(a, b):
    negativo = b < 0
    if negativo:
        b = -b
    resultado = 1
    for i in range(b):
        resultado = resultado * a
    if negativo:
        resultado = 1 / resultado
    return resultado
