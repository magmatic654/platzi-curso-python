def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+ fibonacci(n-2)
    
fibonacci_10 = fibonacci(8)

print(fibonacci_10)