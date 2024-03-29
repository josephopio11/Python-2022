# We have a class defined for vehicles. Create two new vehicles called car1 and car2. Set car1 
# to be a red convertible worth $60,000.00 with a name of Fer, and car2 to be a blue van named 
# Jump worth $10,000.00.


# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00

    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str


# your code goes here Please complete the work

car1 = Vehicle()
car1.kind = "convertible"
car1.color = "red"
car1.name = "Fer"
car1.value = 60000.00

car2 = Vehicle()
car2.value = 100000.00
car2.name = "Jump"
car2.kind = "van"
car2.color = "blue"


# test code
print(car1.description())
print(car2.description())
