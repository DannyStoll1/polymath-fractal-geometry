import random
import math
import os
import ctypes
import array
random.seed()

#generalized binomial coefficients
def C(a,b):
    if(b==0|b==a):
        return 1
    elif(b==1):
        return a
    elif(b<0):
        return 0;
    else:
        product = 1;
        for i in range(b):
            product*=(a-i)
        product/=math.factorial(b)
        return product

#first digit of a number 
def ndigit(num, n):
    if(num == 0):
        return 0
    while((num<1) & (num>0)):
        num*=10
    return num // 10 ** (int(math.log(num, 10)) - n + 1)

#digits = [0 for i in range(0,10)]


#Linear Diophantine Equation Generator
def DioEquGen(d,m,n):
    #for i in range(n-1,0,-1):
        #if(i == 1):
            #print(d**(i)-1,'j',i, end = ' ')
        #else:
            #print(d**(i)-1,'j',i,'+', end = ' ')
    #print('=', m-1)

    #generate the diophantine equations and store coefficients in an array
    j = [d**(i)-1 for i in range(n,0,-1)]
    #print(j)
    return j
    #next = [d**(n)-1]
    #print(next)
    #j = next + j
    #print(j)

#range of j_i for iteration
def DioEquRange(d,m,n):
    j = DioEquGen(d,m,n)
    maxIter = [0 for i in range(n)]
    for i in range(n):
        while((maxIter[i]+1)*j[i] <= m-1):
            maxIter[i]+=1
    #print(maxIter)
    return maxIter
    


#logic to check if a given sequence is a solution
def SolnCheck(d,m,n,sequence):
    val = 0
    j = DioEquGen(d,m,n)
    for i in range(n):
        val += j[i]*sequence[i]
    success = (val == m-1)
    #print(sequence)
    #print(success)
    if(success):
        print(sequence, 'is a solution')
    return success


#iterating through n=3 case for practice, can generate the first 15 terms
def DioEquIter(d,m,n):
    j = DioEquGen(d,m,n)
    print('j =', j)
    soln=[]
    maxIter = DioEquRange(d,m,n)
    print('max', maxIter)
    print('m-1 =',m-1)
    iteration = [0 for i in range(n)]
    for z in range(maxIter[0]+1):
        for i in range(maxIter[1]+1):
            for k in range(maxIter[2]+1):
                #SolnCheck(d,m,n,iteration)
                if(SolnCheck(d,m,n,iteration)):
                    soln+=iteration
                iteration[2]+=1
            iteration[1]+=1
            iteration[2]=0
        iteration[0]+=1
        iteration[1]=0
        iteration[2]=0
    print(soln)
    print('length=', len(soln))
    print(' ')
    return soln

#formula to compute coefficients, works up to n=3, n=15
def Laurent(d,m,n):
    coeff = 0
    soln = DioEquIter(d,m,n)
    for i in range(0,len(soln)-n+1,n):
        coeff+= C((m/d**n),soln[i])*C((m/d**(n-1))-d*soln[i],soln[i+1])*C((m/d**(n-2))-(d**2)*soln[i]-d*soln[i+1],soln[i+2])
    coeff/=m
    print('coeff',m,'=', coeff)
    print(' ')

for z in range(2,16):
    Laurent(2,z,3)
