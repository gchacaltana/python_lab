#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Imprimir y contar los numeros multiples de 3 que hay entre 1 y 100
"""
__author__ = "Gonzalo Chacaltana Buleje"
__email__ = "gchacaltanab@gmail.com"

if __name__ == "__main__":
    n_start = 1; n_end = 100; num_multiplo_3 = []
    for n in range(n_start, n_end + 1):
        num_multiplo_3.append(n) if n%3==0 else None
    print(num_multiplo_3)
    print(u'Hay %s numeros multiples de 3 del %s al %s' % (len(num_multiplo_3),n_start,n_end))