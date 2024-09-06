import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
special_char = "!@#$%^&*_+?/~"

while True:
    length = int(input("Enter the length of the password : "))
    all_characters = lower_case + upper_case + numbers + special_char
    password = ""
    for each_char in range(length):
        random_letter = random.choice(all_characters)
        password += random_letter
    print(f"your password : {password} \n")

    another_password = input("Enter (yes/no) to generate another password : ")
    if another_password == "no":
        break
    elif another_password == "yes":
        continue
    else:
        print("Please enter valid input...")
        another_ = input("Enter (yes/no) to generate another password : ")
        if another_password == "no":
            break

