#########################
#  DIY 4 Answer
import random
n = 10
guessMe = int(100 * random.random() + 1)
print(guessMe)
guess = 0
while guess != guessMe:
    guess = int(input("Enter new number or -1 to give up: "))
    if guess > 0:
        if guess > guessMe:
            print("Number too large")
        else:
            print("Number too small")
    else:
        print("Sorry, that you're giving up!")
        break
else:
    print("Congratulation. You made it!")
