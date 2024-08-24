logo = ('''
                                 /$$$$$$$$              /$$$$$$$                  /$$       /$$             /$$    
                                |__  $$__/             | $$__  $$                | $$      |__/            | $$    
                                   | $$  /$$$$$$       | $$  | $$  /$$$$$$       | $$       /$$  /$$$$$$$ /$$$$$$  
                                   | $$ /$$__  $$      | $$  | $$ /$$__  $$      | $$      | $$ /$$_____/|_  $$_/  
                                   | $$| $$  | $$      | $$  | $$| $$  | $$      | $$      | $$|  $$$$$$   | $$    
                                   | $$| $$  | $$      | $$  | $$| $$  | $$      | $$      | $$ |____  $$  | $$ /$$
                                   | $$|  $$$$$$/      | $$$$$$$/|  $$$$$$|      | $$$$$$$$| $$ /$$$$$$$/  |  $$$$/
                                   |__/|______/       |_______/  |______/       |________/|__/|_______/    |____/  

''')
print(logo)
tasks = int(input("Enter the no of tasks is to add to the list : "))

tasks_list = []

for i in range(1, tasks+1):
    task = input(f"Enter the task {i} : ")
    tasks_list.append(task)

print("\n")

while True:
    print("Choose the option to operate the list : ")
    print("1.Add task ")
    print("2.Delete task")
    print("3.Change task ")
    print("4.View list ")
    print("5.Exit / Stop \n ")

    selected_option = input("Enter the choosen option : ").lower()

    if selected_option == "add task":
        add_task = input("Enter the task to add in the list : ")
        tasks_list.append(add_task)
        print(f"{add_task} is added successfully to the list. \n")

    elif selected_option == "delete task":
        delete_task = input("Enter the task to delete in the list : ")
        for j in tasks_list:
            if j.lower() == delete_task.lower():
                tasks_list.remove(delete_task)
                print(f"{delete_task} is deleted successfully from the list. \n")

    elif selected_option == "change task":
        change_task = input("Enter the task to change in the list : ")
        for k in range (len(tasks_list)):
            if tasks_list[k].lower() == change_task.lower():
                update_task = input("enter the task to update the list : ")
                tasks_list[k] = update_task
                print(f"{update_task} is updated successfully in the list.\n")

    elif selected_option == "view list":
        print(tasks_list)

    elif selected_option == "exit" or "stop":
        print("You choosed to exit the To Do Application.\n")
        break










