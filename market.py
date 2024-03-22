
# issue 5 release + bugfix (add item) (dy)
# issue 6 : hotfix (narak : add 1 item to menu)

item_dic = {"Coffee" : 7, "Pen" : 3, "Paper cup": 2, "Milk" : 1, "Coke" : 4, "Book" : 5, "Beer": 10}

while True:
    # Issue1 :a add print menu    print("\nMenu:") (commit 2 times)
    # Ta
    print("\nMenu:") 
    print("1. Inventory inquiry")
    print("2. Incoming stock")
    print("3. Outgoing stock")
    print("4. Quit")

    user_input = input("Enter your choice (1-4): ")
    # Seiha
    

    if user_input == "1":
        pro_name = input("Enter the name of the product: ")
        if pro_name in item_dic:
            print(f"Inventory of {pro_name} : {item_dic[pro_name]}")
        else:
            print(f"{pro_name} not found in inventory.")
    elif user_input == "2":
        pro_name, qty = input("Enter name and quantity of the product : ").split()
        qty = int(qty) # convert qty
        if pro_name in item_dic: 
            item_dic[pro_name] += qty # increase user_input product.
            print(qty, 'of', pro_name, '(s) added to the inventory.')
        else:
            print(f"{pro_name} not found in inventory.")
    elif user_input == "3" :
        pro_name, qty = input("Enter name and quantity of the product : ").split()
        qty = int(qty) # convert qty
        if pro_name in item_dic: 
            item_dic[pro_name] -= qty # increase user_input product.
            print(qty, 'of', pro_name, '(s) substracted from the inventory.')
        else:
            print(f"{pro_name} not found in inventory.")
    # issue3 : Create option to quit (commit 1 time)
    elif user_input == "4":
        print("Quitting the program. Goodbye!")
        break
   
    # issue4 : Create else (commit 3 times)
    # Raksa
    else:
        print('Invalid Choice. Please enter a number between 1 and 4.')