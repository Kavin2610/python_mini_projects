import random
import string

letters = list(string.ascii_letters)
special_characters = ['!','@','#','$','%','^','&','*','~']
numbers = ["1","2","3","4","5","6","7","8","9","0"]
    


def generate_password(length):
    if length >= 3:
        special_len = length// 3
        numbers_len = length// 3
        letters_len = length - (special_len + numbers_len)
    password = []
    password.extend(random.choices(numbers, k = numbers_len))
    password.extend(random.choices(special_characters, k = special_len))
    password.extend(random.choices(letters, k = letters_len))
        
    random.shuffle(password)

    return ''.join(password)

print(generate_password(4))