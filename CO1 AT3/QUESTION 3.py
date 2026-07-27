import re

text = """
Meeting on 12/09/2026
Call 9876543210
#NLP
@OpenAI
natural language processing
"""

print("Text:")
print(text)

while True:

    print("\n1.Search Date")
    print("2.Search Phone Number")
    print("3.Search Hashtag")
    print("4.Search Mention")
    print("5.Search Prefix")
    print("6.Search Suffix")
    print("7.Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        result = re.findall(r'\b\d{2}/\d{2}/\d{4}\b', text)
        print(result)

    elif choice == 2:
        result = re.findall(r'\b[6-9]\d{9}\b', text)
        print(result)

    elif choice == 3:
        result = re.findall(r'#\w+', text)
        print(result)

    elif choice == 4:
        result = re.findall(r'@\w+', text)
        print(result)

    elif choice == 5:
        word = input("Enter Prefix: ")
        result = re.findall(r'\b' + word + r'\w*', text)
        print(result)

    elif choice == 6:
        word = input("Enter Suffix: ")
        result = re.findall(r'\b\w*' + word + r'\b', text)
        print(result)

    elif choice == 7:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")