"""recursion fundamentals:"""
"""Recursion works on three cases, basically, first is Base Case: I have to know what is the simplest input
for this function.
Second step is, Relation, so i need to see,is there some relation,usingn which a problem can be broken down, into
solution of small sub-problems, which can then be used to find solution to the larger one.
Third and the final step is to find the, mathematical generalised function, that solvs the problem or the tree."""

def sum(n):
    if n==1:
        return 1
    return sum(n-1)+n

def exp(a,b):
    if b ==1:
        return a
    return int(exp(a,b-1)*a)

def fast_exp(a,b):
    if b==1:
        return a
    elif b%2==0:
        return int(fast_exp(a*a,b/2))
    else:
        return int((fast_exp(a,b-1)*a))

def path(n,m):
    if (n==m==1):
        return 1
    return path(n,m-1) + path(m,n-1)

print(path(4,4))


