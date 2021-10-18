import random
import time
from ValidText import List_Of_Valid_Ans
min = 1
max = 6
Valid_Answers = List_Of_Valid_Ans[0:4]
Name = input("Please Enter Your Name! ")
roll_again = input("Are you ready to roll some dice" + " " +
                   Name + "? I could reaaally use someone to test this!")
# print(Valid_Answers)
# I put the the for loop so that the continue argument will retry from the beginning, not sure if best way to go about it

if roll_again in Valid_Answers[2:4]:
    print("Totally understandable, I wouldn't use this sh** either lol! Good luck and shout out to your family")
    time.sleep(3)

while not roll_again in Valid_Answers:
    print("Sorry that is not a valid response \n Only yes, y , no, n")
    roll_again = input("Do you want to try again? ")
    if roll_again in Valid_Answers[2:4]:
        time.sleep(3)
        print(
            "Thank you for testing my dice roller! Good luck and shout out to your family!")

while roll_again in Valid_Answers[0:2]:
    print("rolling the dice... one moment please")
    time.sleep(1.5)
    print("The values are....")
    print(random.randint(min, max))
    print(random.randint(min, max))
    roll_again = input("Do you want to try again? ")
    if roll_again in Valid_Answers[2:4]:
        print(
            "Thank you for testing my dice roller! Good luck and shout out to your family!")
        time.sleep(3)
        break
    # if roll_again in Valid_Answers[0:2]:
        continue
    while not roll_again in Valid_Answers:
        print("Sorry that is not a valid response \n Only yes, y , no, n")
        roll_again = input("Do you want to try again? ")
        if roll_again in Valid_Answers[2:4]:
            time.sleep(3)
            print(
                "Thank you for testing my dice roller! Good luck and shout out to your family!")
            break
