def add(a,b):
    return a+b
def sub(a,b):
    return a-b 
def mul(a,b):
    return a*b 
def divide(a,b):
    return a/b 
def si(P,R,T): # si means simple Interest
    return (P*R*T)/100       
def ci(P,R,T): # ci means compound Interest 
    return P*pow((1+R/100),T)             
def sqr(num):
    return num**2
def st(num):
    return num**0.5

# It is like a package were all funtions are preserved
print(add(10,66)) # Here by calling the function we can execute that functions
