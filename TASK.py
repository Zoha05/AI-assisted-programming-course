#!/usr/bin/env python3

import argparse
import math
import sys


def is_prime(n: int) -> bool:
	
	if n <= 1:
		return False
	if n <= 3:
		return True
	if n % 2 == 0:
		return False

	# use math.isqrt for exact integer sqrt (Python 3.8+)
	limit = math.isqrt(n)
	for i in range(3, limit + 1, 2):
		if n % i == 0:
			return False
	return True


def format_response(n: int, prime: bool) -> str:
	
	if prime:
		return (
			f"{n} is a prime number — the only positive divisors are 1 and itself. "
			f"This was validated by checking potential factors up to √{n}."
		)
	else:
		return (
			f"{n} is not a prime number — it has a non-trivial divisor that was detected by trial division up to √{n}."
		)


def main() -> None:
	parser = argparse.ArgumentParser(description="Check if a number is prime.")
	parser.add_argument("-n", "--number", type=int, help="Integer to test for primality")
	args = parser.parse_args()

	if args.number is not None:
		n = args.number
	else:
		try:
			raw = input("Enter an integer to test for primality: ")
			n = int(raw.strip())
		except Exception:
			print("Invalid input. Please provide a valid integer.", file=sys.stderr)
			sys.exit(1)

	result = is_prime(n)
	print(format_response(n, result))


if __name__ == "__main__":
	main()

