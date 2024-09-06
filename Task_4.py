import random

rock = '''
                ___________
            ---'   ________)
                  (________)
                  (________)
                  (________)
            ---.__(________)
'''
paper = '''
                _______
            ---'   ____)_______
                      _________)
                      _________)
                     __________)
            ---.__________)
'''
scissor = '''
                _______
            ---'   ____)_______
                      _________)
                   ____________)
                  (______)
            ---.__(______)
'''

symbol_list = [rock,paper,scissor]
user = 0
computer = 0
while True:
    user_selection = int(input("Enter your choice ( 0 for rock / 1 for paper / 2 for scissor ) : "))
    print("Your choice :")
    print(symbol_list[user_selection])
    print("Computer choice :")
    computer_selection = random.randint(0,2)
    print(symbol_list[computer_selection])

    if user_selection == 0 and computer_selection == 2  or user_selection == 2 and computer_selection == 1 or user_selection == 1 and computer_selection == 0  :
        print("you won the Game.")
        user+=1
    elif user_selection == 0 and computer_selection == 1  or user_selection == 1 and computer_selection == 2 or user_selection == 2 and computer_selection == 0 :
        print("Computer won the Game.")
        computer+=1
    elif user_selection == computer_selection:
        print("It's Draw.")

    print(f"your score : {user}")
    print(f"computer score : {computer}")

    another_round = input("Enter yes/no to play the Game : ").lower()
    if another_round == "no":
        print("You quit the game.")
        break
    elif another_round == 'yes':
        continue
    else:
        print("Entered invalid input...")
        break
