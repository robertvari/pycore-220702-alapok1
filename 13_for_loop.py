names = ["Csilla", "Robert", "Kriszta", "Balázs"]
numbers = [1, 2, 3, 4, 5]

for index, name in enumerate(names):
    if name == "Robert":
        continue

    print(name, index)