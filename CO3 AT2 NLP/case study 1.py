import math

# -----------------------------------------
# CASE STUDY 1
# Smart Mobile Keyboard Prediction System
# -----------------------------------------

print("==============================================")
print("SMART MOBILE KEYBOARD PREDICTION SYSTEM")
print("==============================================")

# Student Details
print("Name: M. Yasodha Krishna")
print("Reg No: 192472100")
print()

# -----------------------------------------
# 1. Bigram MLE
# P(science | data) = C(data science) / C(data)
# -----------------------------------------

count_data_science = 3
count_data = 3

p_science_given_data = count_data_science / count_data

print("1. BIGRAM MLE")
print("------------------------------")
print("C(data science) =", count_data_science)
print("C(data) =", count_data)
print("P(science | data) =", p_science_given_data)
print()

# -----------------------------------------
# 2. Backoff Model
# Sequence: data science improves
# "improves" is unseen, so use lower-order
# probability.
# -----------------------------------------

print("2. BACKOFF MODEL")
print("------------------------------")

# Known probability
p_science_given_data = 1.0

# "improves" is unseen in the corpus.
# Therefore, unigram probability is zero.
p_improves = 0.0

backoff_probability = (
    p_science_given_data *
    p_improves
)

print("P(science | data) =", p_science_given_data)
print("P(improves) using backoff =", p_improves)
print("Estimated probability of 'data science improves' =",
      backoff_probability)
print()

# -----------------------------------------
# 3. Deleted Interpolation
# P = λ1 * Trigram + λ2 * Bigram + λ3 * Unigram
# -----------------------------------------

print("3. DELETED INTERPOLATION")
print("------------------------------")

lambda1 = 0.5
lambda2 = 0.3
lambda3 = 0.2

# For "data science is"
# Trigram probability:
# C(data science is) / C(data science)
# = 2 / 3

trigram_probability = 2 / 3

# Bigram probability:
# P(is | science) = 0.66

bigram_probability = 0.66

# Unigram probability of "is"
# is occurs 2 times in a corpus of 13 words

unigram_probability = 2 / 13

interpolated_probability = (
    lambda1 * trigram_probability +
    lambda2 * bigram_probability +
    lambda3 * unigram_probability
)

print("Lambda 1 (Trigram) =", lambda1)
print("Lambda 2 (Bigram) =", lambda2)
print("Lambda 3 (Unigram) =", lambda3)

print("Trigram probability =", trigram_probability)
print("Bigram probability =", bigram_probability)
print("Unigram probability =", unigram_probability)

print("Interpolated probability =",
      interpolated_probability)
print()

# -----------------------------------------
# 4. Entropy
# H = -sum(P(x) log2 P(x))
# -----------------------------------------

print("4. ENTROPY")
print("------------------------------")

p_is = 0.66
p_drives = 0.33

entropy = (
    -(p_is * math.log2(p_is))
    -(p_drives * math.log2(p_drives))
)

print("P(is) =", p_is)
print("P(drives) =", p_drives)
print("Entropy =", entropy, "bits")

print()
print("Interpretation:")
print("Lower entropy means higher prediction confidence.")
print("Higher entropy means greater uncertainty.")
