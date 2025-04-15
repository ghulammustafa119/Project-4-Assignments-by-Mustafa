
# Prompt the user to enter the first number.

# Read the input and convert it to an integer.

# Prompt the user to center the second number.

# Read the input and convert it to an integer.

# Calculate the sum of the two numbers.

# Print the total sum with an appropriate message.

# The provided solution demonstrates a working implementation of this problem, where the main() function guides the user through the process of entering two numbers and displays their sum.

def main():
    print("This program adds two numbers.")
    num1 = int(input("Enter first number: "))  # Convert input directly to int
    num2 = int(input("Enter second number: "))  # Convert input directly to int
    total = num1 + num2
    print(f"The total is: {total}")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()