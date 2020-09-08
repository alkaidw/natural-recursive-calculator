''' 6 recursive operations
    this is a implementation of a natural recursive
    calculator. that use the operations:

        > == +

    and the condictional statement:

        if
    
'''

def incr(a):
    return a + 1

def decr(a): 
    return _decr(a, 0)

def _decr(a, i):
    if a > incr(i):
        return _decr(a, incr(i))
    return i
    
def adic(a, b):
    if b == 0:
        return a
    return incr(adic(a,decr(b)))
    
def subtr(a, b):
    if b > 0:
        return subtr(decr(a), decr(b))
    return a

def mult(a, b):
    if b == 0:
        return 0
    return adic(a, mult(a, decr(b)))

def div(n, d):
    if n > d:
        if n == d:
            return incr(div(subtr(n, d), d))
    return 0

def mod(n, d):
    if n > d:
        if n == d:
            return mod(subtr(n, d), d)
    return n
 
def exp(a, b):
    if b == 0:
        return 0
    return mult(a, mult(a, decr(b)))

