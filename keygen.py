import random
import string
import bcrypt

# Function to generate a random string
def generate_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(letters_and_digits) for i in range(length))
    return random_string

# Function to hash the string using bcrypt
def hash_string(random_string):
    # Generate a salt
    salt = bcrypt.gensalt()
    # Hash the string
    hashed_string = bcrypt.hashpw(random_string.encode(), salt)
    return hashed_string

def generate_key():
    random_string = generate_random_string(10)
    hashed_string = hash_string(random_string)
    
    with open('.env', 'w') as f:  
        f.write(f"SECRET_KEY={hashed_string.decode()}\n")
    # return hashed_string.decode()

generate_key()