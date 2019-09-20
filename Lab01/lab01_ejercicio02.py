#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Programa que imprima los números impares desde el 1 al 25 (incluir ambos).
"""
__author__ = "Gonzalo Chacaltana Buleje"
__email__ = "gchacaltanab@gmail.com"

if __name__ == "__main__":
    n_start = 1; n_end = 25
    print([n for n in range(n_start,n_end+1) if n%2!=0])