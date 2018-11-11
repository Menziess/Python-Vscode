import logging
import argparse

logger = logging.getLogger(__name__)


def fib(n):
    """
	Returns fib(n-1) + fib(n-2).
	"""
    logger.debug(f'calculating fibo for {n}')
    if n < 0:
        logger.warning(f'fibo called with n {n}')
        raise ValueError
    x, y = 0, 1
    for _ in range(n):
        x, y = y, x + y
    return y


def main():
    parser = argparse.ArgumentParser(description="calculates fibonacci")
    parser.add_argument("n", type=int, help="the fib number to calculate")

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true")
    group.add_argument("-q", "--quiet", action="store_true")

    args = parser.parse_args()

    logging.basicConfig()

    if args.verbose:
        logger.setLevel(logging.DEBUG)
    if args.quiet:
        logger.setLevel(logging.WARN)
    logger.info(f"starting fibonacci app for n is {args.n}")
    print(fib(args.n))


if __name__ == "__main__":
    main()
