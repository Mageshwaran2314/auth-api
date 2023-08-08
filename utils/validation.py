import re

def is_valid_email(email):
    # Regular expression pattern to match email format
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Use the re.match function to check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False


def is_valid_password(password):
    # Minimum requirements
    min_length = 8
    requires_uppercase = True
    requires_lowercase = True
    requires_digit = True
    requires_special_char = True

    # Regular expressions to check for specific character types
    uppercase_pattern = r'[A-Z]'
    lowercase_pattern = r'[a-z]'
    digit_pattern = r'\d'
    special_char_pattern = r'[!@#$%^&*()]'

    # Check password length
    if len(password) < min_length:
        return False

    # Check if uppercase letters are required and present
    if requires_uppercase and not re.search(uppercase_pattern, password):
        return False

    # Check if lowercase letters are required and present
    if requires_lowercase and not re.search(lowercase_pattern, password):
        return False

    # Check if digits are required and present
    if requires_digit and not re.search(digit_pattern, password):
        return False

    # Check if special characters are required and present
    if requires_special_char and not re.search(special_char_pattern, password):
        return False

    return True

