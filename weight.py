# Write a program in python that prompts the user to input the weight of a person. 
# If the weight is greater than 75 kg, it should prompt the user to input their name and age,
# and it should also prints the persons name and age. 

weight = int(input("How much do you weigh?: "))

if weight > 75:
    name = input(("What is your name?: "))
    age = input(("What is your age?: "))
    print("Your name is: " + name + ", and you are: " + age + "!")