import random

print ('Welcome to Password Generator')

chars = 'abcdefghijlkmnopqrstuvxwyzABCDEFGHIJLKMNOPQRSTUVXWYZ!@#$%&*1234567890'

number = input ('Amount of password to generate: ')
number = int (number)

lenght = input ('Input your password lenght:')
lenght = int (length)

print ('\where are your passwords: ')

for pwd in range (number):
    passwords = ''
    for c in range (lenght):
        passwords += random.choice(chars)
        print (passwords)