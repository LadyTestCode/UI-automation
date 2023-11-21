import random
import string

def generate_random_string(length):
    random_string = ""
    for i in range(length):
        random_string += random.choice(string.ascii_letters[random.randint(0, 5)])
    return random_string

def generate_random_number_string(length):
    result = ""
    for i in range(0, length):
        result += str(random.randint(0, 9))
    return result