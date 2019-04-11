# More performant version
# The number of times this will run is n- 1
# with the iterative approach we move forward. 
# in the recursive approach we go backwards
def fib(n:int) -> int:
    if n == 0: return n
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next #using 'tuple unpackingt
    return next

if __name__ == "__main__":
    print(fib(14))
    print(fib(233))