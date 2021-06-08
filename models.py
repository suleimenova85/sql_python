def fibb(n):
    if n <= 1:
        return 1
    print(n)
    return fibb(n - 1) + fibb(n - 2)

print(fibb(5))