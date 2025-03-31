def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ?, and :
    
    Args:
        text: The text to be formatted as a string.
        
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    special_chars = ".?:"
    result = ""
    
    for char in text:
        result += char
        if char in special_chars:
            result += "\n\n"
    
    print("\n".join(line.strip() for line in result.split("\n")))

# Example usage
text_indentation("Hello. How are you? I am fine: Thanks!")

