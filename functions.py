# Task: Asks the user to input a number and determines if it is even or odd
def is_even():
	while True:
		try:
			user_input = input("Please enter a whole number: ")

			number = int(user_input)

			if number % 2 == 0:
				print(f"The number {number} is Even.")
			else:
				print (f"The number {number} is Odd.")
		except ValueError:
				print(f"'{user_input}'is not a valid whole number.")
# call the function
is_even()
