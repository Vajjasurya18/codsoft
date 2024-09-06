contact_list = {}

while True:
    print("Choose the below options to update the contact list : ")
    print("1.Add contact")
    print("2.Delete contact")
    print("3.Edit contact")
    print("4.search contact")
    print("5.view contacts")
    print("6.Exit")

    choice = input("Enter your choice : ").lower()

    if choice == "add":
        name = input("Enter the name to add for contact list : ")
        contact = input("Enter the moblie no: ")
        email = input("Enter the email: ")
        address = input("Enter the address: ")
        contact_list[name] = {'Contact': contact,'Email':email, 'Address': address}
        for contact,details in contact_list.items():
            print(f"{contact} : {details}")
        print('\n')

    elif choice == "delete":
        pop_contact = input("enter the contact name for delete the contact : ")
        del contact_list[pop_contact]
        print("Contact is deleted successfully."'\n')

    elif choice == "edit":
        name_to_edit = input("Enter the name to edit in the contact list : ")
        for i in contact_list:
            if i == name_to_edit:
                contact_list[name_to_edit]['Contact']= input("Enter the moblie no: ")
                contact_list[name_to_edit]['Email'] = input("Enter the email: ")
                contact_list[name_to_edit]['Address'] = input("Enter the address: ")
        print("Contact is updated successfully."'\n')

    elif choice == "search":
        search_name = input("Enter the name to search in contact list : ")
        status = {}
        for person in contact_list:
            if search_name == person:
                status = contact_list[person]
        if status != {}:
            print(f"Name : {search_name}")
            for keys,value in status.items():
                print(f"{keys} : {value}")
            print('\n')
        else:
            print("Name invalid '\n'")

    elif choice == "view":
        for contact,details in contact_list.items():
            print(f"{contact} : {details}")
        print('\n')

    elif choice == "exit":
        print("You choose to Exit")
        break

    else:
        print("Please enter invalid input....")


