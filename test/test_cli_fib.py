from src.cli.command_line_fib import fib
import pytest

inp = range(0, 8)
out = (1, 1, 2, 3, 5, 8, 13, 21)

fib_pairs = zip(inp, out)


def test_except_when_n_lt_zero():
    with pytest.raises(ValueError):
        fib(-1)


@pytest.mark.parametrize("n, expected", list(fib_pairs))
def test_fib(n, expected):
    assert fib(n) == expected
