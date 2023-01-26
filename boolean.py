num1 = int(input("Enter any number: "))

num2 = int(input("Enter another number: "))

if num1 % num2 == 0:
    message = "The {var1} is a variable of the {var2}"
    print(message.format(var1 = "First number", var2 = "Second number"))

else:
    message = "{var1} is not a variable of {var2}"
    message = "The {var1} is a variable of the {var2}"
    print(message.format(var1 = "First number", var2 = "Second number"))

