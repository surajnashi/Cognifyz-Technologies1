#Task3: Email Validator
import re

def is_valid_email(email):
    # Regular expression for validating an email address
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, email):
        return True
    else:
        return False

def main():
    email = input("Enter an email address: ")
    if is_valid_email(email):
        print(f"{email} is a valid email address.")
    else:
        print(f"{email} is not a valid email address.")

if __name__ == "__main__":
    main()

