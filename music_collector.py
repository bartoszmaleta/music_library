import csv
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
            print_albums_by_genre(list_of_lists)
        elif (user_choice == "3"):
            print_albums_by_given_time_range(list_of_lists)
        elif (user_choice == "4"):
            printing_shortest_or_longest_album()
        elif (user_choice == "5"):
            print_albums_by_artist(list_of_lists)
        elif (user_choice == "6"):
            print_albums_by_album_name(list_of_lists)
        # elif (user_choice == "7"):  # TODO raport!!!!
        #     printning_raport()
        elif (user_choice == "Q"):
            is_running = False


def import_files(filename="/home/acer/Documents/music_library/music_library/text_albums_data.txt"): 
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


def print_albums_by_genre(list_of_lists):
    genre = input('By what genre you want see albums? ')
    genre = genre.lower()
    
    selected_albums = []
    
    for elem in list_of_lists:
        if genre == elem[-2]:
            # print(elem)
            selected_albums.append(elem)
    
    print_records(selected_albums)


def print_albums_by_given_time_range(list_of_lists):
    minimal_time_in_minutes = (input('Minimum time of album: (in minutes) '))
    maximum_time_in_minutes = (input('Maximum time of album: (in minutes) '))
    print(minimal_time_in_minutes)
    print(maximum_time_in_minutes)
    minimal_time_in_seconds = int(minimal_time_in_minutes) * 60
    print(minimal_time_in_seconds)
    maximum_time_in_seconds = int(maximum_time_in_minutes) * 60
    print(maximum_time_in_seconds)  
    for elem in list_of_lists:
        length_of_album = elem[-1]
        (m, s) = length_of_album.split(':')  
        length_of_album_in_seconds = int(m) * 60 + int(s)
        if length_of_album_in_seconds in range(minimal_time_in_seconds, maximum_time_in_seconds):
            print(elem)


def print_albums_by_artist(list_of_lists):
    artist = input('By what artist you want see albums? ')
    # artist = artist.lower()
    for elem in list_of_lists:
        if artist == elem[0]:
            print(elem)


def print_albums_by_album_name(list_of_lists):
    album_name = input('By what name you want see albums? ')
    # album_name = album_name.lower()
    for elem in list_of_lists:
        if album_name == elem[1]:
            print(elem)


# def print_albums_by_year(list_of_lists):
#     years = []
#     max_or_min = input('Oldest or Newest o/n ? ')
#     # album_name = album_name.lower()
#     for elem in list_of_lists:
#         years.append(int(elem[2]))

#     return years    


def locate_youngest_or_oldest_album():
    list_of_lists = data
    # print_albums_by_year(list_of_lists)
    list_of_years = []
    min_years = []
    max_years = []
    max_or_min = input('Oldest or Newest o/n ? ')
    for elem in list_of_lists:
        list_of_years.append(int(elem[2]))
    
    # print(list_of_years)
        
    if max_or_min == 'o':
        smallest = min(list_of_years)
        # smallest = min(list_of_lists[2])
        for index, element in enumerate(list_of_years): 
            if smallest == element:  # check if this element is the minimum_value
                min_years.append(index)  # add the index to the list if it is
        # print(min_years)

        for elem in min_years:
            print(list_of_lists[elem])

    if max_or_min == 'n':
        biggest_year = max(list_of_years)

        for index, element in enumerate(list_of_years):
            if biggest_year == element:
                max_years.append(index)
        # print(max_years)     

        for elem in max_years:
            print(list_of_lists[elem]) 


def returning_shortest_or_longest_album(list_of_lists):
    list_of_length_of_albums = []

    for elem in list_of_lists:
        length_of_album = elem[-1]
        (m, s) = length_of_album.split(':')  
        length_of_album_in_seconds = int(m) * 60 + int(s)
        list_of_length_of_albums.append(length_of_album_in_seconds)
    # if length_of_album_in_seconds in range(minimal_time_in_seconds, maximum_time_in_seconds):
        # print(elem)
    # print(list_of_length_of_albums)

    # RIGHT NOW IT IS DOING: converting_to_seconds_all_length_of_albums_and_adding_to_new_list

    # finding minimum value
    minimum_length = min(list_of_length_of_albums)
    # print(minimum_length)

    index_of_minimum_length_in_list_of_lists = list_of_length_of_albums.index(minimum_length)
    # print(index_of_minimum_length_in_list_of_lists)
    album_with_shortest_length = list_of_lists[index_of_minimum_length_in_list_of_lists]
    # print(album_with_shortest_length)

    # TODO: maximum lenght:
    maximum_length = max(list_of_length_of_albums)
    # print(maximum_length)

    index_of_maximum_length_in_list_of_lists = list_of_length_of_albums.index(maximum_length)
    # print(index_of_maximum_length_in_list_of_lists)
    album_with_longest_length = list_of_lists[index_of_maximum_length_in_list_of_lists]
    # print(album_with_longest_length)

    list_with_shortest_and_longest = []
    list_with_shortest_and_longest.append(album_with_longest_length)
    list_with_shortest_and_longest.append(album_with_shortest_length)
    return list_with_shortest_and_longest


def printing_shortest_or_longest_album():
    print_list_with_shortest_and_longest = returning_shortest_or_longest_album(list_of_lists)
    print('List with shortest and longest: ', print_list_with_shortest_and_longest)
    # print(list_with_shortest_and_longest)


def printing_raport():
    pass


main()