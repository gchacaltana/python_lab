#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Imprimir los números 48,52,56,....,120
"""
__author__ = "Gonzalo Chacaltana Buleje"
__email__ = "gchacaltanab@gmail.com"

if __name__ == "__main__":
    n = 44; limit = 120; sequence = 4; serie = []
    while n<limit:n+=sequence;serie.append(n);
    print(serie)