#! /usr/bin/env python
import numpy as np
import pandas as pd
from math import log, exp
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

if __name__ == '__main__':
    data = pd.read_csv("laurent_coeffs_2_511.csv", sep=',\s+')
    odd_numerators = data['numerator'][1::2]
    even_numerators = data['numerator'][::2]
    
    model = LinearRegression()

    start_idx = 120

    x = np.reshape(odd_numerators.index[start_idx:], (-1,1))
    y = [[log(abs(int(a)))] for a in odd_numerators.values[start_idx:]]
    model.fit(x,y)

    score = model.score(x,y)

    slope = model.coef_[0][0]
    intercept = model.intercept_[0]

    print("Slope: {}\nIntercept: {}".format(slope, intercept))
    print(f"Exp growth rate: {exp(slope)}")


    # plt.loglog(even_numerators)
    # plt.show()
