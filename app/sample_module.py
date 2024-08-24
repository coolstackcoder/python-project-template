# app/sample_module.py

def capitalize_string(s: str) -> str:
    """
    Capitalizes the first letter of each word in a given string.

    Args:
        s (str): The input string.

    Returns:
        str: The capitalized string.
    """
    if not isinstance(s, str):
        raise ValueError("Input must be a string.")
    return s.title()

def reverse_string(s: str) -> str:
    """
    Reverses the given string.

    Args:
        s (str): The input string.

    Returns:
        str: The reversed string.
    """
    if not isinstance(s, str):
        raise ValueError("Input must be a string.")
    return s[::-1]

def is_palindrome(s: str) -> bool:
    """
    Checks if the given string is a palindrome.

    Args:
        s (str): The input string.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    if not isinstance(s, str):
        raise ValueError("Input must be a string.")
    return s == s[::-1]