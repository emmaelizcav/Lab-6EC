# Name: Emma Cavaneau
# Partner: Julia Martin
# Lab 06


# Defines function to encode entered password
def encode(password):
    # Creates blank string to add encoded digits to make the encoded 
password
    c_password = ""
    # For loop that iterates through the length of the entered password
    for i in range(0, len(password)):
        # Stores the numerical value of the selected digit in the variable 
num
        num = int(password[i])
        # Adds three to num and then adds the number as a string to the 
encoded password string
        num += 3
        c_password += str(num)
    # Returns encoded password
    return c_password


# Added decode function by Julia.
def decode(password):
	global decoded_password
	# Makes decoded password a string and subtracts 3 from each digit.
	decoded_password = ''
	for digit in c_password:
		digit = str((int(digit) - 3))
		decoded_password += digit
	return decoded_password


# Defines main function
def main():
    # Variable to run the while loop while the encoder is running
    run = True
    while run:
        # Prints the menu and asks the user what they want to do
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        print('')
        option = int(input('Please enter an option: '))
        # Encodes password if user enters 1 and stores it
        if option == 1:
            password = input('Please enter your password to encode: ')
            c_password = encode(password)
            print('Your password has been encoded and stored!')
            print('')
        # Will decode password if user enters 2 and returns encoded and 
original password
        if option == 2:
            print('The encoded password is ', c_password, 'and the original password is ', decoded_password)
            print('')
        # Ends program
        if option == 3:
            run = False


# Runs main function
if __name__ == '__main__':
    main()



