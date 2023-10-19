#!/bin/python3

from functools import reduce
#aplicando conceito de map

def fatorial(n):
    return ( n * fatorial(n-1)) if n > 1 else 1




print(f' 10! = {fatorial (10)}')