def is_palindrome_simple(s: str) -> bool:
    """
    Simple approach: build a cleaned string (letters+digits, lowercase)
    and compare it to its reverse.
    """
    cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]


def is_palindrome_two_pointer(s: str) -> bool:
    """
    Memory-efficient two-pointer approach that ignores non-alphanumeric
    characters and compares characters case-insensitively without building
    a second string.
    """
    left, right = 0, len(s) - 1
    while left < right:
        # move left forward to next alnum
        while left < right and not s[left].isalnum():
            left += 1
        # move right backward to prev alnum
        while left < right and not s[right].isalnum():
            right -= 1
        if left < right:
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
    return True


def main():
    print("Palindrome Checker")
    print("Type 'quit' to exit.")
    while True:
        text = input("\nEnter text to check: ")
        if text.strip().lower() == "quit":
            break

        # You can choose either check; both ignore punctuation and case.
        simple_result = is_palindrome_simple(text)
        pointer_result = is_palindrome_two_pointer(text)

        print(f"Simple method:      {'Palindrome' if simple_result else 'Not a palindrome'}")
        print(f"Two-pointer method: {'Palindrome' if pointer_result else 'Not a palindrome'}")

        # Show cleaned form for clarity
        cleaned = ''.join(ch.lower() for ch in text if ch.isalnum())
        print(f"Cleaned (for check): {cleaned}")


if __name__ == "__main__":
    main()