# Formatting Strings
# %s - Strings
# %f - Float
# %d - Integers
# %.<number>f - Floating point numbers with number of digits
# %x - Display integers in hexadecimal in lowercase
# %X - Display integers in hexadecimal in uppercase

# Example 1 using only strings
name = "Dalton"
print("Hello %s" % name)

# Example 2 using a string and an integer
name2 = "Vivian"
age = 23
print("%s, you are %d years old. Can you see this %s?" % (name2, age, name))

# Example 3 using a list
my_list = ["Mike", "Samson", "Jane", "Eunice"]
print("The students in my class are %s" % my_list)

