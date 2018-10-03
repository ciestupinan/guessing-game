

import random



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



name = input("Howdy, what's your name? ")
# print("{}, I\'m thinking of a number between 1 and 100".format(name))
# print("Try to guess my number: ")


guess = 102
answer = "y"
num_guess = 0
try_num = 5
start = int(input("What is the starting range integer (non-zero)? "))
end = int(input("What is the ending range integer (non-zero)? "))
number = random.randint(start, end)
count = 0

#while answer == "y":

# number = random.randint(start, end)
# count = 0

while number != guess:
	# start = int(input("What is the starting range integer (non-zero)? "))
	# end = int(input("What is the ending range integer (non-zero)? "))
	# number = random.randint(start, end)
	# count = 0

	if try_num == count:
		print("Too many tries!")
		answer = input("Would you like to play again? y/n: ")
		if answer == "y":
			start = int(input("What is the starting range integer (non-zero)? "))
			end = int(input("What is the ending range integer (non-zero)? "))
			number = random.randint(start, end)
			count = 0
			#continue
		else:
			break

	try:
		guess = int(input("Your guess? "))
	except ValueError:
		print("Needs to be an integer")
		continue


	count += 1
	if guess > end or guess < start:
		print("That's not in range!")
		continue

	if number > guess:
		print("You guess is too low, try again.")
	elif number < guess:
		print("You guess is too high, try again")
	else:
		if num_guess > count or num_guess == 0:
			num_guess = count
		print("Well done, {}! You found my number in {} tries! Your best score is {}".format(name, count, num_guess))
		answer = input("Would you like to play again? y/n: ")
		if answer == "y":
			start = int(input("What is the starting range integer (non-zero)? "))
			end = int(input("What is the ending range integer (non-zero)? "))
			number = random.randint(start, end)
			count = 0

		


