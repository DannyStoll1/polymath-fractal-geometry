//
//  Laurent Functions.h
//  Laurent Coefficients Reciprocal Mandelbrot Set
//
//  Created by Jesse Dimino on 8/6/21.
//  Copyright © 2021 Jesse Dimino. All rights reserved.
//

#ifndef Solution_Linked_List_h
#define Solution_Linked_List_h
using namespace std;
#include "math.h"
#include "Logic Functions.h"



class soln
{
public:
    int n;
    int * vec;
    soln():n(0),vec(0){};
    soln(int n,int * vec);
    soln(soln & a);
    ~soln();
    void print();
    void dec();
    bool isLastZero();
    
};


soln::soln(int n, int * vec)
{
    this->n = n;
    this->vec = new int[n];
    for(int i = 0; i<n;i++)
        this->vec[i] = vec[i];
}

soln::soln( soln & a)
{
    this->n = a.n;
    this->vec = new int[n];
    for(int i = 0; i<n; i++)
        this->vec[i] = a.vec[i];
}

soln::~soln()
{
    delete[] this->vec;
    this->vec = nullptr;
}

void soln::print()
{
    //if(this->vec==nullptr)
        //{
            //cout << "the solution is empty" << endl;
            //return;
        //}
    
    cout << '[';
    for(int i = 0; i<this->n-1; i++)
        cout << this->vec[i] << ", ";
    cout << this->vec[this->n-1] << ']';
}

//decrements the last element in the array by 1
void soln::dec()
{
    this->vec[this->n-1]-=1;
}


//checks if the last element in the array is 0
bool soln::isLastZero()
{
    return (this->vec[this->n-1]==0);
}




class solnNode
{
public:
    solnNode():node(),next(0),prev(0){};
    solnNode(soln & a);
    solnNode(solnNode & a);
    ~solnNode();
    soln node;
    solnNode* next;
    solnNode* prev;
};

solnNode::solnNode(soln & a)
{   //soln node(a);
    this->node.n = a.n;
    this->node.vec = new int[this->node.n];
    for(int i = 0; i<this->node.n; i++)
        this->node.vec[i] = a.vec[i];
    this->prev = 0;
    this->next = 0;
    a.~soln();
}

solnNode::solnNode(solnNode & a)
{
    this->node.n = a.node.n;
    this->node.vec = new int[this->node.n];
    for(int i = 0; i<this->node.n; i++)
        this->node.vec[i] = a.node.vec[i];
    this->prev = a.prev;
    this->next = a.next;
}


solnNode::~solnNode()
{
    delete [] this->node.vec;
    this->node.vec = nullptr;
}



//linked list of solutions
class solnLinkedList
{
    
public:
    solnNode * head;
    solnNode * tail;
    int size;
    solnLinkedList():head(0),size(0){};
    ~solnLinkedList();
    void solnAdd(soln &a);
    void solnDel(int j);
    void solnDel(solnNode * a);
    void solnDec(solnNode * a);
    void print();
    void traverse();
};

solnLinkedList::~solnLinkedList()
{
    solnNode * temp = this->head;
    while(temp)
    {
        temp->node.~soln();
        delete temp;
        temp = temp->next;
    }
}

//adds a solution to the linked list
void solnLinkedList::solnAdd(soln &a)
{
    if(size==0)
    {
        solnNode* temp = new solnNode(a);
        this->head = temp;
        this->tail = temp;
        this->size++;
        return;
    }
    solnNode* temp = new solnNode(a);
    temp->next = this->head;
    this->head->prev = temp;
    this->head = temp;
    this->size++;
    
}

void solnLinkedList::solnDel(int j)
{
    if(size == 0)
    {
        cout << "the list is empty" << endl;
        return;
    }
    if(j>size)
    {
        cout << "j outside the range of the list" << endl;
        return;
    }
    if(size == 1)
    {
        this->head->node.~soln();
        delete this->head;
        this->head = nullptr;
        this->tail = nullptr;
        this->size--;
        return;
    }
    if(j==1)
    {
        solnNode * temp = new solnNode();
        temp = this->head;
        this->head = this->head->next;
        temp->node.~soln();
        delete temp;
        temp = nullptr;
        this->size--;
        return;
    }
    if(size==j)
    {   solnNode * temp = new solnNode();
        temp = this->tail;
        temp->prev->next = 0;
        this->tail = temp->prev;
        temp->node.~soln();
        delete temp;
        temp = nullptr;
        this->size--;
        return;
    }
    solnNode * temp1 = new solnNode();
    temp1 = this->head;
    for(int i = 1; i<j; i++)
        temp1 = temp1->next;
    solnNode * temp2 = new solnNode();
    temp2 = temp1;
    temp1->prev->next = temp2->next;
    temp1->next->prev = temp2->prev;
    temp2->node.~soln();
    delete temp2;
    temp1 = nullptr;
    temp2 = nullptr;
    this->size--;
    return;
}


//deletes a specified member of the linked List, used when traversing the linked list 
void solnLinkedList::solnDel(solnNode * a)
{
    if(!a)
    {
        cout << "error with input value" << endl;
        return;
    }
    
    
    if(size == 0)
    {
        cout << "the list is empty" << endl;
        return;
    }
    if(size == 1)
    {
        this->head->node.~soln();
        delete this->head;
        this->head = nullptr;
        this->tail = nullptr;
        this->size--;
        return;
    }
    if(a == this->head)
    {
        solnNode * temp = new solnNode();
        temp = this->head;
        this->head = this->head->next;
        temp->node.~soln();
        delete temp;
        temp = nullptr;
        this->size--;
        return;
    }
    if(a == this->tail)
    {   solnNode * temp = new solnNode();
        temp = this->tail;
        temp->prev->next = 0;
        this->tail = temp->prev;
        temp->node.~soln();
        delete temp;
        temp = nullptr;
        this->size--;
        return;
    }
    solnNode * temp1 = new solnNode();
    temp1 = a;
    solnNode * temp2 = new solnNode();
    temp2 = temp1;
    temp1->prev->next = temp2->next;
    temp1->next->prev = temp2->prev;
    temp2->node.~soln();
    delete temp2;
    temp1 = nullptr;
    temp2 = nullptr;
    this->size--;
    return;
}

void solnLinkedList::solnDec(solnNode * a)
{
    a->node.dec();
}



void solnLinkedList::print()
{
    if(size==0)
    {
        cout << "The list is empty" << endl;
        return;
    }
    solnNode * temp = new solnNode();
    temp = this->head;
    for(int i = 0; i<this->size; i++)
    {
        temp->node.print();
        cout << "->";
        temp = temp->next;
    }
    cout << "null" << endl;
}

void solnLinkedList::traverse()
{
    solnNode * temp1 = new solnNode;
    temp1 = this->head;
    solnNode * temp2 = new solnNode;
    temp2 = temp1;
    while(temp1)
    {
        if(temp1->node.isLastZero())
        {
            temp2 = temp1->next;
            solnDel(temp1);
            temp1 = temp2;
            continue;
        }
        else
        {
            solnDec(temp1);
        }
        temp1 = temp1->next;
    }
    print();
    temp1 = nullptr;
    temp2 = nullptr;
    delete temp1;
    
}

#endif /* Solution_Linked_List_h*/
