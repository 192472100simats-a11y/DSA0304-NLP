"""
Experiment 02: Finite State Automaton matching strings ending with 'ab'
"""

def ends_with_ab(s: str) -> bool:
    state = 0
    for ch in s:
        if state == 0:
            state = 1 if ch == 'a' else 0
        elif state == 1:
            state = 2 if ch == 'b' else 1 if ch == 'a' else 0
        elif state == 2:
            state = 1 if ch == 'a' else 0
    return state == 2

samples = ["ab", "cab", "aab", "abc", "baba", "hello"]
print("FSA recognizes strings that end with 'ab'.")
for sample in samples:
    print(sample, "->", ends_with_ab(sample))

# Sample output:
# ab -> True
# cab -> True
# aab -> True
# abc -> False
# baba -> True
# hello -> False
