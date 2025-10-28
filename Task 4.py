def find_largest_number(numbers):
    """Return the largest number in a list. Returns None if the list is empty."""
    if not numbers:
        return None
    largest = numbers[0]
    for num in numbers[1:]:
        if num > largest:
            largest = num
    return largest

if __name__ == "__main__":
    user_input = input("Enter numbers separated by spaces: ")
    try:
        num_list = [float(x) for x in user_input.strip().split()]
    except ValueError:
        print("Invalid input. Please enter only numbers.")
    else:
        result = find_largest_number(num_list)
        if result is not None:
            print(f"The largest number is: {result}")
        else:
            print("No numbers were entered.")
