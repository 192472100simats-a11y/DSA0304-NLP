words = ["writes", "writing", "written"]

print("{:<10} {:<25} {:<15} {:<12} {:<10}".format(
    "Word", "State Transition", "Pattern", "Root", "Output"))

print("-" * 85)

for word in words:

    if word == "writes":
        transition = "Start → write → +s"
        pattern = "Regular"
        root = "write"

    elif word == "writing":
        transition = "Start → write → +ing"
        pattern = "Regular"
        root = "write"

    elif word == "written":
        transition = "Start → write → irregular"
        pattern = "Irregular"
        root = "write"

    print("{:<10} {:<25} {:<15} {:<12} {:<10}".format(
        word, transition, pattern, root, root))
