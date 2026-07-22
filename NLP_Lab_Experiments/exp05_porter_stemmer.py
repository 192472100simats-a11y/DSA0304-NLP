"""
Experiment 05: Porter Stemmer using NLTK
"""
try:
    import nltk
    from nltk.stem import PorterStemmer

    nltk.download('punkt', quiet=True)

    stemmer = PorterStemmer()
    words = ['running', 'happiness', 'played', 'studies', 'cars']
    stems = [stemmer.stem(word) for word in words]

    print('Words:', words)
    print('Stemmed:', stems)
except ImportError:
    print('NLTK is not installed. Please install it with: pip install nltk')

# Sample output:
# Stemmed: ['run', 'happi', 'play', 'studi', 'car']
