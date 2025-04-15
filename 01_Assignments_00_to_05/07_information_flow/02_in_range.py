# Implement the following function which takes in 3 integers as parameters:

# def in_range(n, low, high) """ Returns True if n is between low and high, inclusive. high is guaranteed to be greater than low. """




def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive. 
    high is guaranteed to be greater than low.
    """
    if n >= low and n <= high:
        return True

    # We could have also included an else statement, but since we are returning, it's fine without!
    return False

# Test the function with print statements
print(in_range(5, 1, 10))  # Output: True
print(in_range(15, 1, 10))  # Output: False
