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

Note that the 0th row is a placeholder for names, specifically the data is stored in the format (index+1,Numerator,Denominator)
```

