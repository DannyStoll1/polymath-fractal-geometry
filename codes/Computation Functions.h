//
//  Computation Functions.h
//  Laurent Coefficients Reciprocal Mandelbrot Set
//
//  Created by Jesse Dimino on 8/6/21.
//  Copyright © 2021 Jesse Dimino. All rights reserved.
//

#ifndef Computation_Functions_h
#define Computation_Functions_h

//class to work with rational numbers
//treats the numerator and denominator seperately
class rational
{
public:
    int num;
    int den;
    rational(int a=0, int b=1):num(a),den(b){};
    rational operator +(rational b);
    rational operator +(int b);
    rational operator -(rational b);
    rational operator -(int b);
    rational operator *(rational b);
    rational operator *(int b);
    rational operator /(rational b);
    rational operator /(int b);
    bool operator ==(rational b);
    double decimal();
    void print();
    //need a function to put rationals in lowest terms, will add that later
};

//rational addition
rational rational::operator+(rational b)
{
    rational c;
    c.num = (this->num*b.den)+(b.num*this->den);
    c.den = this->den*b.den;
    return c;
    
}

rational rational::operator+(int b)
{
    rational c;
    c.num = (this->num) + (b*this->den);
    c.den = this->den;
    return c;
}

//rational subtraction
rational rational::operator-(rational b)
{
    b.num*=(-1);
    rational c;
    c.num = (this->num*b.den)+(b.num*this->den);
    c.den = this->den*b.den;
    return c;
    
}

rational rational::operator-(int b)
{   b*=(-1);
    rational c;
    c.num = (this->num) + (b*this->den);
    c.den = this->den;
    return c;
}


//rational multiplication
rational rational::operator*(rational b)
{
    
    rational c;
    c.num = this->num*b.num;
    c.den = this->den*b.den;
    return c;
}

rational rational::operator*(int b)
{
    rational c;
    c.num = this->num*b;
    c.den = this->den;
    return c;
}

//rational division
rational rational::operator/(rational b)
{
    rational c;
    c.num = this->num*b.den;
    c.den = this->den*b.num;
    return c;
}

rational rational::operator/(int b)
{
    rational c;
    c.num = this->num;
    c.den = this->den*b;
    return c;
}

//equality of rational numbers
bool rational::operator==(rational b)
{
    return ((this->num==b.num)&&(this->den==b.den));
}

//prints a rational number
void rational::print()
{
    cout << this->num << '/' << this->den << endl;
}

//converts a rational number into decimal form
double rational::decimal()
{
    return this->num/this->den;
}



//standard recursive definition of a factorial
int factorial(int k)
{
    if(k==0)
        return 1;
    else
        return k*factorial(k-1);
}

//return the general binomial coefficient in rational form (non-reduced)
rational binomialCoefficient(rational n, int k)
   {
       if(((n.num==k)&&(n.den==1))||(k==0))
           return 1;
       
       rational product(n.num,n.den),c(0,1);
       for(int i = 1; i<k; i++)
       {   c.num=i;
           product = product*(n-c);
           product.den*=(k-i+1);
       }
       //product.den*=factorial(k);
       return product;
   }
 
//returns the dth digit of a number
int Digit(double num, int d=1)
{   if(num<0)
        num*=(-1);
    else if(num==0)
        return 0;
    while(num < 1)
        num*=10;
    string s = to_string(num);
    return static_cast<int>(s[0])-48;
}


//class for the Laurent Coeff
class LaurentCoeff
{
public:
    
private:
    int m;
    rational val;
    
};


int LaurentCoeffCalc(int m, int n, int d)
{
    int coeff;
    return coeff;
    
}

#endif /* Computation_Functions_h */
