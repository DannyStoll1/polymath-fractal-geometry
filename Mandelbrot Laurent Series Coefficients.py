#! /usr/bin/env python

import random
import math
from math import log2
import os
import ctypes
import array
from functools import reduce
from operator import mul
from fractions import Fraction
random.seed()

#generalized binomial coefficients
def binomial_coefficient(a,b):
    if(b==0|b==a):
        return Fraction(1)
    elif(b==1):
        return Fraction(a)
    elif(b<0):
        return 0;
    else:
        return product((a-i)/(i+1) for i in range(b))

#first digit of a number 
def ndigit(num, n):
    if num == 0 :
        return 0
    elif num < 0:
        num *= -1
    while((num<1) & (num>0)):
        num*=10
    return num // 10 ** (int(math.log(num, 10)) - n + 1)


# Generate the multi indices
def gen_multi_indices(m, n, coord=0, deg=2):
    if coord == n-1:
        yield [m]
        return

    period = deg**(n-coord) - 1
    for i in range(m//period+1):
        for item in gen_multi_indices(
                m - i*period,
                n,
                coord=coord+1,
                deg=deg
                ):
            yield [i] + item

def product(arr):
    return reduce(mul, arr, 1)


class MandelbrotLaurentSeries:
    def __init__(self, degree=2):
        self.d = degree
        self.n = 0
        self.coefficients = [Fraction(0)]*degree

    # Increment n, generating the next d^n power series coefficients.
    def update(self):
        self.n += 1
        self.coefficients += [0] * (self.d**(self.n+1) - self.d**self.n)
        if self.n >= 4:
            lower = self.d**self.n
            upper = self.d*lower
            print(f"Updating max degree from {lower} to {upper}. "
                  f"This may take a while...")
            for m in range(self.d**(self.n), self.d**(self.n+1)):
                print(f"Calculated {m} of {upper} coefficients.")
                self.coefficients[m] = self.calculate_coefficient(m, self.n, self.d)
        else:
            for m in range(self.d**(self.n), self.d**(self.n+1)):
                self.coefficients[m] = self.calculate_coefficient(m, self.n, self.d)

    @staticmethod
    def calculate_coefficient(m, n, d=2):
        coeff = sum(
            0
            # product(
            #     binomial_coefficient(Fraction(m, d**(n-i)) - sum(
            #         d**(i-j) * idx[j] for j in range(i)
            #         ), idx[i])
            #     for i in range(n)
            #     )
            for idx in gen_multi_indices(m-1,n)
            )

        return coeff/m


if __name__ == '__main__':
    deg = 2
    ser = MandelbrotLaurentSeries(deg)
    for _ in range(9):
        ser.update()

    max_coeff = len(ser.coefficients)-1
    with open(f'laurent_coeffs_{deg}_{max_coeff}.csv', 'w+') as f:
        f.write("degree, numerator, denominator exponent\n")
        for m, coef in enumerate(ser.coefficients):
            a,b = coef.as_integer_ratio()
            f.write(f"{m}, {a}, {b.bit_length()-1}\n")

    # print(ser.calculate_coefficient(512, 9))
