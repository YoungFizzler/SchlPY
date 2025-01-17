# Write a program in python that accepts the maximum and minimum temperature for the day. 
# If the maximum temperature is greater than 30 degrees centigrade, output the message 
# “it was a hot day!”.  It should also output the difference in temperature. 

tdyTempMin = int(input("What is the minimum temperature today?: ")) # Convert to int for maths
tdyTempMax = int(input("What is the maximum temperature today?: ")) # Covert to int for maths

tdyTempDiff = tdyTempMax - tdyTempMin

if tdyTempMax > 30:
    print("It was a hot day. " + "The temperature difference today was: " + str(tdyTempDiff)) 
    # I was getting errors which I fixed with str() to convert to string.
else:
    print("It wasn't a hot day today!")
    # I wasn't sure if you wanted me to print Temperature differnce if it wasn't a hot day so I left it out.






