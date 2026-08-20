# Semantic Representation in Customer Support Chatbot

queries = {
    "Q1": ("Activate Roaming", "Activate Roaming"),
    "Q2": ("Deactivate Caller Tune", "Activate Caller Tune"),
    "Q3": ("Query Data Balance", "Query Data Balance"),
    "Q4": ("Activate 5G Service", "Activate 5G Service")
}

for qid, (actual, predicted) in queries.items():
    print(qid)
    print("Actual Intent   :", actual)
    print("Predicted Intent:", predicted)

    if actual == predicted:
        print("Result          : Correct")
    else:
        print("Result          : Semantic Error")

    print()

