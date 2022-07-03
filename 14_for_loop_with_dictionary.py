phonebook = {
    "06 20 123 4567": {"name": "Csaba", "email": "csaba@gmail.com", "address": "Budapest"},
    "06 20 321 7654": {"name": "Csilla", "email": "csilla@gmail.com", "address": "Pécs"},
    "06 20 321 7623": {"name": "Tamás", "email": "tamas@gmail.com", "address": "Debrecen"},
    "06 20 321 7345": {"name": "Gábor", "email": "gabor@gmail.com", "address": "Miskolc"},
}

# case A
for phone_number in phonebook:
    print(phone_number, phonebook[phone_number])

for phone_number, person_data in phonebook.items():
    print(phone_number, person_data)