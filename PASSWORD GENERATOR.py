import random
import string

print("Welcome to the Password Generator!")
print("Let's create a strong and secure password for you \n")

while True:
    try:
        length = int(input(" Enter the desired password length:" ))
        if length < 4:
            print("Password should be at least 4 characters long")
        else:
            break
    except ValueError:
        print("please enter a valid number.")

all_characters = string.ascii_letters + string.digits + string.punctuation

password = ''.join(random.choice(all_characters) for _ in range(length))

print("\n Your secure password is:\n") 
print(f" {password}") 
print("\n Save your password for future use!")