A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# add items to set
# my_set.add(4)
# print(my_set)
#
# my_set.update([5, 6, 7])
# print(my_set)

# remove items from set
# my_set.discard(10)  # silent error
# my_set.remove(2)

# union: |
# print(A, B)
# print(A | B)

# Intersection: &
# print(A & B)

# Symmetrical difference
# print(A ^ B)

# Difference
# print(A - B)
# print(B - A)


my_friends = ["Tamás", "Kriszta", "Csaba", "Tamás", "Kriszta"]
# cast: convert a list to a set

my_friends_set = set(my_friends)
print(my_friends_set)

my_friends = list(my_friends_set)
print(my_friends)