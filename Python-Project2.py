#Python-Project2
#Print("Password Generator")

import random

characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ2@'

Number_of_passwords = int(input("Number of passwords: "))
Password_length = int(input('Password length: '))

print("Password: \n")
for pwd in range(Number_of_passwords):
    Final_password = ''
    for number_chact in range(Password_length):
        Final_password += random.choice(characters)
    print(Final_password)

print('\n')

