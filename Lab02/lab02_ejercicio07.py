#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Introducir los valores A,B,C: si A dividido entre B es mayor a 30,calcular e imprimir A/C*B^3;
si A divido entre B es menor o igual a 30, calcular e imprimir 2^2 + 4^2 + 6^2 + .... + 30^2
"""
__author__ = "Gonzalo Chacaltana Buleje"
__email__ = "gchacaltanab@gmail.com"
import math

class OperationsToABC(object):
    def __init__(self):
        self.a = 0; self.b = 0; self.c = 0
        self.n_start = 1; self.n_end = 30

    def run(self):
        self.input_numbers()
        self.switchCalculate()

    def input_numbers(self):
        self.a = int(input(u"Ingrese el valor de A: "))
        self.b = int(input(u"Ingrese el valor de B: "))
        self.c = int(input(u"Ingrese el valor de C: "))

    def switchCalculate(self):
        self.invokeCalculateA() if math.floor(self.a/self.b)>30 else self.invokeCalculateB()

    def invokeCalculateA(self):
        print("A/C*B^3 =  %s" %((self.a/self.c)*math.pow(self.b,3)))
    
    def invokeCalculateB(self):
        serie = [math.pow(n,2) for n in range(self.n_start, self.n_end+1) if n%2==0]
        print("Serie: 2^2 + 4^2 + ... + 30^2 = %s" %(sum(serie)))

if __name__ == "__main__":
    try:
        app = OperationsToABC()
        app.run()
    except (ValueError, TypeError) as error:
        print(error)
    except ZeroDivisionError as error:
        print("Ocurrió un error: %s" %error)