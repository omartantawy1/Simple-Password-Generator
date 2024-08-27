import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters= int(input("How many letters would you like in your password?")) 
nr_symbols = int(input(f"How many symbols would you like?"))
nr_numbers = int(input(f"How many numbers would you like?"))

Mypassword=''

for letter in range(nr_letters):
  letters_rand=random.choice(letters)
  Mypassword+=letters_rand

 
for symbol in range(nr_symbols):
  symbols_rand=random.choice(symbols)
  Mypassword+=symbols_rand
    
for number in range(nr_numbers):
  numbers_rand=random.choice(numbers)  
  Mypassword+=numbers_rand
 
 
tolist = list(Mypassword)
random.shuffle(tolist)
Mypassword=''

for char in tolist:
   Mypassword+=char
print(Mypassword)   
    