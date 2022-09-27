def Fibonacci() -> int:
    ls = {0: 0, 1: 1}
    def f(n: int):
        nonlocal ls
        if len(ls) <= n:
            ls[n] = f(n-2) + f(n-1)
        return ls[n]
    return f

def test_Fibonacci():
    fib = Fibonacci()
    assert fib(0) == 0