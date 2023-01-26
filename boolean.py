num1 = int(input("Enter any number: "))

num2 = int(input("Enter another number: "))

if num1 % num2 == 0:
    message = "The number {var1} is a variable of {var2}"
    print(message.format(var1 = num1, var2 = num2))

else:
    message = "The number {var3} is not a variable of the {var4}"
    print(message.format(var3 = num1, var4 = num2))

