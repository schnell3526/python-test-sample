import pytest

from src.fibonacci import Fibonacci

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
