import time
user_choice = ''


def print_records(list_of_lists):
    text_for_printing_the_whole_list_of_lists = 'THE LIST OF ALBUMS \n'
    text_for_printing_the_whole_list_of_lists_alignment = text_for_printing_the_whole_list_of_lists.center(50)
    print(text_for_printing_the_whole_list_of_lists_alignment)
    for elem in list_of_lists:
        print(elem)
    return print_records


def display_menu():
    print('=========================================================')
    print('=========================================================')
    menu_text = '\033[1;35;49m MENU!'
    menu_text_alignment = menu_text.center(63)
    print(menu_text_alignment)
    print('\033[0;37;49m ')
    print('=========================================================')
    print("1. Show list")
    print("2. Find all albums by genre.")
    print("3. Find all albums from given time range.")
    print("4. Find shortest/longest album")
    print("5. Find all albums created by given artist")
    print("6. Find album by album name")
    print("7. Print report")
    print("8. Add new album")
    print("9. Edit album")
    print("10. Find oldest or youngest album")
    print("Q. Quit")


def welcoming_screen():
    print()
    print('                        ##########################################')  # spaces = 20
    user_name_question = ('                        ########### What is your name? ###########')
    print(user_name_question)
    print('                        ##########################################')
    print()
    print('_______________')
    print('|')
    user_name_answer = input('| ')
    print('|______________')
    clear_terminal()
    print()
    hello_text = ('Hello {}'.format(user_name_answer))
    hello_text_alignment = hello_text.ljust(60)
    print(hello_text_alignment)
    print()
    print()
    welcome_text = '\033[1;33;49m Welcome in the MUSIC COLLECTOR!'
    welcome_text_alignment = welcome_text.center(100)
    copyrights_text = '\033[1;32;49m Michał Z., Bartosz M.'
    copyrights_alignment = copyrights_text.center(100)
    print(welcome_text_alignment)
    print(copyrights_alignment)
    print('\033[0;37;49m \n')
    time.sleep(1)         # change to 5
    clear_terminal()


def clear_terminal():
    print('\033[H\033[J')


def your_choice():
    print("Enter your choice: ")


def one_line_space():
    print()