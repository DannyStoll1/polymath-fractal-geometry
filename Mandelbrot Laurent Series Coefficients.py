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
        return 0
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
def gen_multi_indices(m_minus_one, n, coord=0, deg=2):
    if coord == n-1:
        yield [m_minus_one]
        return

    period = deg**(n-coord) - 1
    for i in range(m_minus_one//period+1):
        for item in gen_multi_indices(
                m_minus_one - i*period,
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
        self.a_coeffs = [Fraction(0)]*degree
        self.b_coeffs = []#[Fraction(0)]*degree

    # Increment n, generating the next d^n power series coefficients a_m.
    def update_a(self):
        self.n += 1
        self.a_coeffs += [0] * (self.d**(self.n+1) - self.d**self.n)
        if self.n >= 4:
            lower = self.d**self.n
            upper = self.d*lower
            print(f"Updating max degree from {lower} to {upper}. "
                  f"This may take a while...")
            for m in range(self.d**(self.n), self.d**(self.n+1)):
                print(f"Calculated {m} of {upper} coefficients.")
                self.a_coeffs[m] = self.calculate_a_coefficient(m, self.n, self.d)
        else:
            for m in range(self.d**(self.n), self.d**(self.n+1)):
                self.a_coeffs[m] = self.calculate_a_coefficient(m, self.n, self.d)

    # Increment n, generating the next d^n Laurent series coefficients b_m.
    def update_b(self):
        self.n += 1
        self.b_coeffs += [0] * (self.d**(self.n+1) - self.d**self.n)
        if self.n >= 4:
            lower = self.d**self.n
            upper = self.d*lower
            print(f"Updating max degree from {lower} to {upper}. "
                  f"This may take a while...")
            for m in range(self.d**(self.n)-2, self.d**(self.n+1)-2):
                print(f"Calculated {m} of {upper} coefficients.")
                self.b_coeffs[m] = self.calculate_b_coefficient(m, self.n, self.d)
        else:
            for m in range(self.d**(self.n)-2, self.d**(self.n+1)-2):
                self.b_coeffs[m] = self.calculate_b_coefficient(m, self.n, self.d)

    @staticmethod
    def calculate_a_coefficient(m, n, d=2):
        coeff = sum(
            product(
                binomial_coefficient(Fraction(m, d**(n-i)) - sum(
                    d**(i-j) * idx[j] for j in range(i)
                    ), idx[i])
                for i in range(n)
                )
            for idx in gen_multi_indices(m-1,n,deg=d)
            )

        return coeff/m

    @staticmethod
    def calculate_b_coefficient(m, n, d=2):
        coeff = sum(
            product(
                binomial_coefficient(Fraction(m, d**(n-i)) - sum(
                    d**(i-j) * idx[j] for j in range(i)
                    ), idx[i])
                for i in range(n)
                )
            for idx in gen_multi_indices(m+1,n,deg=d)
            )

        return -coeff/m if m > 0  else -Fraction(1,2)


if __name__ == '__main__':
    deg = 2
    ser = MandelbrotLaurentSeries(deg)

    for _ in range(7):
        ser.update_b()

    max_bm = len(ser.b_coeffs)-1

    with open(f'laurent_coeffs_bm_{deg}_{max_bm}.csv', 'w+') as f:
        f.write("degree, numerator, denominator exponent\n")
        for m, coef in enumerate(ser.b_coeffs):
            a,b = coef.as_integer_ratio()
            f.write(f"{m}, {a}, {b.bit_length()-1}\n")

    # for m,coef in enumerate(ser.a_coeffs):
    #     a,b = coef.as_integer_ratio()
    #     print(f"{m}, {a}, {b.bit_length()-1}")
