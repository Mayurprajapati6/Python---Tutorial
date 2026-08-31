# {} braces use to defina a set
# Always store unique values
# in python set is consider as a datatype

setone = {1, 2, 3, 4}

# intersection
setone & {1, 3} -> {1,3}

# Union
setone | {1, 3, 7} -> {1, 2, 3, 4, 7}

# Difference
setone - {1, 3}   -> {2, 4}

# Empty
setone - {1, 2, 3, 4} -> set() (empty set)

# type
type({}) # empty paranthesis type -> dictonary

 