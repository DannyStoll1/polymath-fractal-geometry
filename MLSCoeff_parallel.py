import random
import math
from math import log2
from functools import reduce
from operator import mul
from fractions import Fraction
import concurrent.futures
import time
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

    # Increment n, generating the next d^n power series coefficients for bm.and am
    def whack_a(self, arguments):
        print(f"Calculating m={arguments[0]},n={arguments[1]} coefficients.")
        return self.calculate_a_coefficient(*arguments)
    def update_generator_a(self):
        arguments = ((m, self.n, self.d) for m in range(self.d**(self.n), self.d**(self.n+1)))
        with concurrent.futures.ProcessPoolExecutor() as executor:
            return executor.map(self.whack_a, arguments)
    def update_a(self):
        self.n += 1
        self.a_coeffs += [0] * self.d**self.n
        lower = self.d**self.n
        upper = self.d*lower
        print(f"Updating max degree from {lower} to {upper}. "
                f"This may take a while...")
        result = self.update_generator_a()
        start = self.d**(self.n)
        for key, r in enumerate(result):
            self.a_coeffs[start+key] = r

    def whack_b(self, arguments):
        print(f"Calculating m={arguments[0]},n={arguments[1]} coefficients.")
        return self.calculate_b_coefficient(*arguments)
    def update_generator_b(self):
        arguments = ((m, self.n, self.d) for m in range(self.d**(self.n)-2, self.d**(self.n+1)-2))
        with concurrent.futures.ProcessPoolExecutor() as executor:
            return executor.map(self.whack_b, arguments)
    def update_b(self):
        self.n += 1
        lower = self.d**self.n
        upper = self.d*lower
        print(f"Updating max degree from {lower} to {upper}. "
                f"This may take a while...")
        result = self.update_generator_b()
        for r in result:
            self.b_coeffs.append(r)

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
        # Save intermediate results in a new file.
        #with open(f'laurent_coeffs_m={m}_bm.csv', 'w+') as f:
        #    f.write("degree, numerator, denominator exponent\n")
        #    coef = -coeff/m if m > 0  else -Fraction(1,2)
        #    a,b = coef.as_integer_ratio()
        #    f.write(f"{m}, {a}, {b.bit_length()-1}\n")

        return -coeff/m if m > 0  else -Fraction(1,2)

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

if __name__ == '__main__':
    
    start = time.time()
    deg = 2
    ser = MandelbrotLaurentSeries(deg)
    
    # Start from m=510 and move on
    # ser.n = 8
    # ser.update_b()

    # Calculate first few coefficients for bm
    # for _ in range(5):
    #     ser.update_b()
    # end = time.time()
    # print(f"time = {end-start} sec")

    # max_bm = len(ser.b_coeffs)-1
    # with open(f'laurent_coeffs_bm_{deg}_{max_bm}_parallel.csv', 'w+') as f:
    #     f.write("degree, numerator, denominator exponent\n")
    #     for m, coef in enumerate(ser.b_coeffs):
    #         a,b = coef.as_integer_ratio()
    #         f.write(f"{m}, {a}, {b.bit_length()-1}\n")
    
    # Calculate first few coefficients for am
    for _ in range(5):
        ser.update_a()
    end = time.time()
    print(f"time = {end-start} sec")

    max_am = len(ser.a_coeffs)-1
    with open(f'laurent_coeffs_am_{deg}_{max_am}_parallel.csv', 'w+') as f:
        f.write("degree, numerator, denominator exponent\n")
        for m, coef in enumerate(ser.a_coeffs):
            a,b = coef.as_integer_ratio()
            f.write(f"{m}, {a}, {b.bit_length()-1}\n")