def product_fib(prod):
    a,b=0,1
    while prod>a*b:
        temp=a
        a=b
        b=b+temp
    return [a,b, prod==a*b]

def fib(n):
    if (n <=1):
        return(1)
    else:
        return(fib(n-1)+fib(n-2))
