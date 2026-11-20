import random
while True:
    choice = input("enter yes or no(y/n)").lower()

    if choice == 'y':
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f"the numbers are {die1} and {die2}")
    elif choice == 'n':
        print("thank you for playing")
        break
    else:
        print("you have entered an in valid operation")
        print("please enter yes or no(y/n)")
