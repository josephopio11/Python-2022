condition = 0

while condition < 5:
    condition += 1
    mark = input("Please enter the marks you got in the test or enter x to exit: ")

    if mark == "x":
        condition = 6
    elif int(mark) < 30:
        print('You got a U')
    elif int(mark) < 40:
        print('You got a G')
    elif int(mark) < 50:
        print('You got a F')
    elif int(mark) < 60:
        print('You got an E')
    elif int(mark) < 70:
        print('You got a D')
    elif int(mark) < 80:
        print('You got a C')
    elif int(mark) < 90:
        print('You got a B')
    else:
        print('You got an A')
