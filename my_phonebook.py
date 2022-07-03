import json


phonebook = {}

print("="*50, "My Phonebook 1.0", "="*50)

phone = "06 20 123 4567"
name = "Kiss Csaba"
email = "csaba@gmail.com"
address = "Pécs"

phonebook[phone] = {"name": name, "email": email, "address": address}

# save data to json file to preserve dictionary format
with open("phonebook.json", "w") as f:
    json.dump(phonebook, f)


# read json file and load phonebook
with open("phonebook.json") as f:
    phonebook = json.load(f)

print(phonebook["06 20 123 4567"]["name"])