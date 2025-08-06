import random
import string

def password_generator(lenght=12):
    # the characters that will be contained in the password
    letters=string.ascii_letters
    digits=string.digits
    symbols=string.punctuation
    # adding all the characters together
    all_chars= letters + digits + symbols 
    # first letter should always contain letters digits and symbols
    password= random.choice(letters) + random.choice(digits) + random.choice(symbols)
    # filling the rest with password lenght
    password += "".join(random.choice(all_chars) for _ in range(lenght-3))
    # shuffling the password more for making it strong
    password="".join(random.sample(password,len(password)))
    # returning the value back
    return password
try:
    print("Welcome to the password generator")
    
    lenght=int(input("\nEnter the lenght of your password: "))
    if lenght < 4:
        print("The password generated should contain more then 4 characters")
    else:
         print(f"Generated password :- {password_generator(lenght)}")
except ValueError:
    print("Invalid value has been entered enter again")

    
    