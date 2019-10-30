import csv
# from display import *


def main():
    data = import_files()
    print(data)
    list_of_lists = data
    print()
    print_records(list_of_lists)
    print()
    print_albums_by_genre(list_of_lists)
    print()
    print_albums_by_given_time_range(list_of_lists)
    print()
    print_albums_by_artist(list_of_lists)
    print()
    print_albums_by_album_name(list_of_lists)
    print_albums_by_year(list_of_lists)


def import_files(filename='/home/acer/Documents/music_library/music_library/text_albums_data.txt'):
    results = []
    with open(filename, newline='') as inputfile:
        for row in csv.reader(inputfile):
            results.append(row)
    return results


def print_records(list_of_lists):
    for elem in list_of_lists:
        print(elem)


def print_albums_by_genre(list_of_lists):
    genre = input('By what genre you want see albums? ')
    genre = genre.lower()
    for elem in list_of_lists:
        if genre == elem[-2]:
            print(elem)


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


# testing git
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


def print_albums_by_year(list_of_lists):
    years =[]
    max_or_min = input('Oldest or Newest o/n ? ')
    # album_name = album_name.lower()
    for elem in list_of_lists:
        years.append(int(elem[2]))
        
    if max_or_min == 'n':
        print(max(years)) 
    else: 
        print(min(years))

    def locate_min(some_list):
        min_indicies = []
        smallest = min(some_list)
        for index, element in enumerate(some_list):
            if smallest == element:  # check if this element is the minimum_value
                min_indicies.append(index)  # add the index to the list if it is

        # return smallest, min_indicies
        # print(smallest)
        # print(min_indicies)
        first_oldest_album = list_of_lists[min_indicies[0]]
        second_oldest_album = list_of_lists[min_indicies[1]]
        print('-----')
        print('first: ', first_oldest_album)
        print('second: ', second_oldest_album)

    # print(list_of_lists[4])
    # print(list_of_lists[9])
    
    print(years)
    locate_min(years)


main()