

import random

name = input("Howdy, what's your name?")
print("{}, I\'m thinking of a number between 1 and 100".format(name))
print("Try to guess my number: ")

# number = random.randint(1, 100)
#guess = int(input("Your guess? "))
# count = 0

# while number != guess:

# 	count += 1

# 	if number > guess:
# 		print("You guess is too low, try again.")
# 	else: 
# 		print("You guess is too high, try again.")
# 	guess = int(input("Your guess? "))


# print("Well done, {}! You found my number in {} tries!".format(name, count))



guess = 102
answer = "y"
num_guess = 0


while answer == "y":
	number = random.randint(1, 100)
	count = 0
	while number != guess: # and answer == "y":
		guess = int(input("Your guess? "))
		count += 1

		if number > guess:
			print("You guess is too low, try again.")
		elif number < guess:
			print("You guess is too high, try again")
		else:
			if num_guess > count or num_guess == 0:
				num_guess = count
			print("Well done, {}! You found my number in {} tries! Your best score is {}".format(name, count, num_guess))
			answer = input("Would you like to play again? y/n: ")


		


