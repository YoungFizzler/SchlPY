import time

name = input("\nWhat is your name?: ")

if name == "John" or name == "George" or name == "Ringo" or name == "Paul":
    print("That is the name of a Beatle")
    time.sleep(2)
    exit()
else:
    print("That is a nice name, however it is not a name of a beetle!")
    time.sleep(2)
    exit()