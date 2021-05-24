import random

# Steps:

# Get random number
for x in range(1):
    numRandom = random.randint(1, 11)
    print(numRandom)
# Ask user for input
question = input("Guess a number from 1-10?: ")
# Check if input is correct
if question == numRandom:
    print("Awesome Job! You Win!")
elif question != numRandom:
    print("Aw! So close! Try again next time!")
else:
    print("Sorry, I did not understand!")
