my_friends = ["Robert", "Csaba", "Csilla", "Tamás", "Béla", "Róbert"]
shopping_list = [
    "Tej",
    "Kenyér",
    "Szalámi",
    "Sonka"
]

print(len(shopping_list) // 2)
print(shopping_list[ len(shopping_list) // 2])

# print(shopping_list)
shopping_list.append("Sonka")
# print(shopping_list)

shopping_list.insert(0, "Cola")
# print(shopping_list)

# print(shopping_list[2])
# print(shopping_list[-2])

# print(shopping_list)
# print(len(shopping_list))
# print(shopping_list[5])

# get the middle item in the shopping list
# print(shopping_list[ len(shopping_list) // 2 ])

# replace item in list
shopping_list[ shopping_list.index("Szalámi") ] = "WC papír"
# print(shopping_list)

# delete item in list
shopping_list.remove("Sonka")
del shopping_list[shopping_list.index("Tej")]
# print(shopping_list)