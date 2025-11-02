def calculate_odd_even_sums(numbers):
    """
    Calculate separate sums for odd and even numbers in a list.
    
    Args:
        numbers (list): List of integers
        
    Returns:
        tuple: (sum of even numbers, sum of odd numbers)
    """
    even_sum = sum(num for num in numbers if num % 2 == 0)
    odd_sum = sum(num for num in numbers if num % 2 != 0)
    return even_sum, odd_sum

def main():
    # Get input from user
    print("Enter numbers separated by spaces (e.g., 1 2 3 4 5): ")
    try:
        # Convert input string to list of integers
        numbers = [int(x) for x in input().strip().split()]
        
        if not numbers:
            print("No numbers entered.")
            return
            
        # Calculate sums
        even_sum, odd_sum = calculate_odd_even_sums(numbers)
        
        # Print results
        print("\nResults:")
        print(f"Numbers entered: {numbers}")
        print(f"Sum of even numbers: {even_sum}")
        print(f"Sum of odd numbers: {odd_sum}")
        print(f"Total sum: {even_sum + odd_sum}")
        
    except ValueError:
        print("Invalid input! Please enter only integers separated by spaces.")

if __name__ == "__main__":
    main()
