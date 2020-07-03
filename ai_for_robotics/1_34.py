# cancer example

# Hint: think of:
# - cancer/noncancer as robot position
# - positive as whether the colored door observed was the correct one

# position in what place-space? position is either cancer or not
# measurement in example is positive

# p(C) = 0.001
# p(~C) = 0.999

# p(POS|C) = 0.8  (prob. of positive if cancer)
# p(POS|~C) = 0.1 (prob. of positive if not cancer)

# calculate probablility of cancer with a positive result
# p(C|POS) = 

# bayes theorem: P(A|B) = P(B|A) * P(A) / P(B)

# positions: [C, ~C]
p = [0.001, 0.999]
measurement = 'pos'

# see POS, figure out how you got there, either from pos or from neg

