user_choice = ''

def print_records(list_of_lists):
    for elem in list_of_lists:
        print(elem)
    return print_records


def display_menu():
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


# def menu():
#     is_running = True
#     while is_running:
#         display_menu()
#         user_choice = input("Your choise is: ")
#         if (user_choice == "1"):
#             print_records(list_of_lists)
#         elif (user_choice == "Q"):
#             is_running = False
    





# is_running = True
# user_choice = None
# display_menu()
