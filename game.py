"""A number-guessing game."""

# Put your code here
import random
def game():
	name = input("Howdy, what's your name?")
	secret_number = random.randint(0,101)
	print(name + " I'm thinking of a number between 1 and 100. Try to guess my number.")
	count = 0
	while True:
		guess = int(input("Your guess?"))
		# to check if the guess is in the range
		while guess > 100 or guess < 0:
			guess= int(input("You are out of range. Try again!"))

		count +=1
		if guess > secret_number:
			print("Your guess is too high, try again.")
		elif guess < secret_number:
			print("Your guess is too low, try again.")
		else:
			print("Well done, " + name + "! You found my number in", count, "tries!")
			break


game()
