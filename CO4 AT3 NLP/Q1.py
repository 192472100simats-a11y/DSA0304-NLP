# CFG Tree and Dependency Parsing

sentence = "The student reads the book"

words = sentence.split()

print("Sentence:", sentence)
print()

# Simple CFG-style constituency structure
print("CFG Tree:")
print("S")
print("|-- NP")
print("|   |-- The")
print("|   `-- student")
print("`-- VP")
print("    |-- reads")
print("    `-- NP")
print("        |-- the")
print("        `-- book")

print()

# Simple dependency relations
dependencies = [
    ("reads", "student", "subject"),
    ("reads", "book", "object"),
    ("student", "The", "determiner"),
    ("book", "the", "determiner")
]

print("Dependency Relations:")

for head, dependent, relation in dependencies:
    print(head, "-->", dependent, "(", relation, ")")
