def factorial(n):
    if n == 0:
        return 1
    else: 
        result = 1
        for i in range(1, n+1):
            result *= i
        return result

a, b = map(int, input().split())

print(factorial(a)//(factorial(b)*factorial(a-b)))