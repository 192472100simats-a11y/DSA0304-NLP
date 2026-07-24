print("=" * 65)
print("{:<15} {:<20} {:<20}".format("Root Word", "Inflectional Form", "Derivational Form"))
print("=" * 65)

data = [
    ("play", "played", "player"),
    ("teach", "teaches", "teacher"),
    ("happy", "happier", "happiness"),
    ("beauty", "beauties", "beautiful"),
    ("write", "writing", "writer")
]

for root, inflectional, derivational in data:
    print("{:<15} {:<20} {:<20}".format(root, inflectional, derivational))

print("=" * 65)
