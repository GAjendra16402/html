a = ["mohit", "rohitnghumar", "jhummar"]

while True:
    print("1. Check name in list")
    print("2. Insert new name")
    print("3. Delete existing name")
    print("4. Print full list")
    print("0. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 0:
        print("Exiting...")
        break
    elif choice == 1:
        name = input("Enter name to check: ")
        if name in a:
            print([f"{name} is in the list."])
        else:
            print([f"{name} is not in the list."])
    elif choice == 2:
        name = input("Enter new name to insert: ")
        a.append(name)
        print([f"{name} has been inserted into the list."])
    elif choice == 3:
        name = input("Enter existing name to delete: ")
        if name in a:
            a.remove(name)
            print([f"{name} has been deleted from the list."])
        else:
            print([f"{name} is not in the list."])
    elif choice == 4:
        print(["Full list:", a])
    else:
        print(["Invalid choice. Please enter a valid option."])