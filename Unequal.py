# Write a program in python that prompts the user to input two unequal values
# that are stored in variables A and B.  It should print the lower value.  

firstNum = int(input("Enter the first number: "))
secondNum = int(input("Enter the second number: "))

while firstNum == secondNum:
    print("Numbers must be unequal!")
    firstNum = int(input("Enter the first number: "))
    secondNum = int(input("Enter the second number: "))

print("The lower value is:", min(firstNum, secondNum))