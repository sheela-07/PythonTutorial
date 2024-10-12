# method1:concatenation using + operator

companyName = "Ednue Technologies"
suffix = "Pvt Ltd"
print(companyName +" "+ suffix)

# %s for string
# %d for integer
# %f for float
name = "Banu"  # string
age = 50
score = 35.2345
print("%s age is %d" % (name, age))
print("%s age is %d.She has scored %.2f in HSC." % (name, age, score))

# method3 - .format()
print("{} age is {}.She has scored {} in HSC.".format(name, age, score))
print("{0} age is {2}.She has scored {1} in HSC.".format(name, age, score))

# method4 - f' string
personName = "Alex"
companyName = "TCS"
# print("{personName}work in {companyName}") output{personName}work in {companyName}
print(f"{personName}work in {companyName}")

waterAmount=1.5
no_of_Time=4
totalAmount = waterAmount*no_of_Time


