# -----------------------------------------
# CASE STUDY 2
# AI-Powered Customer Support Chatbot
# -----------------------------------------

print("==============================================")
print("AI-POWERED CUSTOMER SUPPORT CHATBOT")
print("==============================================")

# Student Details
print("Name: M. Yasodha Krishna")
print("Reg No: 192472100")
print()

# -----------------------------------------
# 1. Penn Treebank POS Tagging
# -----------------------------------------

print("1. PENN TREEBANK POS TAGGING")
print("------------------------------")

print("Sentence 1: Book a flight ticket now.")
print("Book/VB a/DT flight/NN ticket/NN now/RB")
print("Book is a Verb because the sentence is an")
print("imperative command meaning make a reservation.")
print()

print("Sentence 2: This book is interesting.")
print("This/DT book/NN is/VBZ interesting/JJ")
print("Book is a Noun because it refers to a")
print("physical or written object.")
print()

# -----------------------------------------
# 2. HMM Probability
# -----------------------------------------

print("2. HMM PROBABILITY")
print("------------------------------")

p_start_vb = 0.5
p_book_given_vb = 0.6

p_start_nn = 0.5
p_book_given_nn = 0.4

vb_probability = p_start_vb * p_book_given_vb
nn_probability = p_start_nn * p_book_given_nn

print("P(Start | VB) =", p_start_vb)
print("P(book | VB) =", p_book_given_vb)
print("P(VB, book) =", vb_probability)
print()

print("P(Start | NN) =", p_start_nn)
print("P(book | NN) =", p_book_given_nn)
print("P(NN, book) =", nn_probability)
print()

if vb_probability > nn_probability:
    print("HMM favors the tag: VB")
else:
    print("HMM favors the tag: NN")

print()

# -----------------------------------------
# 3. Rule-Based vs Stochastic Tagging
# -----------------------------------------

print("3. RULE-BASED VS STOCHASTIC TAGGING")
print("------------------------------")

print("Rule-Based Tagging:")
print("- Uses hand-written linguistic rules.")
print("- Does not necessarily require training data.")
print("- Can be difficult to maintain for large systems.")
print()

print("Stochastic / HMM Tagging:")
print("- Uses probabilities and statistical context.")
print("- Requires training data.")
print("- Handles ambiguity better.")
print("- More suitable for large-scale chatbot systems.")
print()

# -----------------------------------------
# 4. Importance of Standardized POS Tagsets
# -----------------------------------------

print("4. IMPORTANCE OF POS TAGSETS")
print("------------------------------")

print("NN  = Noun")
print("VB  = Verb")
print("JJ  = Adjective")
print("RB  = Adverb")
print("PRP = Pronoun")
print("DT  = Determiner")
print()

print("POS tagging helps in:")
print("- Intent detection")
print("- Language understanding")
print("- Response generation")
print("- Information extraction")

print()
print("CONCLUSION:")
print("Standardized POS tags improve chatbot")
print("language understanding and response generation.")
