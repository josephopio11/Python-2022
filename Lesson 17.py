# Dictionaries
phonebook = {
    "John": 68541236,
    "Jane": 79787675,
    "June": 22334455
}

# print(phonebook)

phonebook["Darlin"] = 45678912
phonebook["Winston"] = 85496532
phonebook["Davy"] = 41285679

# print(phonebook)

# del phonebook["John"]
# print(phonebook)

# phonebook.pop("June")
# print(phonebook)

# if "John" in phonebook:
#     print("John is in the phonebook")
# else:
#     print("John is not in the phonebook")

for name, number in phonebook.items():
    print("The number of %s is %d\n" % (name, number))
