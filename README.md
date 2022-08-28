# Polymath: Benford's Law and Fractal Geometry
## Introduction

Calculating the coeﬀicients of the Riemann mapping function for the exterior of the Mandelbrot set to the closed unit disk.



## Compute Coefficients

To compute am and bm coefficients of the Laurent series of the Riemann mapping function, use **codes/coeff_compute.py**

For example, to compute the first 7168 coefficients for both am and bm

```
$ python codes/coeff_compute.py --max_power 7168
```

Results will be saved in the same folder with names "am_coeffs_7168.csv" and "bm_coeffs_7168.csv." Intermediate results will also be saved for every 1024 coefficients.



If existing am and/or bm coefficients are computed, we can load coefficients from existing files (say bm_coeffs_1024.csv and am_coeffs_1024.csv)

```
$ python codes/coeff_compute.py --max_power 7168 --load_bm "bm_coeffs_1024.csv" --load_am "am_coeffs_1024.csv"

```

## Sampling simulation

To conduct simulations to see sampling error, use **Data Analysis/sampling_simulation.ipynb**


## Test Statistics and Power Computation

We provide two jupyter notebooks for computing chi-square test statistics and draw all plots in our work. 
They are named as **amChiSquareData.ipynb** and **bmChiSquareData.ipynb**.

For results related to log base 10 modulo 1, please refer to **amLogData.ipynb** and **bmLogData.ipynb**.

To compute the power of each tests, we provide a Excel sheet and instructions to compute the power inside the sheet.
There are also equivalent chi-square test statistics for cross-checking.

For example, to compute the power of a test with 0.05 significance level with degree of freedom equals 8, we can use the 
following R command (lambda should be substituted with the value automatically computed on the Excel sheet).

'''
1 - qchisq(.95, 8), 8, lambda)
'''

To conduct simulations to see sampling error, use **Data Analysis/sampling_simulation.ipynb**