# Transition-Based and Graph-Based Dependency Parsing

words = ["Student", "reads", "book"]

print("Sentence:", " ".join(words))
print()

# -----------------------------
# Transition-Based Parsing
# -----------------------------

stack = ["ROOT"]
buffer = words.copy()
dependencies = []

print("Transition-Based Parsing:")
print()

# SHIFT Student
stack.append(buffer.pop(0))
print("SHIFT  -> Stack:", stack, "Buffer:", buffer)

# SHIFT reads
stack.append(buffer.pop(0))
print("SHIFT  -> Stack:", stack, "Buffer:", buffer)

# LEFT-ARC: reads -> Student
dependencies.append(("reads", "Student", "subject"))
stack.pop(-2)
print("LEFT-ARC -> reads -> Student")

# SHIFT book
stack.append(buffer.pop(0))
print("SHIFT  -> Stack:", stack, "Buffer:", buffer)

# RIGHT-ARC: reads -> book
dependencies.append(("reads", "book", "object"))
stack.pop()
print("RIGHT-ARC -> reads -> book")

print()
print("Transition-Based Dependencies:")

for head, dependent, relation in dependencies:
    print(head, "-->", dependent, "(", relation, ")")

print()

# -----------------------------
# Graph-Based Parsing
# -----------------------------

print("Graph-Based Parsing:")

candidate_edges = [
    ("reads", "Student", "subject"),
    ("reads", "book", "object"),
    ("Student", "book", "modifier")
]

print("Candidate dependency edges:")

for head, dependent, relation in candidate_edges:
    print(head, "-->", dependent, "(", relation, ")")

# Select the best complete tree
best_tree = [
    ("reads", "Student", "subject"),
    ("reads", "book", "object")
]

print()
print("Best Dependency Tree:")

for head, dependent, relation in best_tree:
    print(head, "-->", dependent, "(", relation, ")")
