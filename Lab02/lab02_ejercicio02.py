#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Imprimir los números del 1 al 100 y calcular la suma de todos los números pares por un lado;
e impares por otro.
"""
__author__ = "Gonzalo Chacaltana Buleje"
__email__ = "gchacaltanab@gmail.com"

if __name__ == "__main__":
    n_start = 1; n_end = 100; num_par = []; num_impar = []
    for n in range(n_start, n_end + 1):
        num_par.append(n) if n%2==0 else num_impar.append(n);print(n)
    print(u'La suma de números pares es %s' % sum(num_par))
    print(u'La suma de números impares es %s' % sum(num_impar))