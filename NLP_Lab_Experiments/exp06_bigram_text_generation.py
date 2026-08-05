yyeplace"""
Experiment 06: Bigram Text Generation
"""
import random

corpus = " i love python because python is to learn"
words = corpus.split()
bigrams = {}
for i in range(len(words) - 1):
    bigrams.setdefault(words[i], []).append(words[i + 1])

current = words[0]
output = [current]
for _ in range(15):
    choices = bigrams.get(current, words)
    current = random.choice(choices)
    output.append(current)

print('Corpus:', corpus)
print('Generated text:')
print(' '.join(output))

# Sample output might be:
# I love natural language processing and I love writing simple programs ...
