#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Programa que imprima los números impares desde el 100 hasta la unidad y calcule su suma.
"""
__author__ = "Gonzalo Chacaltana Buleje"
__email__ = "gchacaltanab@gmail.com"

if __name__ == "__main__":
    n = 100; limit = 1; nums_impar = []
    while n>=limit:nums_impar.append(n) if n%2!=0 else None;n-=1
    print(nums_impar)
    print("La suma es %s" % sum(nums_impar))