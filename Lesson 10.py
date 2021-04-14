# Boolean Operations | AND, OR, NOT
name = input("What is your name? ")
children = int(input("How many kids do you have? "))

if name == "Michael":
    print("You are the man!")

if name == "Mike" and children == 18:
    print("This guy needs prayers")

if name == "Mike" or children > 9:
    print("This guys is like a rabbit")
