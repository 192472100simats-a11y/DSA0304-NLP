# CFG, PCFG and Neural Parsing

sentence = "She saw the man with a telescope"

print("Sentence:", sentence)
print()

# Two possible interpretations
parse1 = "She used the telescope to see the man."
parse2 = "The man had the telescope."

print("Possible Interpretations:")
print("1.", parse1)
print("2.", parse2)
print()

# CFG generates both possible parses
print("CFG:")
print("Number of possible parses = 2")
print()

# Example PCFG probabilities
probability1 = 0.70
probability2 = 0.30

print("PCFG:")
print("Parse 1 probability =", probability1)
print("Parse 2 probability =", probability2)

if probability1 > probability2:
    best_parse = parse1
else:
    best_parse = parse2

print("Selected Parse:", best_parse)
print()

# Neural parser demonstration
print("Neural Parsing:")
print("Uses contextual information from training data.")
print("Best interpretation:", best_parse)
