#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Introducir 2 números por teclado. Imprimir los números que hay entre ellos, comenzando por el menor.
Contar cuántos hay, cuántos son pares, y cuál es la suma de todos los impares.
"""
__author__ = "Gonzalo Chacaltana Buleje"
__email__ = "gchacaltanab@gmail.com"

class AnalyzeTwoNumbers(object):
    def __init__(self):
        self.elems = []; self.n_par = []; self.n_impar = [];self.min_n_show_detail = 5

    def run(self):
        self.input_numbers()
        self.process()
        self.print_results()

    def input_numbers(self):
        self.n1 = int(input("Ingresa el número 1: "))
        self.n2 = int(input("Ingresa el número 2: "))

    def process(self):
        self.minor = self.n1 if self.n1<self.n2 else self.n2; 
        self.major = self.n1 if self.n1>self.n2 else self.n2; 
        for n in range(self.minor+1, self.major):
            self.n_par.append(n) if n%2==0 else self.n_impar.append(n); self.elems.append(n)

    def print_results(self):
        if len(self.elems)>self.min_n_show_detail:
            self.print_results_big_numbers()
        else:
            self.print_results_small_numbers()

    def print_results_big_numbers(self):
        print(u"Números que hay del %s al %s" %(self.minor, self.major))
        print(self.elems)
        print(u"Hay %s números del %s al %s" %((self.major-self.minor-1),self.minor, self.major))
        print(u"Hay %s números pares del %s al %s" %(len(self.n_par),self.minor,self.major))
        print(u"La suma de los números impares es: %s" %(sum(self.n_impar)))

    def print_results_small_numbers(self):
        print(u"Números que hay del %s al %s" %(self.minor, self.major))
        print(self.elems)
        print(u"Hay %s números del %s al %s: %s" %((self.major-self.minor-1),self.minor, self.major, self.elems))
        print(u"Hay %s números pares del %s al %s: %s" %(len(self.n_par),self.minor,self.major,self.n_par))
        print(u"La suma de los números impares es: %s - %s" %(sum(self.n_impar),self.n_impar))

if __name__ == "__main__":
    try:
        app = AnalyzeTwoNumbers()
        app.run()
    except (ValueError,TypeError)  as error:
        print(u"Ocurrió un error: %s" %error)