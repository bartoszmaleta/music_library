import csv
import pickle
from display import *


def main():
    menu()
   

def menu():
    is_running = True
    while is_running:
        display_menu()
        user_choice = input("Your choise is: ")
        if (user_choice == "1"):
            print_records(list_of_lists)
        elif (user_choice == "2"):
            print_albums_by_genre()
        elif (user_choice == "3"):
            print_albums_by_given_time_range()
        elif (user_choice == "4"):
            printing_shortest_or_longest_album()
        elif (user_choice == "5"):
            print_albums_by_given_artist()
        elif (user_choice == "6"):
            print_albums_by_given_album_name()
        elif (user_choice == "7"):  # TODO raport!!!!
            # printning_raport()
            return_raport()
        elif (user_choice == "8"):
            add_new_album()
        elif (user_choice == "10"):
            print_youngest_or_oldest_album()
        elif (user_choice == "Q"):
            is_running = False


def import_files(filename="text_albums_data.txt"): 
    results = []
    with open(filename, newline='') as inputfile:
        for row in csv.reader(inputfile):
            results.append(row)
    return results


# filename = "text_albums_data.txt"
data = import_files()
import_files()
print(data)
list_of_lists = data


def return_albums_by_genre(list_of_lists):
    genre = input('By what genre you want see albums? ')
    genre = genre.lower()
    
    list_of_albums_sorted_by_genre = []
    
    for elem in list_of_lists:
        if genre == elem[-2]:
            # print(elem)
            list_of_albums_sorted_by_genre.append(elem)
    
    # print_records(list_of_albums_sorted_by_genre)

    return list_of_albums_sorted_by_genre


def print_albums_by_genre():
    albums_by_genre = return_albums_by_genre(list_of_lists)
    print()
    print('Albums with your genre are: \n {}'.format(albums_by_genre))
    print()
    # print_records(list_of_albums_sorted_by_genre)


def return_albums_by_given_time_range(list_of_lists):
    minimal_time_in_minutes = (input('Minimum time of album: (in minutes) '))
    maximum_time_in_minutes = (input('Maximum time of album: (in minutes) '))
    print(minimal_time_in_minutes)
    print(maximum_time_in_minutes)
    minimal_time_in_seconds = int(minimal_time_in_minutes) * 60
    print(minimal_time_in_seconds)
    maximum_time_in_seconds = int(maximum_time_in_minutes) * 60
    print(maximum_time_in_seconds)  

    list_of_albums_sorted_by_given_time_range = []

    for elem in list_of_lists:
        length_of_album = elem[-1]
        (m, s) = length_of_album.split(':')  
        length_of_album_in_seconds = int(m) * 60 + int(s)
        if length_of_album_in_seconds in range(minimal_time_in_seconds, maximum_time_in_seconds):
            print(elem)
            list_of_albums_sorted_by_given_time_range.append(elem)

    # print_records(list_of_albums_sorted_by_given_time_range)

    return list_of_albums_sorted_by_given_time_range


def print_albums_by_given_time_range():
    albums_by_given_time_range = return_albums_by_given_time_range(list_of_lists)
    print()
    print('Albums with your given range are: \n {}'.format(albums_by_given_time_range))
    print()


def return_albums_by_artist(list_of_lists):
    artist = input('By what artist you want see albums? ')
    list_of_albums_sorted_by_artist = []
    # artist = artist.lower()
    for elem in list_of_lists:
        if artist == elem[0]:
            # print(elem)
            list_of_albums_sorted_by_artist.append(elem)
    
    # print_records(list_of_albums_sorted_by_artist)

    return list_of_albums_sorted_by_artist


def print_albums_by_given_artist():
    albums_by_given_artist = return_albums_by_artist(list_of_lists)
    print()
    print('Albums with your given artist are: \n {}'.format(albums_by_given_artist))
    print()


def return_albums_by_given_album_name(list_of_lists):
    album_name = input('By what name you want see albums? ')
    list_of_albums_sorted_by_album_name = []
    # album_name = album_name.lower()
    for elem in list_of_lists:
        if album_name == elem[1]:
            # print(elem)
            list_of_albums_sorted_by_album_name.append(elem)

    # print_records(list_of_albums_sorted_by_album_name)

    return list_of_albums_sorted_by_album_name    


def print_albums_by_given_album_name():
    albums_by_given_album_name = return_albums_by_given_album_name(list_of_lists)
    print()
    print('Albums with your given album name are: \n {}'.format(albums_by_given_album_name))
    print()


# -------------------------------

def return_list_of_years(list_of_lists):
    list_of_years = []
    for elem in list_of_lists:
        list_of_years.append(int(elem[2]))
    return list_of_years


def return_list_of_oldest_album():
    min_years = []
    list_of_oldest_album = []

    list_of_years = return_list_of_years(list_of_lists)
    smallest = min(list_of_years)
    
    for index, element in enumerate(list_of_years): 
        if smallest == element:  # check if this element is the minimum_value
            min_years.append(index)  # add the index to the list if it is
    # print(min_years)

    for elem in min_years:
        # print(list_of_lists[elem])
        list_of_oldest_album.append(list_of_lists[elem])

    return list_of_oldest_album


def return_list_of_youngest_album():
    max_years = []
    list_of_youngest_album = []

    list_of_years = return_list_of_years(list_of_lists)
    biggest_year = max(list_of_years)
    
    for index, element in enumerate(list_of_years): 
        if biggest_year == element:  # check if this element is the minimum_value
            max_years.append(index)  # add the index to the list if it is
    # print(min_years)

    for elem in max_years:
        # print(list_of_lists[elem])
        list_of_youngest_album.append(list_of_lists[elem])

    return list_of_youngest_album


def print_youngest_or_oldest_album():
    # list_of_lists = data
    print_youngest_album = return_list_of_youngest_album()

    print_oldest_album = return_list_of_oldest_album()

    max_or_min = input('Oldest or Youngest? (o/y) ')
    if max_or_min == 'o':
        print(print_oldest_album)
    elif max_or_min == 'y':
        print(print_youngest_album)


# ------------------

def return_list_of_length_of_albums(list_of_lists):
    list_of_length_of_albums = []

    for elem in list_of_lists:
        length_of_album = elem[-1]
        (m, s) = length_of_album.split(':')  
        length_of_album_in_seconds = int(m) * 60 + int(s)
        list_of_length_of_albums.append(length_of_album_in_seconds)

    return list_of_length_of_albums

    # minimum_length = min(list_of_length_of_albums)

    # index_of_minimum_length_in_list_of_lists = list_of_length_of_albums.index(minimum_length)
    # album_with_shortest_length = list_of_lists[index_of_minimum_length_in_list_of_lists]

    # maximum_length = max(list_of_length_of_albums)

    # index_of_maximum_length_in_list_of_lists = list_of_length_of_albums.index(maximum_length)
    # album_with_longest_length = list_of_lists[index_of_maximum_length_in_list_of_lists]

    # list_with_shortest_and_longest = []
    # list_with_shortest_and_longest.append(album_with_longest_length)
    # list_with_shortest_and_longest.append(album_with_shortest_length)

    # return list_with_shortest_and_longest


def return_list_of_longest_albums():
    returned_list_of_length_of_albums = return_list_of_length_of_albums(list_of_lists)
    maximum_length = max(returned_list_of_length_of_albums)

    index_of_maximum_length_in_list_of_lists = returned_list_of_length_of_albums.index(maximum_length)
    list_of_albums_with_longest_length = list_of_lists[index_of_maximum_length_in_list_of_lists]

    return list_of_albums_with_longest_length


def return_list_of_shortest_albums():
    returned_list_of_length_of_albums = return_list_of_length_of_albums(list_of_lists)
    minimum_length = min(returned_list_of_length_of_albums)

    index_of_minimum_length_in_list_of_lists = returned_list_of_length_of_albums.index(minimum_length)
    list_of_albums_with_shortest_length = list_of_lists[index_of_minimum_length_in_list_of_lists]

    return list_of_albums_with_shortest_length


def printing_shortest_or_longest_album():
    # print_list_with_shortest_and_longest = returning_shortest_or_longest_album(list_of_lists)
    # print('List with shortest and longest: ', print_list_with_shortest_and_longest)
    # # print(list_with_shortest_and_longest)
    
    print_list_of_shortest_albums = return_list_of_shortest_albums()
    print_list_of_longest_albums = return_list_of_longest_albums()

    shortest_or_longest = input('Shortest or Longest? (s/l) ')
    if shortest_or_longest == 's':
        print(print_list_of_shortest_albums)
    elif shortest_or_longest == 'l':
        print(print_list_of_longest_albums)

# ----------------------------


def return_raport():
    print_youngest_album = return_list_of_youngest_album()
    print_oldest_album = return_list_of_oldest_album()
    print_list_of_shortest_albums = return_list_of_shortest_albums()
    print_list_of_longest_albums = return_list_of_longest_albums()

    print('ya ---> ', print_youngest_album, '\n', 'old ----> ', print_oldest_album)
    print('shortest ---> ', print_list_of_shortest_albums)
    print('longest ---> ', print_list_of_longest_albums)

def add_new_album():
    new_album = []
    input_class_list = ['Artist', 'Title', 'year', 'genre', 'lenght']
    for elem in input_class_list:
        element = input(f"Input : {elem} : ")
        new_album.append(element)
    print(new_album)
    string = ",".join(new_album)
    print(string)
    with open('text_albums_data.txt', 'a+') as fo:
        fo.writelines("%s" % string)
        
    return new_album




main()