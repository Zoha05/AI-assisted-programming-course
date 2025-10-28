from typing import Optional

def recursive_factorial(n: int) -> int:
	"""Return n! using recursion.

	Raises ValueError for negative inputs.
	"""
	if n < 0:
		raise ValueError("Factorial is not defined for negative integers")
	if n <= 1:
		return 1
	return n * recursive_factorial(n - 1)


# Iterative factorial implementation
# Uses a simple loop to multiply numbers from 2..n.
def iterative_factorial(n: int) -> int:
	"""Return n! using an iterative loop.

	Raises ValueError for negative inputs.
	"""
	if n < 0:
		raise ValueError("Factorial is not defined for negative integers")
	result = 1
	i = 2
	while i <= n:
		result *= i
		i += 1
	return result


def _ask_int(prompt: str) -> Optional[int]:

	try:
		raw = input(prompt)
	except Exception:
		return None
	if raw is None:
		return None
	raw = raw.strip()
	if raw == "":
		return None
	try:
		return int(raw)
	except ValueError:
		print("Invalid integer provided.")
		return None


def main() -> None:
	n = _ask_int("Enter a non-negative integer to compute its factorial (leave blank to exit): ")
	if n is None:
		print("No valid integer provided. Exiting.")
		return
	if n < 0:
		print("Factorial is not defined for negative integers. Exiting.")
		return

	# compute both ways and display
	try:
		rec = recursive_factorial(n)
	except RecursionError:
		rec = "<recursion depth exceeded>"
	it = iterative_factorial(n)

	print(f"recursive_factorial({n}) = {rec}")
	print(f"iterative_factorial({n}) = {it}")


if __name__ == "__main__":
	main()

