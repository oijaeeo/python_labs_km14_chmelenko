def factorial(n):
    if n == 1:
        return 1
    else:
        m = n * factorial(n - 1)
        return m