#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Introducir un numero por teclado y decir si es par o impar
"""
__author__ = "Gonzalo Chacaltana Buleje"
__email__ = "gchacaltanab@gmail.com"

if __name__ == "__main__":
    try:
        n = int(input(u'Ingrese un número: '))
        print(u'El número es %s' %('Par' if n%2==0 else 'Impar'))
    except ValueError as error:
        print('Ocurrió un error: %s' % error)