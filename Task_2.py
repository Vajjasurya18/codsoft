print('''
                                                                 _____________________
                                                                |  _________________  |
                                                                | |                 | |
                                                                | |_________________| |
                                                                |  ___ ___ ___   ___  |
                                                                | | 7 | 8 | 9 | | + | |
                                                                | |___|___|___| |___| |
                                                                | | 4 | 5 | 6 | | - | |
                                                                | |___|___|___| |___| |
                                                                | | 1 | 2 | 3 | | x | |
                                                                | |___|___|___| |___| |
                                                                | | . | 0 | = | | / | |
                                                                | |___|___|___| |___| |
                                                                |_____________________|
''')

result_operation = "no"
while True:
    if result_operation == "no":
        numbers_1 = int(input("Enter 1st number : "))
    else:
        numbers_1 = result
        print("\n")
        print(f"Result as 1st number : {result}")
    numbers_2 = int(input("Enter 2nd number : "))

    result = 0

    choosed = input("Enter the operation ('+' or '-' or '*' or '/') b/w the numbers : ")
    if choosed == "+":
        result = numbers_1 + numbers_2
    elif choosed == "-":
        result = numbers_1 - numbers_2
    elif choosed == "*":
        result = numbers_1 * numbers_2
    elif choosed == "/":
        result = numbers_1 / numbers_2
    print(f"Result : {result} \n")
    To_continue = input("Do you want to continue the calculation ? (yes/no) : ").lower()
    if To_continue == "no":
        break
        print(result)
    else:
        result_operation = input(" Enter the result as 1st number (yes/no) : ")

