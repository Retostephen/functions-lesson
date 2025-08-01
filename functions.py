'''
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


# NOTES!!!
#Try/Except Block
#Loops while-loop
#Functions 
#Conditionals
#Operators
#A function is just a set of instructions. a function musn't define anything, it can also execute a set of instruction which you musn't always write

'''

#Task 2: Ask the user for two numbers and calculate their sum
def is_sum():
	while True:
		try:
			user_input1 = input("Please enter any number: ")
	
			user_input2 = input("Please enter any number: ")
	
			number1 = int(user_input1)
	
			number2 = int(user_input2)
	
			total_sum = number1 + number2
			print(f"The total sum of {number1} and {number2} is {total_sum}.")
		except ValueError:
			print("The value of the inputs are invalid")
is_sum()



'''
#Task 3: Ask the user to input a number and find determine if it's positive, negative or zero
def check_number_sign():
	while True:
		try:
			user_input = input("Please enter any number: ")
	
			number = int(user_input)

			if number > 0:
				print(f"The number {number} is Positive.")
			elif number < 0:
				print(f"The number {number} is Negative")
			else:
				print(f"The number {number} is Zero")
		except ValueError: 
			print(f"The value {user_input} is not a valid number.")

check_number_sign() 
'''
