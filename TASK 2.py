# Function to reverse a string
def reverse_string(s: str) -> str:
	"""Return the reverse of the given string."""
	# simple, Pythonic slice reversal
	return s[::-1]


def main() -> None:
	# ask user for a string to reverse (leave blank to skip)
	try:
		txt = input("Enter a string to reverse (leave blank to skip): ")
	except Exception:
		txt = ""

	if txt:
		print("Reversed string:", reverse_string(txt))
	else:
		print("No string provided. Exiting.")


if __name__ == "__main__":
	main()

