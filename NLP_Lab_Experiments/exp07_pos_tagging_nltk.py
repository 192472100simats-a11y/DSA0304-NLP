"""
Experiment 07: POS Tagging using NLTK
"""
try:
    import nltk
    from nltk import pos_tag, word_tokenize

    nltk.download('punkt', quiet=True)
    nltk.download('averaged_perceptron_tagger', quiet=True)

    text = 'The quick brown fox jumps over the lazy dog.'
    tokens = word_tokenize(text)
    tags = pos_tag(tokens)

    print('Text:', text)
    print('Tokens:', tokens)
    print('POS tags:', tags)
except ImportError:
    print('NLTK is not installed. Please install it with: pip install nltk')

# Sample output:
# POS tags: [('The', 'DT'), ('quick', 'JJ'), ('brown', 'JJ'), ('fox', 'NN'), ('jumps', 'VBZ'), ('over', 'IN'), ('the', 'DT'), ('lazy', 'JJ'), ('dog', 'NN'), ('.', '.')]
