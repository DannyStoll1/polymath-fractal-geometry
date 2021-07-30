#! /usr/bin/env python

from math import ceil, log10, cos, sin, tan, sqrt, pi
from fractions import Fraction
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
from matplotlib import cm
from matplotlib.lines import Line2D

class Lamination:
    def __init__(self, period=1, degree=2):
        self.degree = degree

        self.max_period = 1
        self.size = 1

        # Maintain list of arcs of form (id, angle1, angle2)
        self.arcs = [ (0, Fraction(0,1), Fraction(0,1)) ]
        self.endpoints = {Fraction(0,1)}

        self.period_cutoffs = [0,1]

        self.extend_to_period(period)

    # Add in arcs of next period
    def extend(self):
        self.max_period = p = self.max_period + 1
        n = self.degree**p - 1

        counters = [0] * n

        for k in range(n):
            # Ignore arcs that have already been drawn
            if Fraction(k,n) in self.endpoints:
                counters[k] = -1

        for (id, a, b) in self.arcs:
            for k in range(ceil(n*a), ceil(n*b)):
                if counters[k] != -1:
                    counters[k] ^= (1<<id)
        
        angles = {}

        it = enumerate(counters)
        next(it)

        for k, counter in it:
            if counter == -1:
                continue

            if counter in angles.keys():
                id = self.size
                self.arcs.append((id, angles[counter], Fraction(k,n)))
                self.size += 1
                self.endpoints.add(angles[counter])
                self.endpoints.add(Fraction(k, n))
                del angles[counter]
            else:
                angles[counter] = Fraction(k,n)

        self.period_cutoffs.append(self.size)

    def __len__(self):
        return self.size

    def extend_to_period(self, per):
        for _ in range(self.max_period, per):
            self.extend()

    def arcs_of_period(self, per=1, sort=False):
        i = self.period_cutoffs[per-1]
        j = self.period_cutoffs[per]
        out = [(a,b) for _,a,b in self.arcs[i:j]]

        if sort:
            out.sort()

        return out

    def arc_lengths_of_period(self, per=1):
        i = self.period_cutoffs[per-1]
        j = self.period_cutoffs[per]
        return [b-a for _,a,b in self.arcs[i:j]]

    def arc_lengths_cumulative(self, max_per=-1):
        j = self.period_cutoffs[max_per]
        return [b-a for _,a,b in self.arcs[:j]]

    def arc_lengths_cumulative_set(self, max_per=-1):
        j = self.period_cutoffs[max_per]
        return {b-a for _,a,b in self.arcs[:j]}

    def draw(self, max_period = None):
        if max_period is None or max_period >= self.max_period:
            max_period = self.max_period

        fig, ax = plt.subplots()

        ax.set_xlim(-1.4,1.4)
        ax.set_ylim(-1.1,1.1)
        ax.set_aspect(1)
        ax.axis('off')

        def draw_arc(a, b, color='blue', lw=1):
            u = 2*pi*a
            v = 2*pi*b

            # center of arc
            x = (sin(u)-sin(v))/sin(u-v)
            y = (cos(v)-cos(u))/sin(u-v)

            r = tan((v-u)/2)

            start = v*180/pi + 90
            end   = u*180/pi + 270
            arc = Arc(
                    [x,y],
                    2*r,2*r,
                    angle = 0,
                    theta1 = start,
                    theta2 = end,
                    color = color,
                    lw = lw)
            ax.add_patch(arc)

        disk = plt.Circle((0,0), 1, fill=False)
        ax.add_artist(disk)

        cmap = cm.get_cmap("Set1", max_period)

        for p in reversed(range(1, max_period)):
            i = self.period_cutoffs[p]
            j = self.period_cutoffs[p+1]
            color = cmap((p-1)/max_period)
            
            for _,a,b in self.arcs[i:j]:
                draw_arc(a,b,
                        color=color,
                        lw = max_period / (2*p+3))
        p = max_period
        i = self.period_cutoffs[p]
        color = cmap((p-1)/max_period)
        
        for _,a,b in self.arcs[i:]:
            draw_arc(a,b,
                    color=color,
                    lw = max_period / (2*p+3))

        legend_icons = [
                Line2D([0], [0], color=cmap((p-2)/max_period), lw=4)
                for p in range(2, max_period+1)]
        legend_labels = [
                f"Period {i}"
                for i in range(2,max_period+1)]
        ax.legend(legend_icons, legend_labels, loc='upper right',
                fontsize='x-small')

        plt.title(f"Mandelbrot lamination up to period {max_period}")
        plt.savefig(f"lamination_{max_period}.png", dpi=300)
        plt.show()
        
if __name__ == '__main__':
    lam = Lamination(14)

    arc_length_first_digits = [x//10**int(log10(x)-1)
            for x in lam.arc_lengths_cumulative_set() if x != 0]
    plt.hist(arc_length_first_digits, bins=9)
    plt.show()

    lam.draw(9)
