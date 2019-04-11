from functools import lru_cache

#built-in decorator for meoization
@lru_cache(maxsize=None) # None indicates no limit in caching
def fib(n: int) -> int:
    if n < 2: #Base case
        return n
    return fib(n - 2) + fib(n - 1) # Recursive call

if __name__ == "__main__":
    print(fib(5))
    print(fib(233))