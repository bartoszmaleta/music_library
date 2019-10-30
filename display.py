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
    print("10. Find oldest or youngest album (o/y)")
    print("Q. Quit")

