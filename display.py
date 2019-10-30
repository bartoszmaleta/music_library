is_running = True
user_choice = None

def menu():
    user_choice = input("Your choise is: ")
    print("1. Show list")
    print("2. Find all albums by genre.")
    print("3. Find all albums from given time range.")
    print("4. Find shortest/longest album")
    print("5. Find all albums created by given artist")
    print("6. Find album by album name")
    print("7. Print report")
    print("8. Add new album")
    print("9. Edit album")
    print("Q. Quit")
while is_running:
    menu()
    if (user_choice == "1"):
        print_records(list_of_lists)
    elif 