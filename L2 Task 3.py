import math  # Import math module for pi and other mathematical operations

def calculate_area(shape_type):
    """
    Calculate the area of different shapes based on user input.
    Supports circle, rectangle, triangle, and square.
    """
    # Convert shape type to lowercase to make input case-insensitive
    shape_type = shape_type.lower()
    
    if shape_type == "circle":
        # Get radius from user and calculate circle area using πr²
        radius = float(input("Enter the radius of the circle: "))
        area = math.pi * radius ** 2
        return f"Area of circle = {area:.2f} square units"
        
    elif shape_type == "rectangle":
        # Get length and width, calculate rectangular area using l×w
        length = float(input("Enter the length of rectangle: "))
        width = float(input("Enter the width of rectangle: "))
        area = length * width
        return f"Area of rectangle = {area:.2f} square units"
        
    elif shape_type == "triangle":
        # Get base and height, calculate triangle area using ½×b×h
        base = float(input("Enter the base of triangle: "))
        height = float(input("Enter the height of triangle: "))
        area = 0.5 * base * height
        return f"Area of triangle = {area:.2f} square units"
        
    elif shape_type == "square":
        # Get side length, calculate square area using s²
        side = float(input("Enter the side length of square: "))
        area = side ** 2
        return f"Area of square = {area:.2f} square units"
        
    else:
        return "Invalid shape type! Please choose circle, rectangle, triangle, or square."

# Main program
print("Available shapes: circle, rectangle, triangle, square")
shape = input("Enter the shape type to calculate its area: ")
result = calculate_area(shape)
print(result)

