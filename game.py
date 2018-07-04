"""A number-guessing game."""

# Put your code here
import random
def game():
	"""A number-guessing game.

		The code generates a random number between 0-100, and asks the user to guess the number. 
		The user must input an integer in range, and the code checks both conditions 
		The game gives a hint about if the number was too high or too low, 
		and ends when the user guesses the secret number
	"""
	name = input("Howdy, what's your name?")
	secret_number = random.randint(0,101)
	print(name + " I'm thinking of a number between 1 and 100. Try to guess my number.")
	count = 0
	while True:
		# to check that the guess is really an integer
		try:
			guess = int(input("Your guess?"))
		except ValueError:
			print("This is not a number.")
			continue
		# to check if the guess is in the range
		while guess > 100 or guess < 0:
			guess= int(input("You are out of range. Try again!"))

		count +=1
		if guess > secret_number:
			print("Your guess is too high, try again.")
		elif guess < secret_number:
			print("Your guess is too low, try again.")
		else:
			print("Well done,", name, "! You found my number in", count, "tries!")
			# print("Well done, " + name + "! You found my number in" + str(count) + "tries!")
			break


game()
