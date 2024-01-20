import random


def password_generator():

    characters_base = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@'
    password = ""


    for i in range(random.randint(8,16)):
        password += random.choice(characters_base)

    print("Password:", password)

password_generator()


