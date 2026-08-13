# -----------------------------------------
# CASE STUDY 3
# News Analytics and POS Tag Correction System
# -----------------------------------------

import math

print("==============================================")
print("NEWS ANALYTICS AND POS TAG CORRECTION SYSTEM")
print("==============================================")

# Student Details
print("Name: M. Yasodha Krishna")
print("Reg No: 192472100")
print()

# -----------------------------------------
# 1. Transformation-Based Tagging
# -----------------------------------------

print("1. TRANSFORMATION-BASED TAGGING")
print("------------------------------")

print("Initial POS tags:")
print("economic/JJ")
print("growth/NN")
print("increases/NNS")
print("employment/NN")
print()

print("Transformation Rule:")
print("Change NNS to VBZ if the preceding word is NN.")
print()

print("Corrected POS tags:")
print("economic/JJ")
print("growth/NN")
print("increases/VBZ")
print("employment/NN")
print()

print("Reason:")
print("growth is the singular subject.")
print("increases is the third-person singular verb.")
print()

# -----------------------------------------
# 2. Analysis of Initial Tagging Errors
# -----------------------------------------

print("2. ANALYSIS OF INITIAL TAGGING ERRORS")
print("------------------------------")

print("Incorrect tag: increases/NNS")
print("NNS represents a plural noun.")
print()
print("Correct tag: increases/VBZ")
print("VBZ represents a third-person singular")
print("present-tense verb.")
print()

print("Final grammatical structure:")
print("Economic/JJ")
print("growth/NN")
print("increases/VBZ")
print("employment/NN")
print()

# -----------------------------------------
# 3. Word Frequency Distribution
# -----------------------------------------

print("3. WORD FREQUENCY DISTRIBUTION")
print("------------------------------")

economic = 120
growth = 450
increases = 210
employment = 380

total_frequency = (
    economic +
    growth +
    increases +
    employment
)

print("Total frequency =", total_frequency)
print()

p_economic = economic / total_frequency
p_growth = growth / total_frequency
p_increases = increases / total_frequency
p_employment = employment / total_frequency

print("Word        Frequency     Probability")
print("---------------------------------------")
print("economic    ", economic, "       ", p_economic)
print("growth      ", growth, "       ", p_growth)
print("increases   ", increases, "       ", p_increases)
print("employment  ", employment, "       ", p_employment)
print()

# -----------------------------------------
# 4. Entropy Before and After Transformation
# -----------------------------------------

print("4. ENTROPY BEFORE AND AFTER TRANSFORMATION")
print("------------------------------")

# Before correction
p_nns_before = 0.5
p_vbz_before = 0.5

entropy_before = (
    -(p_nns_before * math.log2(p_nns_before))
    -(p_vbz_before * math.log2(p_vbz_before))
)

print("Before correction:")
print("P(NNS) =", p_nns_before)
print("P(VBZ) =", p_vbz_before)
print("Entropy =", entropy_before, "bits")
print()

# After correction
p_vbz_after = 0.95
p_nns_after = 0.05

entropy_after = (
    -(p_vbz_after * math.log2(p_vbz_after))
    -(p_nns_after * math.log2(p_nns_after))
)

print("After correction:")
print("P(VBZ) =", p_vbz_after)
print("P(NNS) =", p_nns_after)
print("Entropy =", entropy_after, "bits")
print()

print("Interpretation:")
print("Entropy decreases after transformation.")
print("Lower entropy indicates higher confidence")
print("in the correct POS tag.")
