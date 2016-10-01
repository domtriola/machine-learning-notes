#### Support Vector Machine ####
################################

# Creates a classification line that maximizes the distance between the two
# nearest data points (of different classes)
# Margin: distance between the nearest points

# Correct classification has higher precidence over margin maximization
# SVM ignores outliers when correct classification is not possible


# With only 2 features (x and y) the data below is not linearly seperable

# Ex: y / x
#        |    x
#  x     | x
#    x   |
#      o | o
#____o___|__o______
#      o |o
#  x     |     x
#   x    |    x
#        |


# But if you use a third feature (z = x^2 + y^2) the data does become linearly
# separable:

# Ex: z / x
#     x  |    x
#  x   x | x    x
#    x   |    x
#      o | o
#____o_o_|o_o______
#        |
#        |


# Another ex: y / x
#     x  |    x
#  x   x | x    x
#o   x   |    x   o
#  o   x | x    o
#____o___|__o______
#     o  |     o
#   o    |  o
#        |   o
#        |

# This data set could be solved using the non-linear feature |x|
# Ex: y / |x|
#        |  x x
#        | x  x x
#        |  x x  o
#        | x  o o
#________|__oo_____
#        |   o o
#        |  o
#        |   o
#        |
