from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = ["played", "player", "playing"]

print("{:<10} {:<10} {:<10} {:<15} {:<12}".format(
    "Word", "Stem", "Affix", "Type", "Normalized"))

print("-" * 65)

for word in words:

    if word.endswith("ed"):
        stem = stemmer.stem(word)
        affix = "ed"
        t = "Inflectional"

    elif word.endswith("ing"):
        stem = stemmer.stem(word)
        affix = "ing"
        t = "Inflectional"

    elif word.endswith("er"):
        stem = word[:-2]
        affix = "er"
        t = "Derivational"

    else:
        stem = stemmer.stem(word)
        affix = "-"
        t = "-"

    normalized = "play"

    print("{:<10} {:<10} {:<10} {:<15} {:<12}".format(
        word, stem, affix, t, normalized))

