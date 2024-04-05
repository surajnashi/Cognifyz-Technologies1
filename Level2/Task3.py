#Task3: Password Strength Checker
import re

def check_password_strength(password):
    # Minimum length check
    if len(password) < 8:
        return "Password is too short. It should be at least 8 characters long."

    # Presence of uppercase and lowercase letters, digits, and special characters
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = bool(re.search("[!@#$%^&*()-+=]", password))

    # Strength evaluation
    if has_uppercase and has_lowercase and has_digit and has_special:
        return "Strong password."
    else:
        missing_factors = []
        if not has_uppercase:
            missing_factors.append("uppercase letters")
        if not has_lowercase:
            missing_factors.append("lowercase letters")
        if not has_digit:
            missing_factors.append("digits")
        if not has_special:
            missing_factors.append("special characters")

        return f"Weak password. It is missing: {', '.join(missing_factors)}."

# Example usage
password = input("Enter your password: ")
print(check_password_strength(password))
