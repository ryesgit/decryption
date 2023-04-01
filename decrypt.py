'''

Filename: decrypt.py

This program decrypts a message so that it is human-readable

Pseudocode:

2. Iterate through every character from the phrase that user entered
    (a) If the character is '*', convert it to 'a';
    (b) If the character is '&', convert it to 'e';
    (c) If the character is '#', convert it to 'i';
    (d) If the character is '+', convert it to 'o', and;
    (e) If the character is '!', convert it to 'u'.
    (f) If the character is not in the dictionary, retain character
3. Return decrypted message to user

'''
# Create dictionary (hashmap) to look up from for better performance
decrypt_keys = {
   "*": "a",
   "&": "e",
   "#": "i",
   "+": "o",
   "!": "u"
}