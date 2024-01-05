a = [1, 2, 3]
b = [7, 8, 9]

print([(x+y) for (x,y) in zip(a,b)])

def fib(n):
    p,q=0,1
    while(p<q):
        yield p
        p,q=q,p+q

x=fib(5)
x.__next__()
x.__next__()