"""
Experiment 08: Simple Stochastic POS Tagger
"""
from collections import defaultdict

# Training data: list of (word, tag) pairs
train_data = [
    ('The', 'DT'), ('cat', 'NN'), ('is', 'VBZ'), ('sleeping', 'VBG'),
    ('A', 'DT'), ('dog', 'NN'), ('runs', 'VBZ'), ('fast', 'RB'),
    ('She', 'PRP'), ('eats', 'VBZ'), ('apples', 'NNS')
]

word_tag_counts = defaultdict(lambda: defaultdict(int))
for word, tag in train_data:
    word_tag_counts[word.lower()][tag] += 1

def tag_sentence(sentence: str):
    tags = []
    for word in sentence.split():
        options = word_tag_counts[word.lower()]
        if options:
            best_tag = max(options, key=options.get)
        else:
            best_tag = 'NN'
        tags.append((word, best_tag))
    return tags

sentence = 'A cat eats apples'
print('Sentence:', sentence)
print('Tags:', tag_sentence(sentence))

# Sample output:
# Tags: [('A', 'DT'), ('cat', 'NN'), ('eats', 'VBZ'), ('apples', 'NNS')]
