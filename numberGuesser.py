import random

print("Number Guesser Game")
number = random.randint(1, 10)

chance = 0
print("Guess a Number Between 1 and 9 : ") 

while chance < 5:
    guess = int(input("Enter Your Guess :"))

    if guess == number:
        print("CONGRATULATIONS!! YOU WIN!! YOU ARE A MIND READER")

    elif guess < number:
        print("Your Guess was LOW : Try again with a number higher than : " , guess)

    else:
        print("Your guess was Higher than the number : Try again with a number lower than : " , guess)


    chance += 1

if  chance > 5:
    print("YOU LOSE , THE NUMBER WAS : " , number)
 




# print(number)