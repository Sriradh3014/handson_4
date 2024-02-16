def fib(n):
    print(f"fib({n}) -> ",end="")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)
res=fib(5)
print(f"\n {res}")