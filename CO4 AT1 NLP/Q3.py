# Word Sense Disambiguation

queries = {
    "Apple accessories": {
        "sense": "Technology Brand",
        "result": "iPhone Charger"
    },
    "Mouse wireless": {
        "sense": "Computer Device",
        "result": "Bluetooth Mouse"
    },
    "Java tutorial": {
        "sense": "Programming Language",
        "result": "Coding Lessons"
    },
    "Python course": {
        "sense": "Programming Language",
        "result": "Software Development Training"
    }
}

for query, data in queries.items():
    print("Query :", query)
    print("Correct Sense :", data["sense"])
    print("Clicked Result:", data["result"])
    print()
