# Top-Down and Earley Parsing

grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": [["the"]],
    "N": [["student"], ["book"]],
    "V": [["reads"]]
}

sentence = ["the", "student", "reads", "the", "book"]


# Simple top-down parser
def top_down(symbol, words, pos):
    if symbol not in grammar:
        if pos < len(words) and symbol == words[pos]:
            return pos + 1
        return None

    for rule in grammar[symbol]:
        current = pos
        success = True

        for part in rule:
            result = top_down(part, words, current)

            if result is None:
                success = False
                break

            current = result

        if success:
            return current

    return None


print("Sentence:", " ".join(sentence))
print()

# Top-down parsing
result = top_down("S", sentence, 0)

if result == len(sentence):
    print("Top-Down Parsing : Accepted")
else:
    print("Top-Down Parsing : Rejected")


# Simple Earley parser
def earley_parse(words):
    chart = [[] for _ in range(len(words) + 1)]

    # State format: (lhs, rhs, dot, start)
    chart[0].append(("S'", ["S"], 0, 0))

    for i in range(len(words) + 1):

        changed = True

        while changed:
            changed = False

            for state in chart[i].copy():

                lhs, rhs, dot, start = state

                # Predictor
                if dot < len(rhs) and rhs[dot] in grammar:
                    next_symbol = rhs[dot]

                    for rule in grammar[next_symbol]:
                        new_state = (
                            next_symbol,
                            rule,
                            0,
                            i
                        )

                        if new_state not in chart[i]:
                            chart[i].append(new_state)
                            changed = True

                # Completer
                elif dot == len(rhs):
                    for old_state in chart[start].copy():

                        old_lhs, old_rhs, old_dot, old_start = old_state

                        if (
                            old_dot < len(old_rhs)
                            and old_rhs[old_dot] == lhs
                        ):
                            new_state = (
                                old_lhs,
                                old_rhs,
                                old_dot + 1,
                                old_start
                            )

                            if new_state not in chart[i]:
                                chart[i].append(new_state)
                                changed = True

        # Scanner
        if i < len(words):

            for state in chart[i]:

                lhs, rhs, dot, start = state

                if dot < len(rhs):
                    symbol = rhs[dot]

                    if symbol not in grammar and symbol == words[i]:
                        new_state = (
                            lhs,
                            rhs,
                            dot + 1,
                            start
                        )

                        if new_state not in chart[i + 1]:
                            chart[i + 1].append(new_state)

    final_state = ("S'", ["S"], 1, 0)

    return final_state in chart[len(words)]


print("Earley Parsing   :", end=" ")

if earley_parse(sentence):
    print("Accepted")
else:
    print("Rejected")
