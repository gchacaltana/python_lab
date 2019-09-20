#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Calcular e imprimir el producto 1*2*3*....*10 
"""
__author__ = "Gonzalo Chacaltana Buleje"
__email__ = "gchacaltanab@gmail.com"

if __name__ == "__main__":
    n = 1; limit = 10; product = 1
    while n<=limit:product*=n;n+=1;
    print(product)