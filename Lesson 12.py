animals = ['cow', 'goat', 'pig','chicken', 'sheep']

# print('cow' in animals)
# print('pig' in animals)
# print('lion' in animals)
#
# # Exercise: what is the output of the following lines
#
# print('o' in 'Joshua')
# print('k' in 'chicken')
# print('she' in 'She is the right person for the job')


# animal = input("What animal do you keep at home? ")
#
# if animal in animals:
#     print("Welcome to the club")
# else:
#     print("Stay out of here...")


mark = int(input("Please enter the mark you scored: "))

if mark > 80:
    print('Super student')
elif mark>60:
    print("You passed well")
elif mark > 40:
    print("Gentleman pass")
elif mark>20:
    print("Thanks for attending the exam")
else:
    print("Failed")