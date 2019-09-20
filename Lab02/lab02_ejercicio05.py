#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Imprimir, sumar y contar los números que son a la vez multiplos de 2 y de 3 que hay entre el 1 y 
un determinado numero introducido por teclado
"""
__author__ = "Gonzalo Chacaltana Buleje"
__email__ = "gchacaltanab@gmail.com"

if __name__ == "__main__":
    try:
        n_start = 1; multiplo_2_3 = []
        n_end = int(input(u"Ingresa un numero: "))
        if n_start>n_end: raise ValueError(u"El número ingresado debe ser mayor a 1") 
        for n in range(n_start, n_end + 1): multiplo_2_3.append(n) if (n%2==0 and n%3==0)else None
        print(multiplo_2_3)
        print(sum(multiplo_2_3))
        print(len(multiplo_2_3))
    except (ValueError, TypeError) as error:
        print(error)