'''

Filename: decrypt.py

This program decrypts a message so that it is human-readable

'''
# Create dictionary (hashmap) to look up from for better performance
decrypt_keys = {
   "*": "a",
   "&": "e",
   "#": "i",
   "+": "o",
   "!": "u"
}

def main():
  running = True
  while running:
    ask_and_decrypt_input()


    invalid = True
    
    while invalid:
        # Ask user if there are more to decrypt
        res = input('Continue decrypting? (y/n): ')

        if res[0].lower() == 'y':
            # If answer is yes, just continue decrypting
            invalid = False

        elif res[0].lower() == 'n':
            # If answer is no, terminate program
            print('Thank you for using Decryptor')
            invalid = False
            running = False

        else:
            print('Invalid input! Try again')


# Ask for encrypted input from user
def ask_and_decrypt_input():
  user_input = input('Please enter encrypted input: ')
  decrypted = decrypt(user_input)
  print(decrypted)

def decrypt(text):
  completed_word = ''
  for letter in text:
      
      # Iterate through every character from the phrase that user entered, and then manipulate with respect to the set of decryption keys
      if letter in decrypt_keys:
        completed_word += decrypt_keys[letter]
      
      else:
        completed_word += letter

  # Return decrypted message to user
  return completed_word

main()