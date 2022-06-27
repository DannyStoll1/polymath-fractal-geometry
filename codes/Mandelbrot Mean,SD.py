import os
import csv
import math
import statistics

#first digit of a number 
def digit(num, n=1):
    if(num<0):
        num*=-1
    elif(num == 0):
        return 0
    while((num<1) & (num>0)):
        num*=10
    return num // 10 ** (int(math.log(num, 10)) - n + 1)


def ChiSquVal(expec,obs):
    if(len(expec) != len(obs)):
        print('error, lists not the same size')
        return
    sum = 0
    for j in range(len(expec)):
        if(expec[j] == 0):
            continue
        sum += (expec[j]-obs[j])**2/expec[j]
    return sum


        

file_to_open = os.path.expanduser('~/Desktop/Coding Text Files/laurent_coeffs_bm_2_1021.csv')
file = open(file_to_open)
type(file)
csvreader=csv.reader(file)
header = []
header = next(csvreader)
print(header)

rows = []
for row in csvreader:
    rows.append(row)
#0 is degree
#1 is numerator
#2 is the exponent of the denominator
print(rows[0])

numel = len(rows)

Benford = []
for i in range(numel):
    Benford.append([i*math.log10(1),i*math.log10(2/1),i*math.log10(3/2),i*math.log10(4/3),i*math.log10(5/4),i*math.log10(6/5),i*math.log10(7/6),i*math.log10(8/7),i*math.log10(9/8),i*math.log10(10/9)])
print(Benford[20])

a = 0
d = 0
m = 0
sd = 0
LogNum = []
for i in range(numel):
    a = abs(int(rows[i][1]))
    if(a == 0):
        continue
    d = math.log10(a)
    LogNum.append(d)
print('LogNum =', LogNum)
m = sum(LogNum);
m /= len(LogNum)
print('the mean is: ', m)
sd = statistics.pstdev(LogNum)
print('the sd is:', sd)



a = 0
d = 0
m = 0
sd = 0
LogDen = []
for i in range(numel):
    a = 2**int(rows[i][2])
    d = math.log10(a)
    LogDen.append(d)
print('LogDen =', LogDen)
m = sum(LogDen);
m /= len(LogDen)
print('the mean is: ', m)
sd = statistics.pstdev(LogDen)
print('the sd is:', sd)


q = 0
r = 0
a = 0
d = 0
m = 0
sd = 0
LogDec = []
for i in range(numel):
    q = abs(int(rows[i][1]))
    if(q == 0):
        continue
    r = 2**int(rows[i][2])
    a = q/r
    d = math.log10(a)
    LogDec.append(d)
print('LogDec =', LogDec)
m = sum(LogDec);
m /= len(LogDec)
print('the mean is: ', m)
sd = statistics.pstdev(LogDec)
print('the sd is:', sd)



a = 0
d = 0
m = 0
sd = 0
prod = 1
LogPowers2 = []
for i in range(1,1024):
    prod*=2
    d = math.log10(prod)
    LogPowers2.append(d)
print('LogPowers2 =', LogPowers2)
m = sum(LogPowers2);
m /= len(LogPowers2)
print('the mean is: ', m)
sd = statistics.pstdev(LogPowers2)
print('the sd is:', sd)

a = 0
d = 0
m = 0
sd = 0
prod = 1
LogPowersPi = []
for i in range(1,526):
    prod*=math.pi
    d = math.log10(prod)
    LogPowersPi.append(d)
print('LogPowersPi =', LogPowersPi)
m = sum(LogPowersPi);
m /= len(LogPowersPi)
print('the mean is: ', m)
sd = statistics.pstdev(LogPowersPi)
print('the sd is:', sd)

a = 0
d = 0
m = 0
sd = 0
Fib = [1,1]
for i in range(2,1023):
    Fib.append(Fib[i-1]+Fib[i-2])
LogFib = []
for i in range(len(Fib)):
    d = math.log10(Fib[i])
    LogFib.append(d)
print('LogFib =', LogFib)
m = sum(LogFib);
m /= len(LogFib)
print('the mean is: ', m)
sd = statistics.pstdev(LogFib)
print('the sd is:', sd)
