# Feature Structures and Subcategorization

# Feature structures
subject = {
    "word": "She",
    "number": "singular",
    "person": "third"
}

verb = {
    "word": "runs",
    "number": "singular",
    "person": "third"
}

print("Sentence: She runs")
print()

print("Feature Structure:")
print("Subject:", subject)
print("Verb   :", verb)
print()

# Check agreement
if (
    subject["number"] == verb["number"]
    and subject["person"] == verb["person"]
):
    print("Subject-Verb Agreement: Correct")
else:
    print("Subject-Verb Agreement: Incorrect")

print()

# Subcategorization frame
sentence = "The teacher gave the student a book"

frame = {
    "verb": "gave",
    "subject": "teacher",
    "object": "book",
    "recipient": "student"
}

print("Sentence:", sentence)
print()

print("Subcategorization Frame:")
print("Verb      :", frame["verb"])
print("Subject   :", frame["subject"])
print("Object    :", frame["object"])
print("Recipient :", frame["recipient"])

print()

# Validate the required arguments
if (
    frame["subject"]
    and frame["object"]
    and frame["recipient"]
):
    print("Verb Argument Structure: Correct")
else:
    print("Verb Argument Structure: Incomplete")
