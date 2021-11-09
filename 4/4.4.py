def fibonacci(n):
    a = 1
    b = 1
    while n > 1:
        a, b = b, a+b
        n-=1
    return a
