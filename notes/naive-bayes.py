####### Naive Bayes #######
##########################

# Prior Probability * Test Evidence => Posterior Probability

def naive_bayes(prior, sensitivity, specificity, result):
    joint_sen = prior * sensitivity
    joint_spec = (1 - prior) * (1 - specificity)
    normalize = joint_sen + joint_spec
    if result:
        return joint_sen / normalize
    else:
        return joint_spec / normalize

# Note: result is True for a positive test result or False for a negative result


### Elaborated ###

# Assume 1% of people have a particular kind of cancer
# A test gives an accurate positive result 90% of the time
# It also gives an accurate negative result 90% of the time

# P(c) = 0.01
# P(Pos|c) = 0.9 Test sensitivity: 90% positive if cancer
# P(Neg|!c) = 0.9 Test specificity: 90% negative if !cancer

# if test is positive you have an ~8.333% chance of actually having cancer
print(naive_bayes(0.01, 0.9, 0.9, True))  # => 0.08333

## Prior Probability
c = 0.01       # P(c)
pos_sen = 0.9  # P(Pos|c)
pos_spec = 0.1 # P(Pos|!c)

## Joint Sensitivity and Specificity
joint_sen = c * pos_sen                # P(Pos,c)   # => 0.009
joint_spec = (1 - c) * pos_spec        # P(Pos,!c)  # => 0.099
normalize = joint_sen + joint_spec     # P(Pos)     # => 0.108

## Posterior Probability
# For a positive result we'll normalize on the joint_sensitivity
probability = joint_sen / normalize
# print(probability) # => 0.08333

# If test is negative you have a ~91.667% chance of not having cancer
not_probability = joint_spec / normalize
# print(not_probability) # => 0.91667

# print(probability + not_probability) # => 1.0
