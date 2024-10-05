import string
import random
import time

letters = string.printable
NAME = 'Aruneem Bhowmick'
result = ''

for letter in NAME:
    while True:
        random_letter = random.choice(letters)
        print(result + random_letter)
        if(random_letter == letter):
            result += random_letter
            break
        time.sleep(0.001)