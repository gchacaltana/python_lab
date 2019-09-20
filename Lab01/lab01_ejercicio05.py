#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Calcular e imprimir la suma 1 + 2 + 3 + 4 + 5 + ..... + 50  
"""
__author__ = "Gonzalo Chacaltana Buleje"
__email__ = "gchacaltanab@gmail.com"

if __name__ == "__main__":
    n = 0; limit = 50; sum = 0
    while n<=limit:sum+=n;n+=1;
    print(sum)