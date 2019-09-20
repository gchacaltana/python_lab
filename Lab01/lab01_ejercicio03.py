#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Programa que imprima los números pares desde el 40 al 60 (incluir ambos)
"""
__author__ = "Gonzalo Chacaltana Buleje"
__email__ = "gchacaltanab@gmail.com"

if __name__ == "__main__":
    n_start = 40; n_end = 60
    print([n for n in range(n_start,n_end+1) if n%2==0])