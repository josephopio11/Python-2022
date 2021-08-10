# Functions

ninjas = ["Derrick", "Armel", "Darcy", "Okello", "Florian"]


def greet(the_person):
    print("\n")
    print("Hello %s" % the_person)
    print("How is your day? Hope all is well")
    print("%s, Please go back to your father's house, I don't know you" % the_person)


for persons in ninjas:
    greet(persons)
