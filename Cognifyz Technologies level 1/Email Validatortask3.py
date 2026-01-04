def is_valid_email(email):
    # Check if exactly one '@' is present
    if email.count("@") != 1:
        return False

    username, domain = email.split("@")

    # Username and domain should not be empty
    if not username or not domain:
        return False

    # Domain must contain at least one '.'
    if "." not in domain:
        return False

    return True


# User input
email = input("Enter an email address: ")

if is_valid_email(email):
    print("Valid email address")
else:
    print("Invalid email address")
