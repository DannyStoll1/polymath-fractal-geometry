import random
import math
import os
from fractions import Fraction as frac
import ctypes
import array
from decimal import *
getcontext().prec=30
random.seed()
from functools import reduce
from operator import mul
from fractions import Fraction
from math import log2


#generalized binomial coefficients
def C(a,b):
    if(b==0|b==a):
        return Fraction(1)
    elif(b==1):
        return Fraction(a)
    elif(b<0):
        return 0
    else:
        return math.prod((a-i)/(i+1) for i in range(b))

#first digit of a number 
def ndigit(num, n):
    if(num<0):
        num*=-1
    elif(num == 0):
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
    #if(success):
        #print(sequence, 'is a solution')
    return success


#iterating through the data works up to n=10
#fix all the other j_i then solve explicitly for the last one
def DioEquIter(d,m,n):
    j = DioEquGen(d,m,n)
    print('j =', j)
    soln=[]
    maxIter = DioEquRange(d,m,n)
    #print('max', maxIter)
    #print('m-1 =',m-1)
    iteration = [0 for i in range(n)]
    val = 0


    if(n==1):
        for b in range(len(iteration)-1):
            val += iteration[b]*j[b]
        iteration[n-1] = m-1-val
        if(iteration[n-1]<0):
            val = 0
            #break
        else:
            val = 0

    elif(n==2):
        for i in range(maxIter[0]+1):
            for b in range(len(iteration)-1):
                    val += iteration[b]*j[b]
            iteration[n-1] = m-1-val
            if(iteration[n-1]<0):
                val = 0
                break
            else:
                val = 0
            iteration[0]+=1
            iteration[1]=0


    elif(n==3):
        for z in range(maxIter[0]+1):
            for i in range(maxIter[1]+1):
                for b in range(len(iteration)-1):
                    val += iteration[b]*j[b]
                iteration[n-1] = m-1-val
                if(iteration[n-1]<0):
                    val = 0
                    break
                else:
                    val = 0
                    soln+=iteration
                iteration[1]+=1
                iteration[2]=0
            iteration[0]+=1
            iteration[1]=0
            iteration[2]=0

    elif(n==4):
        for r in range(maxIter[0]+1):
            for z in range(maxIter[1]+1):
                for i in range(maxIter[2]+1):
                    for b in range(len(iteration)-1):
                        val += iteration[b]*j[b]
                    iteration[n-1] = m-1-val
                    if(iteration[n-1]<0):
                        val = 0
                        break
                    else:
                        val = 0
                        soln+=iteration
                    iteration[2]+=1
                    iteration[3]=0
                iteration[1]+=1
                iteration[2]=0
                iteration[3]=0
            iteration[0]+=1
            iteration[1]=0
            iteration[2]=0
            iteration[3]=0

    elif(n==5):
        for t in range(maxIter[0]+1):
            for r in range(maxIter[1]+1):
                for z in range(maxIter[2]+1):
                    for i in range(maxIter[3]+1):
                        for b in range(len(iteration)-1):
                            val += iteration[b]*j[b]
                        iteration[n-1] = m-1-val
                        if(iteration[n-1]<0):
                            val = 0
                            break
                        else:
                            val = 0
                            soln+=iteration
                        iteration[3]+=1
                        iteration[4]=0
                    iteration[2]+=1
                    iteration[3]=0
                    iteration[4]=0
                iteration[1]+=1
                iteration[2]=0
                iteration[3]=0
                iteration[4]=0
            iteration[0]+=1
            iteration[1]=0
            iteration[2]=0
            iteration[3]=0
            iteration[4]=0

    elif(n==6):
        for p in range(maxIter[0]+1):
            for t in range(maxIter[1]+1):
                for r in range(maxIter[2]+1):
                    for z in range(maxIter[3]+1):
                        for i in range(maxIter[4]+1):
                            for b in range(len(iteration)-1):
                                val += iteration[b]*j[b]
                            iteration[n-1] = m-1-val
                            if(iteration[n-1]<0):
                                val = 0
                                break
                            else:
                                val = 0
                                soln+=iteration
                            iteration[4]+=1
                            iteration[5]=0
                        iteration[3]+=1
                        iteration[4]=0
                        iteration[5]=0
                    iteration[2]+=1
                    iteration[3]=0
                    iteration[4]=0
                    iteration[5]=0
                iteration[1]+=1
                iteration[2]=0
                iteration[3]=0
                iteration[4]=0
                iteration[5]=0
            iteration[0]+=1
            iteration[1]=0
            iteration[2]=0
            iteration[3]=0
            iteration[4]=0
            iteration[5]=0



    elif(n==7):
        for s in range(maxIter[0]+1):
            for p in range(maxIter[1]+1):
                for t in range(maxIter[2]+1):
                    for r in range(maxIter[3]+1):
                        for z in range(maxIter[4]+1):
                            for i in range(maxIter[5]+1):
                                for b in range(len(iteration)-1):
                                    val += iteration[b]*j[b]
                                iteration[n-1] = m-1-val
                                if(iteration[n-1]<0):
                                    val = 0
                                    break
                                else:
                                    val = 0
                                    soln+=iteration
                                iteration[5]+=1
                                iteration[6]=0
                            iteration[4]+=1
                            iteration[5]=0
                            iteration[6]=0
                        iteration[3]+=1
                        iteration[4]=0
                        iteration[5]=0
                        iteration[6]=0
                    iteration[2]+=1
                    iteration[3]=0
                    iteration[4]=0
                    iteration[5]=0
                    iteration[6]=0
                iteration[1]+=1
                iteration[2]=0
                iteration[3]=0
                iteration[4]=0
                iteration[5]=0
                iteration[6]=0
            iteration[0]+=1
            iteration[1]=0
            iteration[2]=0
            iteration[3]=0
            iteration[4]=0
            iteration[5]=0
            iteration[6]=0

    elif(n==8):
        for p in range(maxIter[0]+1):
            for s in range(maxIter[1]+1):
                for p in range(maxIter[2]+1):
                    for t in range(maxIter[3]+1):
                        for r in range(maxIter[4]+1):
                            for z in range(maxIter[5]+1):
                                for i in range(maxIter[6]+1):
                                    for b in range(len(iteration)-1):
                                        val += iteration[b]*j[b]
                                    iteration[n-1] = m-1-val
                                    if(iteration[n-1]<0):
                                        val = 0
                                        break
                                    else:
                                        val = 0
                                        soln+=iteration
                                    iteration[6]+=1
                                    iteration[7]=0
                                iteration[5]+=1
                                iteration[6]=0
                                iteration[7]=0
                            iteration[4]+=1
                            iteration[5]=0
                            iteration[6]=0
                            iteration[7]=0
                        iteration[3]+=1
                        iteration[4]=0
                        iteration[5]=0
                        iteration[6]=0
                        iteration[7]=0
                    iteration[2]+=1
                    iteration[3]=0
                    iteration[4]=0
                    iteration[5]=0
                    iteration[6]=0
                    iteration[7]=0
                iteration[1]+=1
                iteration[2]=0
                iteration[3]=0
                iteration[4]=0
                iteration[5]=0
                iteration[6]=0
                iteration[7]=0
            iteration[0]+=1
            iteration[1]=0
            iteration[2]=0
            iteration[3]=0
            iteration[4]=0
            iteration[5]=0
            iteration[6]=0
            iteration[7]=0


    elif(n==9):
        for g in range(maxIter[0]+1):
            for p in range(maxIter[1]+1):
                for s in range(maxIter[2]+1):
                    for p in range(maxIter[3]+1):
                        for t in range(maxIter[4]+1):
                            for r in range(maxIter[5]+1):
                                for z in range(maxIter[6]+1):
                                    for i in range(maxIter[7]+1):
                                        for b in range(len(iteration)-1):
                                            val += iteration[b]*j[b]
                                        iteration[n-1] = m-1-val
                                        if(iteration[n-1]<0):
                                            val = 0
                                            break
                                        else:
                                            val = 0
                                            soln+=iteration
                                        iteration[7]+=1
                                        iteration[8]=0
                                    iteration[6]+=1
                                    iteration[7]=0
                                    iteration[8]=0
                                iteration[5]+=1
                                iteration[6]=0
                                iteration[7]=0
                                iteration[8]=0
                            iteration[4]+=1
                            iteration[5]=0
                            iteration[6]=0
                            iteration[7]=0
                            iteration[8]=0
                        iteration[3]+=1
                        iteration[4]=0
                        iteration[5]=0
                        iteration[6]=0
                        iteration[7]=0
                        iteration[8]=0
                    iteration[2]+=1
                    iteration[3]=0
                    iteration[4]=0
                    iteration[5]=0
                    iteration[6]=0
                    iteration[7]=0
                    iteration[8]=0
                iteration[1]+=1
                iteration[2]=0
                iteration[3]=0
                iteration[4]=0
                iteration[5]=0
                iteration[6]=0
                iteration[7]=0
                iteration[8]=0
            iteration[0]+=1
            iteration[1]=0
            iteration[2]=0
            iteration[3]=0
            iteration[4]=0
            iteration[5]=0
            iteration[6]=0
            iteration[7]=0
            iteration[8]=0


    elif(n==10):
        for h in range(maxIter[0]+1):
            for g in range(maxIter[1]+1):
                for p in range(maxIter[2]+1):
                    for s in range(maxIter[3]+1):
                        for p in range(maxIter[4]+1):
                            for t in range(maxIter[5]+1):
                                for r in range(maxIter[6]+1):
                                    for z in range(maxIter[7]+1):
                                        for i in range(maxIter[8]+1):
                                            for b in range(len(iteration)-1):
                                                val += iteration[b]*j[b]
                                            iteration[n-1] = m-1-val
                                            if(iteration[n-1]<0):
                                                val = 0
                                                break
                                            else:
                                                val = 0
                                                soln+=iteration
                                            iteration[8]+=1
                                            iteration[9]=0
                                        iteration[7]+=1
                                        iteration[8]=0
                                        iteration[9]=0
                                    iteration[6]+=1
                                    iteration[7]=0
                                    iteration[8]=0
                                    iteration[9]=0
                                iteration[5]+=1
                                iteration[6]=0
                                iteration[7]=0
                                iteration[8]=0
                                iteration[9]=0
                            iteration[4]+=1
                            iteration[5]=0
                            iteration[6]=0
                            iteration[7]=0
                            iteration[8]=0
                            iteration[9]=0
                        iteration[3]+=1
                        iteration[4]=0
                        iteration[5]=0
                        iteration[6]=0
                        iteration[7]=0
                        iteration[8]=0
                        iteration[9]=0
                    iteration[2]+=1
                    iteration[3]=0
                    iteration[4]=0
                    iteration[5]=0
                    iteration[6]=0
                    iteration[7]=0
                    iteration[8]=0
                    iteration[9]=0
                iteration[1]+=1
                iteration[2]=0
                iteration[3]=0
                iteration[4]=0
                iteration[5]=0
                iteration[6]=0
                iteration[7]=0
                iteration[8]=0
                iteration[9]=0
            iteration[0]=0
            iteration[1]=0
            iteration[2]=0
            iteration[3]=0
            iteration[4]=0
            iteration[5]=0
            iteration[6]=0
            iteration[7]=0
            iteration[8]=0
            iteration[9]=0




    

        #else:
            #print('error not defined')
            #return 0


    #print(soln)
    #print('length=', len(soln))
    #print(' ')
    return soln

#formula to compute coefficients, just expanded by hand each time (useful as a control?)
def Laurent(d,m,n,matrixSoln):
    coeff = 0
    #soln = DioEquIter(d,m,n)

    if(n==1):
        i = 0
        for k in range(len(matrixSoln)):
            soln = matrixSoln[k]
            #print('solution passed:', soln)
            coeff+= C((m/d**n),soln[i])

    elif(n==2):
        i = 0
        for k in range(len(matrixSoln)):
            soln = matrixSoln[k]
            #print('solution passed:', soln)
            coeff+= C((m/d**n),soln[i])*C((m/d**(n-1))-(d**1)*soln[i],soln[i+1])
    
    elif(n==3):
        i = 0
        for k in range(len(matrixSoln)):
            soln = matrixSoln[k]
            #print('solution passed:', soln)
            coeff+= C((m/d**n),soln[i])*C((m/d**(n-1))-(d**1)*soln[i],soln[i+1])*C((m/d**(n-2))-(d**2)*soln[i]-d*soln[i+1],soln[i+2])

    elif(n==4):
        i = 0
        for k in range(len(matrixSoln)):
            soln = matrixSoln[k]
            #print('solution passed:', soln)
            coeff+= C((m/d**n),soln[i])*C((m/d**(n-1))-(d**1)*soln[i],soln[i+1])*C((m/d**(n-2))-(d**2)*soln[i]-d*soln[i+1],soln[i+2])*C((m/d**(n-3))-(d**3)*soln[i]-(d**2)*soln[i+1]-(d**1)*soln[i+2],soln[i+3])

    elif(n==5):
        i = 0
        for k in range(len(matrixSoln)):
            soln = matrixSoln[k]
            #print('solution passed:', soln)
            coeff+= C((m/d**n),soln[i])*C((m/d**(n-1))-(d**1)*soln[i],soln[i+1])*C((m/d**(n-2))-(d**2)*soln[i]-d*soln[i+1],soln[i+2])*C((m/d**(n-3))-(d**3)*soln[i]-(d**2)*soln[i+1]-(d**1)*soln[i+2],soln[i+3])*C((m/d**(n-4))-(d**4)*soln[i]-(d**3)*soln[i+1]-(d**2)*soln[i+2]-(d**1)*soln[i+3],soln[i+4])

    elif(n==6):
        i = 0
        for k in range(len(matrixSoln)):
            soln = matrixSoln[k]
            #print('solution passed:', soln)
            coeff+= C((m/d**n),soln[i])*C((m/d**(n-1))-(d**1)*soln[i],soln[i+1])*C((m/d**(n-2))-(d**2)*soln[i]-d*soln[i+1],soln[i+2])*C((m/d**(n-3))-(d**3)*soln[i]-(d**2)*soln[i+1]-(d**1)*soln[i+2],soln[i+3])*C((m/d**(n-4))-(d**4)*soln[i]-(d**3)*soln[i+1]-(d**2)*soln[i+2]-(d**1)*soln[i+3],soln[i+4])*C((m/d**(n-5))-(d**5)*soln[i]-(d**4)*soln[i+1]-(d**3)*soln[i+2]-(d**2)*soln[i+3]-(d**1)*soln[i+4],soln[i+5])

    elif(n==7):
        i = 0
        for k in range(len(matrixSoln)):
            soln = matrixSoln[k]
            #print('solution passed:', soln)
            coeff+= C((m/d**n),soln[i])*C((m/d**(n-1))-(d**1)*soln[i],soln[i+1])*C((m/d**(n-2))-(d**2)*soln[i]-d*soln[i+1],soln[i+2])*C((m/d**(n-3))-(d**3)*soln[i]-(d**2)*soln[i+1]-(d**1)*soln[i+2],soln[i+3])*C((m/d**(n-4))-(d**4)*soln[i]-(d**3)*soln[i+1]-(d**2)*soln[i+2]-(d**1)*soln[i+3],soln[i+4])*C((m/d**(n-5))-(d**5)*soln[i]-(d**4)*soln[i+1]-(d**3)*soln[i+2]-(d**2)*soln[i+3]-(d**1)*soln[i+4],soln[i+5])*C((m/d**(n-6))-(d**6)*soln[i]-(d**5)*soln[i+1]-(d**4)*soln[i+2]-(d**3)*soln[i+3]-(d**2)*soln[i+4]-(d**1)*soln[i+5],soln[i+6])

    elif(n==8):
        i = 0
        for k in range(len(matrixSoln)):
            soln = matrixSoln[k]
            #print('solution passed:', soln)
            coeff+= C((m/d**n),soln[i])*C((m/d**(n-1))-(d**1)*soln[i],soln[i+1])*C((m/d**(n-2))-(d**2)*soln[i]-d*soln[i+1],soln[i+2])*C((m/d**(n-3))-(d**3)*soln[i]-(d**2)*soln[i+1]-(d**1)*soln[i+2],soln[i+3])*C((m/d**(n-4))-(d**4)*soln[i]-(d**3)*soln[i+1]-(d**2)*soln[i+2]-(d**1)*soln[i+3],soln[i+4])*C((m/d**(n-5))-(d**5)*soln[i]-(d**4)*soln[i+1]-(d**3)*soln[i+2]-(d**2)*soln[i+3]-(d**1)*soln[i+4],soln[i+5])*C((m/d**(n-6))-(d**6)*soln[i]-(d**5)*soln[i+1]-(d**4)*soln[i+2]-(d**3)*soln[i+3]-(d**2)*soln[i+4]-(d**1)*soln[i+5],soln[i+6])*C((m/d**(n-7))-(d**7)*soln[i]-(d**6)*soln[i+1]-(d**5)*soln[i+2]-(d**4)*soln[i+3]-(d**3)*soln[i+4]-(d**2)*soln[i+5]-(d**1)*soln[i+6],soln[i+7])


    elif(n==9):
        i = 0
        for k in range(len(matrixSoln)):
            soln = matrixSoln[k]
            #print('solution passed:', soln)
            coeff+= C((m/d**n),soln[i])*C((m/d**(n-1))-(d**1)*soln[i],soln[i+1])*C((m/d**(n-2))-(d**2)*soln[i]-d*soln[i+1],soln[i+2])*C((m/d**(n-3))-(d**3)*soln[i]-(d**2)*soln[i+1]-(d**1)*soln[i+2],soln[i+3])*C((m/d**(n-4))-(d**4)*soln[i]-(d**3)*soln[i+1]-(d**2)*soln[i+2]-(d**1)*soln[i+3],soln[i+4])*C((m/d**(n-5))-(d**5)*soln[i]-(d**4)*soln[i+1]-(d**3)*soln[i+2]-(d**2)*soln[i+3]-(d**1)*soln[i+4],soln[i+5])*C((m/d**(n-6))-(d**6)*soln[i]-(d**5)*soln[i+1]-(d**4)*soln[i+2]-(d**3)*soln[i+3]-(d**2)*soln[i+4]-(d**1)*soln[i+5],soln[i+6])*C((m/d**(n-7))-(d**7)*soln[i]-(d**6)*soln[i+1]-(d**5)*soln[i+2]-(d**4)*soln[i+3]-(d**3)*soln[i+4]-(d**2)*soln[i+5]-(d**1)*soln[i+6],soln[i+7])*C((m/d**(n-8))-(d**8)*soln[i]-(d**7)*soln[i+1]-(d**6)*soln[i+2]-(d**5)*soln[i+3]-(d**4)*soln[i+4]-(d**3)*soln[i+5]-(d**2)*soln[i+6]-(d**1)*soln[i+7],soln[i+8])

    elif(n==10):
        i = 0
        for k in range(len(matrixSoln)):
            soln = matrixSoln[k]
            #print('solution passed:', soln)
            coeff+= C((m/d**n),soln[i])*C((m/d**(n-1))-(d**1)*soln[i],soln[i+1])*C((m/d**(n-2))-(d**2)*soln[i]-d*soln[i+1],soln[i+2])*C((m/d**(n-3))-(d**3)*soln[i]-(d**2)*soln[i+1]-(d**1)*soln[i+2],soln[i+3])*C((m/d**(n-4))-(d**4)*soln[i]-(d**3)*soln[i+1]-(d**2)*soln[i+2]-(d**1)*soln[i+3],soln[i+4])*C((m/d**(n-5))-(d**5)*soln[i]-(d**4)*soln[i+1]-(d**3)*soln[i+2]-(d**2)*soln[i+3]-(d**1)*soln[i+4],soln[i+5])*C((m/d**(n-6))-(d**6)*soln[i]-(d**5)*soln[i+1]-(d**4)*soln[i+2]-(d**3)*soln[i+3]-(d**2)*soln[i+4]-(d**1)*soln[i+5],soln[i+6])*C((m/d**(n-7))-(d**7)*soln[i]-(d**6)*soln[i+1]-(d**5)*soln[i+2]-(d**4)*soln[i+3]-(d**3)*soln[i+4]-(d**2)*soln[i+5]-(d**1)*soln[i+6],soln[i+7])*C((m/d**(n-8))-(d**8)*soln[i]-(d**7)*soln[i+1]-(d**6)*soln[i+2]-(d**5)*soln[i+3]-(d**4)*soln[i+4]-(d**3)*soln[i+5]-(d**2)*soln[i+6]-(d**1)*soln[i+7],soln[i+8])*C((m/d**(n-9))-(d**9)*soln[i]-(d**8)*soln[i+1]-(d**7)*soln[i+2]-(d**6)*soln[i+3]-(d**5)*soln[i+4]-(d**4)*soln[i+5]-(d**3)*soln[i+6]-(d**2)*soln[i+7]-(d**1)*soln[i+8],soln[i+9])

    
    else:
        print('error, not defined')
        return 0

    coeff/=m
    print('coeff', m,'=',coeff)
    print('first digit:', ndigit(coeff,1))
    return int(ndigit(coeff,1))
    #print(coeff)
    print(' ')


#calculate the highest coefficient m for degree n then decrement to get all lower m
#calculates down to m=2
#also stores first digit in an array
def TopDownCalc(d,m,n):
    soln = DioEquIter(d,m,n)
    matrixSoln = []
    firstDigit = [0 for i in range(10)]
    k = 0
    for i in range(0,len(soln),n):
        matrixSoln += [[soln[k+i] for i in range(n)]]
        k+=n

    
    for p in range(n,0,-1):
        for c in range(2**(p+1)-1,2**(p)-1,-1):
            marker = []
            l = len(matrixSoln)
            #print('length =',l)
            #print(matrixSoln)
            firstDigit[Laurent(d,c,p,matrixSoln)]+=1
            for i in range(l):
                if(matrixSoln[i][p-1]==0):
                    marker+=[i]
                else:
                    matrixSoln[i][p-1]-=1

            for i in range(len(marker)):
                del matrixSoln[marker[i]-i]

        for i in range(len(matrixSoln)):
            del matrixSoln[i][0]
        #print(matrixSoln)
        print(firstDigit)


    """
    for c in range(2**(n+1)-1,2**(n)-1,-1):
        marker = []
        l = len(matrixSoln)
        print('length =',l)
        print(matrixSoln)
        Laurent(d,c,n,matrixSoln)
        for i in range(l):
            if(matrixSoln[i][n-1]==0):
                marker+=[i]
            else:
                matrixSoln[i][n-1]-=1

        for i in range(len(marker)):
            del matrixSoln[marker[i]-i]

    for i in range(len(matrixSoln)):
        del matrixSoln[i][0]
    print(matrixSoln)
"""
       


d = 2
n = 8
#for n in range(1,4):
    #for m in range(2**n,2**(n+1)):
        #Laurent(d,m,n)
#Laurent(2,15,3)
TopDownCalc(d,d**(n+1)-1,n)


