//
//  Logic Functions.h
//  Laurent Coefficients Reciprocal Mandelbrot Set
//
//  Created by Jesse Dimino on 8/6/21.
//  Copyright © 2021 Jesse Dimino. All rights reserved.
//

#ifndef Logic_Functions_h
#define Logic_Functions_h

bool isSolution_a_dm(int * iteration, int m, int n, int d)
{
    int val=0;
    for(int i = 0; i<n; i++)
        val+=iteration[i];
    return (val==m-1);
}

bool isSolution_b_dm(int * iteration, int m, int n, int d)
{
    int val=0;
    for(int i = 0; i<n; i++)
        val+=iteration[i];
    return (val==m+1);
}

#endif /* Logic_Functions_h */
