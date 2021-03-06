#! /usr/bin/env python

import sys
from fractions import Fraction

# d = 2
class MandelbrotLaurentSeries:
    def __init__(self):
        self.b_coeffs = {}
        self.betas = {}
        
        self.a_coeffs = {
            0: Fraction(1),
            1: Fraction(0),
            2: Fraction(0),
            3: Fraction(1,2),
            4: Fraction(1,8)
        }
    
    def open_b(self, path):
        with open(path, "r") as f:
            lines = f.readlines()
            for l in lines:
                k, num, denom = list(map(int, l.split(",")))
                self.b_coeffs[k] = Fraction(num, denom)
    def open_a(self, path):
        with open(path, "r") as f:
            lines = f.readlines()
            for l in lines:
                k, num, denom = list(map(int, l.split(",")))
                if k not in self.a_coeffs.keys():
                    self.a_coeffs[k] = Fraction(num, denom)
                

    def get_beta(self, n, m):
        if (n,m) in self.betas.keys():
            return self.betas[(n,m)]

        if m == 0:
            return Fraction(1)

        # 2^(n+1)
        u = 2 << n

        if m <= u-2:
            return 0

        summands = (self.get_beta(n,k) * self.get_beta(n, m-k)
                for k in range(u-1, m-u+2)
                )

        beta = (self.get_beta(n+1,m) - sum(summands) - \
                self.get_beta(0, m-u+1)
                )/2
        self.betas[(n,m)] = beta
        return beta

    # # To Do: change to calculate alpha
    # def get_alpha(self, n, m):
    #     if (n,m) in self.alphas.keys():
    #         return self.alphas[(n,m)]

    #     if m == 0:
    #         return Fraction(1)

    #     # 2^(n+1)
    #     u = 2 << n

    #     if m <= u-2: 
    #         return 0

    #     summands = (self.get_alpha(n,k) * self.get_alpha(n, m-k)
    #             for k in range(u-1, m-u+2)
    #             )

    #     alpha = (self.get_alpha(n+1,m) - sum(summands) - \
    #             self.get_alpha(0, m-u+1)
    #             )/2

    #     self.alphas[(n,m)] = alpha
    #     return alpha

    def get_b(self, m):
        if m in self.b_coeffs.keys():
            return self.b_coeffs[m]
        b = self.get_beta(0,m)
        return b

    def get_a(self, m):
        if m in self.a_coeffs.keys():
            return self.a_coeffs[m]
        if m < 4:
            exit("m must be greater than 3")
        a = self.b_coeffs[m-2] * (-1) - sum(self.a_coeffs[j+1] * self.b_coeffs[m-j-1] for j in range(2, m-1))
        #print(f"a({m}) = {self.b_coeffs[m-2] * (-1)} - {sum(self.a_coeffs[j+1] * self.b_coeffs[m-j-1] for j in range(2, m-1))}")
        return a

    def compute_bs(self, max_power):
        for m in range(max_power):
            sys.stdout.write(f"\r{m}")
            sys.stdout.flush()
            self.b_coeffs[m] = self.get_b(m)
            if m > 1000 and m % 1024 == 0:
                with open(f"bm_coeffs_{m}_interm.csv", 'w+') as f:
                    for i in range(m):
                        bi = ser.b_coeffs[i]
                        f.write(f"{i}, {bi.numerator}, {bi.denominator}\n")
        sys.stdout.write("\r")
        sys.stdout.flush()


    def compute_as(self, max_power):
        for m in range(max_power):
            sys.stdout.write(f"\r{m}")
            sys.stdout.flush()
            self.a_coeffs[m] = self.get_a(m)
            if m > 1000 and m % 1024 == 0:
                with open(f"am_coeffs_{m}_interm.csv", 'w+') as f:
                    for i in range(m):
                        ai = ser.a_coeffs[i]
                        f.write(f"{i}, {ai.numerator}, {ai.denominator}\n")

        sys.stdout.write("\r")
        sys.stdout.flush()
    



if __name__ == '__main__':
    ser = MandelbrotLaurentSeries()
    ser.open_b("bm_coeffs_7168.csv")
    ser.open_a("am_coeffs_6144_interm.csv")
    max_power = 7168

    compute_b = True

    if compute_b:
        #ser.compute_bs(max_power)
        ser.compute_as(max_power)
        # with open(f"bm_coeffs_{max_power}.csv", 'w+') as f:
        #     for i in range(max_power):
        #         bi = ser.b_coeffs[i]
        #         f.write(f"{i}, {bi.numerator}, {bi.denominator}\n")
        with open(f"am_coeffs_{max_power}.csv", 'w+') as f:
            for i in range(max_power):
                ai = ser.a_coeffs[i]
                f.write(f"{i}, {ai.numerator}, {ai.denominator}\n")
    # else:
    #     ser.compute_as(max_power)
    #     with open(f"am_coeffs_{max_power}.txt", 'w+') as f:
    #         for i in range(max_power):
    #             ai = ser.a_coeffs[i]
    #             f.write(f"{i}, {ai.numerator}, {ai.denominator}\n")

