"""
Experiment 01: Regular Expression Matching
"""
import re

text = "The quick brown fox jumps over the lazy dog. Contact: example@mail.com"
pattern = r"\b\w{5}\b"

matches = re.findall(pattern, text)
search = re.search(r"\bexample@mail\.com\b", text)

print("Text:", text)
print("Pattern:", pattern)
print("Matches (5-letter words):", matches)
print("Email found:", bool(search))

# Sample output:
# Text: The quick brown fox jumps over the lazy dog. Contact: example@mail.com
# Matches (5-letter words): ['quick', 'brown', 'jumps']
# Email found: True
