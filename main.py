#Abraham Banos Lombardero Encode Function
#This is me making changes to my program as outlined in the rubric ;-;

#Initialization of variables
password = ''

#Function Definitions

def encoder(password):
  encodedPassword = ''

#For loop using python's keyword digit which every character in a string is a digit to itterate through the string and finding the previous character at that index changing it and appending it to the new string.

  for digit in password:
    new_digit = str((int(digit) + 3) % 10)
    encodedPassword += new_digit
  return encodedPassword
    
def main():
  while True:
    #Creation of the program's menu
    print('\nMenu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    #Prompting and storing user input for menu selection
    choice = input('Please enter an option: ')
      
    #If-elif tree to determine user choice and then call the appropriate function
    if choice == '1' or choice == 'Encode':
      password = input('\nPlease enter your password to encode: ')
      encoder(password)
      print('Your password has been encoded and stored!')

    elif choice == '2' or choice == 'Decode':
      if len(password) >= 1:
        password
      else:
        print('\nNo password has been encoded yet. Please select option 1 to encode a password.')

    elif choice == '3' or choice == 'Quit':
      break

    else:
      print('Invalid option. Please choose again.')
# Function Call
main()