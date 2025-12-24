# 1. Simple if statement
age = 16
if age < 18:
    print("You are a minor")

print("---")

# 2. If-Else statement
age = 20
if age < 18:
    print("Minor")
else:
    print("Adult")

print("---")

# 3. Elif statement
age = 70
if age < 18:
    print("Minor")
elif age < 65:
    print("Adult")
else:
    print("Senior")

print("---")

# 4. Nested conditionals
age = 25
is_student = True
if age < 30:
    if is_student:
        print("Young student")
    else:
        print("Young professional")
else:
    print("Adult")

print("---")

# 5. Combining logical operators with conditionals
score = 85
attendance = 90
if score > 80 and attendance > 75:
    print("Eligible for certificate")
else:
    print("Not eligible")
