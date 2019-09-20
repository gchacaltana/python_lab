#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Introducir dos valores A y B: si A es mayor o igual que B, calcular e imprimir la suma 10 + 14 +
18 + ... + 50; si A dividido entre B es menor o igual a 30, calcular e imprimir el valor de la suma
de cuadrados de A y B
"""
__author__ = "Gonzalo Chacaltana Buleje"
__email__ = "gchacaltanab@gmail.com"
import math

class OperationsToAB(object):
    def __init__(self):
        self.a = 0; self.b = 0; self.end_serie = 50
        self.sequence = 4

    def run(self):
        self.input_numbers()
        self.switchCalculate()
    def input_numbers(self):
        self.a = int(input(u"Ingrese el valor de A: "))
        self.b = int(input(u"Ingrese el valor de B: "))

    def switchCalculate(self):
        if self.a>=self.b: self.invokeCalculateA()
        if math.floor(self.a/self.b)<=30:self.invokeCalculateB()

    def invokeCalculateA(self):
        n = 10; sum = 0
        while n<=self.end_serie:sum+=n;n+=self.sequence
        print("A es mayor e igual que B: La suma es %s" %sum)
    
    def invokeCalculateB(self):
        print("Division de A y B es menor e igual que 30: La suma de los cuadrados de A y B es %s" %sum([math.pow(self.a,2),math.pow(self.b,2)]))

if __name__ == "__main__":
    try:
        app = OperationsToAB()
        app.run()
    except (ValueError, TypeError) as error:
        print(error)
    except ZeroDivisionError as error:
         print("Ocurrió un error: %s" % error)