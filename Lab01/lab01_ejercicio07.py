#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Calcular e imprimir la suma 50 + 48 + 46 + 44 + .... + 20
"""
__author__ = "Gonzalo Chacaltana Buleje"
__email__ = "gchacaltanab@gmail.com"

if __name__ == "__main__":
    n = 50; limit = 20; sequence = 2; sum = 0
    while n>=limit:sum+=n;n-=sequence;
    print(sum)