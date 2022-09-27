import pytest
from functools import lru_cache

from src.fibonacci import Fibonacci

# 基本的な使い方
def test_fibonacci1():
    fib = Fibonacci()
    assert fib(10) == 55

# 複数パターンのパラメタを渡したい時
@pytest.mark.parametrize(('number', 'expected'),[
    (0, 0),
    (1, 1),
    (2, 1),
    (100, 354224848179261915075),
    (500, 139423224561697880139724382870407283950070256587697307264108962948325571622863290691557658876222521294125),
])
def test_fibonacci(number, expected):
    fib = Fibonacci()
    assert fib(number) == expected

# 特定の例外やエラーが発生するか確認したい時
def test_fibonacci3():
    fib = Fibonacci()
    with pytest.raises(RecursionError):
        fib(2000)

# テストのモック作成
@pytest.fixture(scope='module')
def naive_fibonacci():
    arg = 200
    @lru_cache(maxsize=1000)
    def f(n=arg):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        return f(n-1) + f(n-2)
    yield arg, f()

def test_fibonacci4(naive_fibonacci):
    n, expected = naive_fibonacci
    fib = Fibonacci()
    assert fib(n) == expected