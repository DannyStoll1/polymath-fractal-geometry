format long
t = 1023;
x = 1:1:t;
product = 1;
d = 0;
c = 0;
fib = zeros(1,t);
fib(1) = 1;
fib(2) = 1;
for i=3:t
    fib(i) = fib(i-1) + fib(i-2);
end

digits = zeros(1,9);
ChiSquVec = zeros(1,t);
for n=1:t
expec = n*log10([2,3/2,4/3,5/4,6/5,7/6,8/7,9/8,10/9]);
d = firstDigit(fib(n));
digits(d) = digits(d) + 1;

c = ChiSqu(expec,digits);

ChiSquVec(n) = c;


end 

plot(x,ChiSquVec)


function c = ChiSqu(expec,obs)
c = 0;
for i=1:length(expec)
    c = c + (expec(i)-obs(i))^2/expec(i);
end 

end
