//
//  main.cpp
//  Laurent Coefficients Reciprocal Mandelbrot Set
//
//  Created by Jesse Dimino on 8/6/21.
//  Copyright © 2021 Jesse Dimino. All rights reserved.
//

#include <iostream>
#include "Solution Linked List.h"
#include "Logic Functions.h"
#include "Generation Functions.h"
#include "Iteration Functions.h"
#include "Computation Functions.h"
using namespace std;
int main(int argc, const char * argv[]) {
    // insert code here...
    
    std::cout << "Hello, World!\n";
    int arr[3] = {1,2,3};
    for(int i = 0; i<3; i++)
        cout << arr[i] << ' ';
    cout << endl;
    cout << Digit(-0.005) << endl;
    rational q(3,2);
    rational p =binomialCoefficient(q, 2);
    p.print();
    int w[3] = {0,1,2}, e[3]={3,4,5}, r[3]={7,8,9};
    soln soln1(3,w), soln2(3,e), soln3(3,r);
    solnLinkedList list;
    list.solnAdd(soln1);
    list.solnAdd(soln2);
    list.solnAdd(soln3);
    list.print();
    //list.solnDel(1);
    solnNode * temp = new solnNode();
    temp = list.head;
    temp= temp->next;
    temp = temp->next;
    list.traverse();
    list.print();
    return 0;
}
