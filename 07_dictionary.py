from pprint import pprint

phonebook = {
    "06 20 123 4567": {"name": "Csaba", "email": "csaba@gmail.com", "address": "Budapest"},
    "06 20 321 7654": {"name": "Csilla", "email": "csilla@gmail.com", "address": "Pécs"},
    "06 20 321 7623": {"name": "Tamás", "email": "tamas@gmail.com", "address": "Debrecen"},
    "06 20 321 7345": {"name": "Gábor", "email": "gabor@gmail.com", "address": "Miskolc"},
}

# print(phonebook["06 20 123 4567"])
# print(phonebook["06 20 123 4567"]["address"])

# get user data: phone, name, email, address
# store user data into phonebook dictionary

# phone = input("Phone?")
# name = input("Name?")
# email = input("Email?")
# address = input("Address?")

# print("=" * 100)
# print(f"Phone: {phone}\nName: {name}\nEmail: {email}\nAddress: {address}")

# add new data to dictionary
# phonebook[phone] = {"name": name, "email": email, "address": address}
# print(phonebook)


# replace/add data in dictionary
phonebook["06 20 123 4567"] = {"name": "Ákos", "email": "akos@gmail.com", "address": "Siófok"}
# pprint(phonebook)

# delete data from dictionary
del phonebook["06 20 123 4567"]
pprint(phonebook)