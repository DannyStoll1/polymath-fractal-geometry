#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import itertools

def logistic_map_iter(r, x=0.2, iters=1):
    for _ in range(iters):
        x = r*x*(1-x)
    return x

def logistic_map_orbit(r, x=0.2, iters=100, start=0):
    orbit = []
    for _ in range(start):
        x = r*x*(1-x)
    for _ in range(iters - start):
        x = r*x*(1-x)
        orbit.append(x)
    return orbit

def logistic_map_orbit_set(r, x=0.2, iters=100, start=50):
    orbit = set()
    for _ in range(start):
        x = r*x*(1-x)
    for _ in range(iters - start):
        x = r*x*(1-x)
        orbit.add(x)
    return orbit

def plot_iters(r, x0=0.2, iters=100, start=0):
    orbit = logistic_map_orbit(r, x=x0, iters=iters, start=start)
    plt.plot(orbit, '.:')
    plt.xlabel("Iterations")
    plt.ylabel("Value")
    plt.ylim(0,1)
    plt.show()

"""
Return the attracting orbit for values of r in a given range.

rmin:  bottom of range for r
rmax:  top of range for r
x0:    starting point for iterations; should be something generic
iters: how many iterations of computation to perform
start: drop iterations before this from the orbit
res:   number of samples for r

Outputs a pair (rs, ys) of arrays
"""
def orbit_locus(rmin=0, rmax=4, x0=0.2, iters=400, start=200, res=300):
    points = []
    for r in np.linspace(rmin, rmax, res):
        orbit = logistic_map_orbit_set(r, x=x0, iters=iters, start=start)
        points += zip(itertools.repeat(r), orbit)

    return zip(*points)

def plot_locus(rs, ys):
    plt.scatter(rs, ys, marker='.', s=1)
    plt.xlabel("r")
    plt.ylabel("Orbit")
    plt.ylim(0,1)
    plt.show()

if __name__ == "__main__":
    rs, ys = orbit_locus(
            rmin = 3.5,
            rmax = 4,
            iters = 2000,
            start = 1500,
            res = 1000)
    plot_locus(rs, ys)
    #plot_iters(r=3.9, iters=50)

