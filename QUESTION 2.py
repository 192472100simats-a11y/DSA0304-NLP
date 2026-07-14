import re

# Product list
products = [
    "Laptop",
    "Laptop Bag",
    "Smartphone",
    "Phone Charger",
    "Bluetooth Speaker",
    "Wireless Mouse",
    "Gaming Laptop",
    "USB Cable"
]

keyword = input("Enter search keyword: ")

# Exact Match
exact_matches = [p for p in products if re.fullmatch(keyword, p, re.IGNORECASE)]

# Prefix Search
prefix_matches = [p for p in products if re.search("^" + re.escape(keyword), p, re.IGNORECASE)]

# Suffix Search
suffix_matches = [p for p in products if re.search(re.escape(keyword) + "$", p, re.IGNORECASE)]

# Partial Search
partial_matches = [p for p in products if re.search(re.escape(keyword), p, re.IGNORECASE)]

print("\n----- PRODUCT SEARCH REPORT -----")

print("\nExact Match:")
for item in exact_matches:
    print(item)
print("Total Matches:", len(exact_matches))

print("\nPrefix Search:")
for item in prefix_matches:
    print(item)
print("Total Matches:", len(prefix_matches))

print("\nSuffix Search:")
for item in suffix_matches:
    print(item)
print("Total Matches:", len(suffix_matches))

print("\nPartial / Case-Insensitive Search:")
for item in partial_matches:
    print(item)
print("Total Matches:", len(partial_matches))
