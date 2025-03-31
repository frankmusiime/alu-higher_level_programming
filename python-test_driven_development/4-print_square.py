def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first name> <last name>".
    
    Args:
        first_name: The first name as a string.
        last_name: The last name as a string (optional, defaults to empty string).
        
    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    print(f"My name is {first_name} {last_name}")

# Example usage
say_my_name("John", "Doe")  # Output: My name is John Doe
say_my_name("Alice")  # Output: My name is Alice

