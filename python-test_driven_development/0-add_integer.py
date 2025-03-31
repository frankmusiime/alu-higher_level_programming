def add_integer(a, b=98):
    """
    Adds two integers.
    
    Args:
        a: First number (int or float).
        b: Second number (int or float, default is 98).
        
    Returns:
        The sum of a and b as an integer.
        
    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)

# Example usage
print(add_integer(10, 20))  # Output: 30
print(add_integer(10.5, 20.7))  # Output: 30 (since floats are cast to int)

