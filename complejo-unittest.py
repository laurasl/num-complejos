#!/usr/bin/env python3

import unittest

class Complejo(object):
    def __init__(self, real, imag=0):
        self.real = real
        self.imag = imag

    def sumar(self, otro):
        result = Complejo(self.real + otro.real,
                            self.imag + otro.imag)
        return result

    def restar(self, otro):
        result = Complejo(self.real - otro.real,
                            self.imag - otro.imag)
        return result

    def multiplicar(self, otro):
        pass

    def dividir(self, otro):
        pass

    def igual(self, otro):
        return self.real == otro.real and self.imag == otro.imag 


class TestComplejo(unittest.TestCase):

    def test_sumar(self):

        c1 = Complejo(1,2)
        c2 = Complejo(3,4)

        suma = c1.sumar(c2)

        self.assertEqual(suma.real, 4)
        self.assertEqual(suma.imag, 6)

    def test_restar(self):

        c1 = Complejo(6,1)
        c2 = Complejo(8,4)

        restar = c1.restar(c2)

        self.assertEqual(restar.real, -2)
        self.assertEqual(restar.imag, -3)

    def test_multiplicar(self):
        c1 = Complejo(0,1)
        c2 = Complejo(2,5)
       
        multiplica = c1.multiplicar(c2)
       
        self.assertEqual(multiplica.real, -2)
        self.assertEqual(multiplica.imag, 7)
    

    def test_dividir(self):
        c1 = Complejo(8,9)
        c2 = Complejo(1,-5)
       
        divide = c1.dividir(c2)
       
        self.assertEqual(divide.real, float(-5/4))
        self.assertEqual(divide.imag, float(6/3))

if __name__ == "__main__":
    unittest.main()
