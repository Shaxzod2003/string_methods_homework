def main(s):
    """
    A variable of type str is given. Check that it consists only of numbers.
    Args:
        s: str
    Returns:
        bool: answer
    """
    
    return s.isdigit()
s="231316"
print(main(s))