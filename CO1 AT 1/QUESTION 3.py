import re

# Input from user
reg_no = input("Enter Register Number: ")
email = input("Enter Institutional Email: ")
course_code = input("Enter Course Code: ")
semester = input("Enter Semester (1-8): ")
mobile = input("Enter Mobile Number: ")

status = True

# Validate Register Number (Example: 192472100)
if re.fullmatch(r'\d{9}', reg_no):
    print("Register Number: Valid")
else:
    print("Register Number: Invalid")
    status = False

# Validate Institutional Email
if re.fullmatch(r'[a-zA-Z0-9._%+-]+@saveetha\.com', email):
    print("Email Address: Valid")
else:
    print("Email Address: Invalid")
    status = False

# Validate Course Code (Example: DSA03)
if re.fullmatch(r'[A-Z]{3}\d{2}', course_code):
    print("Course Code: Valid")
else:
    print("Course Code: Invalid")
    status = False

# Validate Semester (1 to 8)
if re.fullmatch(r'[1-8]', semester):
    print("Semester: Valid")
else:
    print("Semester: Invalid")
    status = False

# Validate Mobile Number (10 digits starting with 6,7,8,9)
if re.fullmatch(r'[6-9]\d{9}', mobile):
    print("Mobile Number: Valid")
else:
    print("Mobile Number: Invalid")
    status = False

# Final Registration Status
print("\n----- REGISTRATION STATUS -----")

if status:
    print("Registration Successful")
else:
    print("Registration Failed")
