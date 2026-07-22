"""
Experiment 03: Morphological Analysis using NLTK
"""
try:
    import nltk
    from nltk.stem import WordNetLemmatizer
    from nltk.tokenize import word_tokenize

    nltk.download('punkt', quiet=True)
    nltk.download('wordnet', quiet=True)

    text = "The children are playing with different colored toys."
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    print("Text:", text)
    print("Tokens:", tokens)
    print("Lemmas:", [lemmatizer.lemmatize(token.lower()) for token in tokens])
except ImportError:
    print("NLTK is not installed. Please install it with: pip install nltk")

# Sample output:
# Tokens: ['The', 'children', 'are', 'playing', 'with', 'different', 'colored', 'toys', '.']
# Lemmas: ['The', 'child', 'are', 'playing', 'with', 'different', 'colored', 'toy', '.']
