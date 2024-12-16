password = "secure3p@$"
password_length=len(password)

if len(password) < 6:
    strength="weak"
elif len(password) <= 10:
    strength="Medium"
elif
    strength="strong"

print("password strength is:",strength)               