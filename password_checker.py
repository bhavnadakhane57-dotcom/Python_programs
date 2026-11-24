import re

def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."
    if not re.search("[a-z]", password):
        return "Weak: Add at least one lowercase letter."
    if not re.search("[A-Z]", password):
        return "Weak: Add at least one uppercase letter."
    if not re.search("[0-9]", password):
        return "Weak: Add at least one number."
    if not re.search("[@#$%^&+=!]", password):
        return "Weak: Add at least one special character (@, #, $, etc.)."
    
    return "Strong Password! Good job."

user_pass = input("Enter a password to test: ")
print(check_password_strength(user_pass))
