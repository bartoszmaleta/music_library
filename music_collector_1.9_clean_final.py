import csv
from display import *
import time

# INFO: MICHAŁ!!!!!! Don't change path!!! Just comment my path, and uncomment yours, which is below
# PATH to change are in: 
# 1) 
# 2) -----ADDING ALBUMS
# CHANGE time.sleep in display to 5

# TODO:
# 1) Last point of report ===> DONE partially ==>  how many albums are given the genres         DONE
# 2) As a user I want to view all similar music genres albums when searching            
#    for particular album (Like in spotify, where user receives context suggestions 
#    regarding similar bands or tracks)
# 3) As a user I want to add new album ===> DONE partially ==> does not update print_tabel 
#                                                              during running program           DONE
# 4) As a user I want to edit already existing albums   ====> IN PROGRESS!!!!
# 5) As a user I want to save all new albums to external file
#
# TODO: Features not in exercises:
# 6) Pretty tables!!!!!


def main():
    welcoming_screen()
    menu()


def menu():
    is_running = True
    while is_running:
        display_menu()
        your_choice()
        user_choice = input()
        if (user_choice == "1"): 
            clear_terminal()
            list_of_lists = import_files()
            print_records(list_of_lists)
        elif (user_choice == "2"):
            clear_terminal()
            print_albums_by_genre()
        elif (user_choice == "3"):
            clear_terminal()
            print_albums_by_given_time_range()
        elif (user_choice == "4"):
            clear_terminal()
            printing_shortest_or_longest_album()
        elif (user_choice == "5"):
            clear_terminal()
            print_albums_by_given_artist()
        elif (user_choice == "6"):
            clear_terminal()
            print_albums_by_given_album_name()
        elif (user_choice == "7"): 
            clear_terminal()
            print_report()
        elif (user_choice == "8"):  
            clear_terminal()
            add_new_album()
        elif (user_choice == "9"):
            clear_terminal()
            edit_album()
        elif (user_choice == "10"):
            clear_terminal()
            print_youngest_or_oldest_album()
        elif (user_choice == "11"):  #  TESTING LIST_OF_ALL_GENRES
            clear_terminal()
            print_list_of_genres()
        elif (user_choice == "12"):
            clear_terminal()
            return_number_of_albums()
        elif (user_choice == "e"):
            clear_terminal()
            easter_egg()
            time.sleep(7)
        elif (user_choice == "Q"):
            is_running = False


# def import_files(filename="text_albums_data.txt"): 
def import_files(filename="/home/acer/Documents/music_library/music_library/text_albums_data.txt"): 
    results = []
    with open(filename, newline='') as inputfile:
        for row in csv.reader(inputfile):
            results.append(row)
    inputfile.close()
    return results


# filename = "text_albums_data.txt"
data = import_files()
import_files()
list_of_lists = data


# ---------------------------------------------- GENRE 

def return_albums_by_genre(list_of_lists):
    genre = input('By what genre you want see albums? ')
    genre = genre.lower()
    list_of_albums_sorted_by_genre = []
    
    for elem in list_of_lists:
        if genre == elem[-2]:
            list_of_albums_sorted_by_genre.append(elem)

    return list_of_albums_sorted_by_genre


def print_albums_by_genre():
    albums_by_genre = return_albums_by_genre(list_of_lists)
    one_line_space()
    print('Albums with your genre are: ')
    print('--------------------------------------')    
    for elem in albums_by_genre:
        print(elem)
    print('--------------------------------------')    
    print()
    print()


# ---------------------------------------------- TIME RANGE

def return_albums_by_given_time_range(list_of_lists):
    minimal_time_in_minutes = (input('Minimum time of album: (in minutes) '))
    maximum_time_in_minutes = (input('Maximum time of album: (in minutes) '))
    minimal_time_in_seconds = int(minimal_time_in_minutes) * 60
    maximum_time_in_seconds = int(maximum_time_in_minutes) * 60

    list_of_albums_sorted_by_given_time_range = []

    for elem in list_of_lists:
        length_of_album = elem[-1]
        (m, s) = length_of_album.split(':')  
        length_of_album_in_seconds = int(m) * 60 + int(s)
        if length_of_album_in_seconds in range(minimal_time_in_seconds, maximum_time_in_seconds):
            list_of_albums_sorted_by_given_time_range.append(elem)

    return list_of_albums_sorted_by_given_time_range


def print_albums_by_given_time_range():
    albums_by_given_time_range = return_albums_by_given_time_range(list_of_lists)
    one_line_space()
    info_about_what_is_displaying = 'Albums with your given range are: '
    print(info_about_what_is_displaying)
    print('--------------------------------------')    
    for elem in albums_by_given_time_range:
        print(elem)
    print('--------------------------------------')    


# ---------------------------------------------- ALBUMS BY ARTIST

def return_albums_by_artist(list_of_lists):
    artist = input('By what artist you want see albums? ')
    list_of_albums_sorted_by_artist = []
    # artist = artist.lower()      # NOT CASE SENSITIVE
    # print(artist)       # NOT CASE SENSITIVE
    for elem in list_of_lists:
        # elem_str = elem[0]
        # elem_str_lower = elem_str.lower()
        # print(elem_str_lower)
        # if artist == elem_str_lower:
        #     print(elem_str_lower)      # NOT CASE SENSITIVE
        #     # elem.lower()      # NOT CASE SENSITIVE
        #     list_of_albums_sorted_by_artist.append(elem_str_lower)
        if artist == elem[0]:
            print(elem[0])      # NOT CASE SENSITIVE
            # elem.lower()      # NOT CASE SENSITIVE
            list_of_albums_sorted_by_artist.append(elem)
    
    return list_of_albums_sorted_by_artist


def print_albums_by_given_artist():
    albums_by_given_artist = return_albums_by_artist(list_of_lists)
    one_line_space()
    info_about_what_is_displaying = 'Albums with your given artist name are: '
    print(info_about_what_is_displaying)
    print('--------------------------------------')    
    for elem in albums_by_given_artist:
        print(elem)
    print('--------------------------------------')    


# ---------------------------------------------- BY GIVEN NAME

def return_albums_by_given_album_name(list_of_lists):
    album_name = input('By what album name you want see albums? ')
    list_of_albums_sorted_by_album_name = []
    # album_name = album_name.lower()
    for elem in list_of_lists:
        if album_name == elem[1]:
            # print(elem)
            list_of_albums_sorted_by_album_name.append(elem)

    return list_of_albums_sorted_by_album_name    


def print_albums_by_given_album_name():
    albums_by_given_album_name = return_albums_by_given_album_name(list_of_lists)
    one_line_space()
    info_about_what_is_displaying = 'Albums with your given album name are: '
    print(info_about_what_is_displaying)
    print('--------------------------------------')    
    for elem in albums_by_given_album_name:
        print(elem)
    print('--------------------------------------')  


# ---------------------------------------------- OLDEST

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

    for elem in min_years:
        # print(list_of_lists[elem])
        list_of_oldest_album.append(list_of_lists[elem])

    return list_of_oldest_album


# ---------------------------------------------- YOUNGEST 

def return_list_of_youngest_album():
    max_years = []
    list_of_youngest_album = []

    list_of_years = return_list_of_years(list_of_lists)
    biggest_year = max(list_of_years)
    
    for index, element in enumerate(list_of_years): 
        if biggest_year == element:  # check if this element is the minimum_value
            max_years.append(index)  # add the index to the list if it is

    for elem in max_years:
        # print(list_of_lists[elem])
        list_of_youngest_album.append(list_of_lists[elem])

    return list_of_youngest_album


def print_youngest_or_oldest_album():
    print_youngest_album = return_list_of_youngest_album()
    print_oldest_album = return_list_of_oldest_album()

    max_or_min = input('Oldest or Youngest? (o/y) ')
    if max_or_min == 'o':
        one_line_space()
        info_about_what_is_displaying = 'Oldest albums are: '
        print(info_about_what_is_displaying)
        for elem in print_oldest_album:
            print(elem)
    elif max_or_min == 'y':
        one_line_space()
        info_about_what_is_displaying = 'Newest albums are: '
        print(info_about_what_is_displaying)
        for elem in print_youngest_album:
            print(elem)


# ---------------------------------------------- LONGEST / SHORTEST

def return_list_of_length_of_albums(list_of_lists):
    list_of_length_of_albums = []

    for elem in list_of_lists:
        length_of_album = elem[-1]
        (m, s) = length_of_album.split(':')  
        length_of_album_in_seconds = int(m) * 60 + int(s)
        list_of_length_of_albums.append(length_of_album_in_seconds)
    return list_of_length_of_albums


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
    print_list_of_shortest_albums = return_list_of_shortest_albums()
    print_list_of_longest_albums = return_list_of_longest_albums()

    shortest_or_longest = input('Shortest or Longest? (s/l) ')
    if shortest_or_longest == 's':
        one_line_space()
        info_about_what_is_displaying = 'Albums with shortest length are: '
        print(info_about_what_is_displaying)
        print(print_list_of_shortest_albums)

    elif shortest_or_longest == 'l':
        one_line_space()
        info_about_what_is_displaying = 'Albums with longest length are: '
        print(info_about_what_is_displaying)

        # for elem in print_list_of_longest_albums:
            # print(elem)
        print(print_list_of_longest_albums)


# ---------------------------------------------- REPORT

def print_report():
    print_youngest_album = return_list_of_youngest_album()
    print_oldest_album = return_list_of_oldest_album()
    print_list_of_shortest_albums = return_list_of_shortest_albums()
    print_list_of_longest_albums = return_list_of_longest_albums()
    print_dictionary_of_genres = dictionary_of_genres()
    print_number_of_albums = return_number_of_albums()

    report_text = '\033[1;34;49m REPORT'
    report_text = report_text.center(60)
    print(report_text)
    print('\033[0;37;49m ')

    print('Newest album: \n')
    for elem in print_youngest_album:
        print('', elem)

    print('---------------------')
    print('Oldest album: \n') 
    for elem in print_oldest_album:
        print('', elem)
    print('---------------------')
    print('Shortest album: \n\n', print_list_of_shortest_albums)

    print('---------------------')
    print('Longest album: \n\n', print_list_of_longest_albums)

    print('---------------------')
    print('Number of albums: \n\n', print_number_of_albums)

    print('---------------------')
    list_of_length_of_all_albums = return_list_of_length_of_albums(list_of_lists)
    sum_of_list_of_length_of_all_albums = sum(list_of_length_of_all_albums)
    length_of_all_albums = (time.strftime("%H:%M:%S", time.gmtime(sum_of_list_of_length_of_all_albums)))

    print('Length of all albums: \n\n', length_of_all_albums)

    print('---------------------')
    print('Genres statistics: \n')
    for k, v in print_dictionary_of_genres.items():
        print('', k, ':', v)


# ---------------------------------------------- ADDING NEW ALBUM

def add_new_album():
    new_album = []
    adding_new_album_text = '\033[1;34;49m ADDING NEW ALBUM'
    adding_new_album_text_alignment = adding_new_album_text.center(60)
    print(adding_new_album_text_alignment)
    print('\033[0;37;49m ')
    input_class_list = ['artist', 'title', 'year', 'genre', 'lenght (mm:ss)']
    for elem in input_class_list:
        element = input(f"Input {elem} : ")
        new_album.append(element)
    one_line_space()
    new_album_text = 'Your new album is: '
    print(new_album_text)
    one_line_space()
    print(new_album)
    one_line_space()
    
    string = ",".join(new_album)
    with open('/home/acer/Documents/music_library/music_library/text_albums_data.txt', 'a+') as fo:
    # with open('text_albums_data.txt', 'a+') as fo:
        print('It has been added to albums list')
        fo.writelines("%s" % "\n" + string)
        fo.close()
        
    return new_album


# ---------------------------------------------- List of all genres

def return_list_of_genres(list_of_lists):
    list_of_genres = []
    GENRE_INDEX = -2
    for elem in list_of_lists:
        # print(elem)
        list_of_genres.append(elem[GENRE_INDEX])
    
    return list_of_genres


def dictionary_of_genres():
    dict_of_genres = {} 
    all_genres_list = return_list_of_genres(list_of_lists)
    for elem in all_genres_list:
        if elem in dict_of_genres:
            dict_of_genres[elem] += 1
        else:
            dict_of_genres[elem] = 1

    return dict_of_genres


# ---------------------------------------------- HELPING FUNCIONS TO TESTS

def print_list_of_genres():     # HELPING FUNCIONS = TESTING
    all_genres_list = return_list_of_genres(list_of_lists)
    one_line_space()
    info_about_what_is_displaying = 'Dict of genres: '
    print(info_about_what_is_displaying)

    print('---------------------')

    dictionary_of_genres
    print(all_genres_list)


# ---------------------------------------------- NUMBER OF ALBUMS

def return_number_of_albums():
    list_of_length_of_albums = return_list_of_length_of_albums(list_of_lists)

    number_of_albums = len(list_of_length_of_albums)
    return number_of_albums


# ---------------------------------------------- EDITING ALBUM

def edit_album():
    edited_album = []
    editing_album_text = '\033[1;34;49m EDITING ALBUM'
    editing_album_text_alignment = editing_album_text.center(60)
    print(editing_album_text_alignment)
    print('\033[0;37;49m ')
    input_number_of_album = input('Which album you want to edit? (Input number) ====> ')
    input_number_of_album_int = int(input_number_of_album)
    
    print(list_of_lists[input_number_of_album_int])


def easter_egg():
    print(""" 
    %%%%%%%%%%%%%%%%%%%%%#%%%%%%%%#####((########%#%%%###*..................            ...,,*/(#(/(##%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%#(,.,**//**##%###((##/*,.........,.,....  .... ...   .... .  ..,,*,/%/%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#(#%#%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%#(,./(,.**,(#*,*/**,..........,*,.,................... .... ....,*,*,(#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#(##(#%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%(,.*/*/(*,*#/,.,........,.*,,,....,......... ...................,*,,**%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#((###(((#%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%#/../%%##*.*(/*......,.,,,,,,,.,,,,.,,,,,.....,,....................,*,/%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#(/*****//(##%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#//(#%#(*,,*,,..,.,,..,,,,**,,,,,,,,,,,,,,...,,,,,,.,........ ......*,,(%%%%%%%%%%%%%%%%%%%%%%%%%%%%%######(#####%%%%%%%%%%%%%%%%%
%%%%#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%##(*,......,.,,,,,**,,,,....................,............. ...,..*(%%%%%%%%%%%%%%%%%%%%%%%%%%(**//((//#%%%%%%%%%%%%%%%%%%%%%
###%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#*,,,,....,,.,***,,,..........................,,............  ....*,*/(%%%%%%%%%%%%%%%%%%%%%%(,,//,,**/#(****/#%%%%%%%%%%%%%
###%%%%%%%%%%%%%%%%%%%%%%%#%%%%%##*,,,,,,,,.,..,*,,,,,...........,......,........................ .......,/%%%%%%%%%%%%%%%%%%%%%(,,/*,*/**#/,*/(#%%%%%%%%%%%%%%
##%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#(,,,*,*.*,,,,.,**,,,..............,..,,,,............,.................,...*#%%%%%%%%%%%%%%%%%%%(,,(###/,,##(*,,,(%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%##%%%#%/**,,,..**,*,,*,,,,,,,,,..............,,....................,.............. .*(#%%%%%%%%%%%%%%%%%#//(%%#/,,/**//**(%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#***,,.,*/,,,,,,,,,,,,,,..,,.,,,,,.,.....,................,...,.,..............,#%%%%%%%%%%%%%%%%%%%%%%%%%%#%###(##%%%%%%%%%%%%%%
##%%%#%%%%###%%#%%%%###%%%%%##/*,,,,,,*,.....,,,,,,,,,,,.,,,,,,,,,,,..,,..........,...,..,.....................(%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
##%%%%#%%%%#/(#((#%%%##%%%%%#/*,,,*,,,,...,.,,,*,,,,,,,,,,,,,,,,,,,,,,,,......,...,.,...,,.,.......,.......,..../%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%##%%####%#(###((#####%%%###,,*,,,,,...,,,,,,,,,,,,,,,,,,.,,,,,,,,,,,,,,.......,...,.,............,,.......,....%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%###%%#####(((###//(#%##%%##/,*,,,,,....,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.,,...,..,,,,.,,..,.............,....,#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%#%%#(**,,*****/((#%##%%%%##/*,.,.....,..,,*,,***,,,,,,,,,,,,,,,,.,,,,,,,,,,,,,,,,,,,.,,,,.,,,,,,,,..........,...(%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
###########((######%#%%#####*,,,,,,,..,..,,,,,,,,,*,,***,,,,,,,,,,,,,,,,,,*,,,,,,,,,,,,,,,,,,,,,,,,,,,,....,,,,..*#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
##(**/(((/*/#%######%##%###(,,*,,*,,,,,,,,*,*,,,,,,,,***,,,,*******/(*//*/**/*,,,,,*,,,*,,*******/*/*****,..,,,..*(###%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%(,.**,.**,*##*****(######(,,,,,,*,,,*,,,*,*,,,,,**,**,***/****/(#%##((/(/(///*****,*****////////(((/****,,,,,...(#####%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
##(,.**,,//,*#*,,/(########(**,,*****,*,,,,,*,**,,,*******/////****,,*****//((((//**,,,/(((((///*******,***,,,,,..(##((#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
##(../####*.,#(/*,.,*#####%#/,******,,,,,,,,**,,,,,,,******/*******,,,*******/((/**,,,,*/((//******,,*,*****,,,,..*/(#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
##/,,/####,.,(,,(#(,,####%%%/,///****,********,,**,,,,****/*****/%%%&&&&%#%%((/(/**,,.,*////(%##%%%%###/****,,,,,,*###%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%###########(((//(#%%%%%%%#,/((*************,,,,*,,,,***/*/(%&&%%%&&&%(#%#(//(/**,,,,,*/*(#%#%&@@&&&&%%/,**,.,,,*%#((#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%##################%%%%%/..,,/#(/***/*********,**,,*****((##(/*****,,,*/(////((**,,,,,,,*////********(%%/**,..,****//*(#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
###%##%########%%#%#%%%%%*//******//////*********/////*,,*///***//*//////******/*,,,,,,,,,,***//////*****//****,,,,,,,,/#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
####%%%#####%####%%%%%%%#*%%%%(((/*//((///*******,*,,**.,,,.....,,,,,,,,,,,,,,,,,,,,,,,,,.,,,,,,,,,,,,,*,....,,,,,*#,/*,,(%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
####%%%%#%##%%%##%%%%%%%(*(((//(#(((//(/////*****,,,,,,,.,.....,.,,,,,,,,,,,,,,,,,,,,,,,,,..,,,,,,,,........,...,/((,***/#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
(((##%%%%#%##%%%%%%%%%%%(,//*,,*////(///////****,,*,,,,,,,,,,...,..,,,,,,,,,,,,,,*,,,,,,,,,..,,,,,,,,...........,/(**###%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%####%%#%%%%%%%%%%%%%%#*//,,,,,*////*//*********,,,,,,,,,,,.,..,,..,,,,,,,*****,,,,,,...,..,,,,,,.,...........,/(*/%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%##%%#%%%%%%%%%%%%%#%##**,,,***(%&((****/*************,,,,,,,,,,,,.,,,,**//**//(((//****,,,*,,***,,..........,,,(,(%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%#%%%%%%%%%%%%%%%%#%%#%(*,*/////#%#,*********//*/*******,,,,,,,,,,,,,*///((((#&@@&@#(((///(%(/*//**,,,,,,...,,,,,,#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%###%%%%%%%%%%%%%%%%#%%%##,*,**///##(***********************,,,,,,****/((**//((((##%%%##%####///***(/**,,,,,,,,,,,,,#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%#%%%%#%%%#%#%//*,,*/(((((*************/***************/((/*********//////##(///*******/((/****,,,,,,,*,%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%#%%%%%%%%%%%**/*,,,,*(#/**************************//((//**********,*,**********,,,****(((/*******,,,*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%#%%%%%%%#%%#*,/(*,,****/******************//**///(#(((//*********************,,,,,**//(#(/******,.,#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%###%%%%%%%%%%%%%%%%%%##*,*,,,,*,,//*/***************///////(///////*//**********,,**********,**//#(//*****,../%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%###%%#%%%%%#%%%#%%%%%#%##/*,,,,,*(//////*************//**/**(/((#((((((((#/((////**////****/**/(//(/*******,...%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%#%%%#%%%%%%%%%%%%%%#%###(//*//(##////////////******//****,/(/#&@@@@@@@&&@@&&&&&%%&@&&&&&%%%%%#(//******,,,*,,%%%%%%%%%%%%%%%%%%%#((##%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%#%%#///((##%%#(#//////////////*****(/****,**///(%&&&%&&&&&&&&%%%%%%&%%&%%((////********,,#(%%%%%%%%%%%%%%%%%%%%########%%%%%%%%%%%%%%%%
%%%#%%%%%%%%%%%%%%%%#%%%#%##,.*(*.**,*/((//////////////****///***,********/(((((///*/****//((//*****///**********%%%%%%%%%%%%%%%%%%%%%#(((###((#%%%%%%%%%%%%%%%
%%%%%%#%%%%%%%%%%%%%%%%#%%##,.*/,,*/,*/((//(////////////****///******************************,****,*///*****,***#%%%%%%%%%%%%%%%%#(/*****//(##%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%##%#,./####*.,#/(((//((///((((///****///************///////*/*/*/*******,,,***/*****,***%%%%%%%%%%%%%%%%%%#######%##%%%%%%%%%%%%%%%%%%%
%%%%%%%%%#%%%%%%%%%%%%%%%%#(,,*#%%#*.,(*(((((((((//((((((/****/(/******,******************,,,,,,,,,,***********(%%%%%%%%%%%%%%%#/*///(/*#%%%###%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%####(((((((((((((((#(((/****/(/******,,,,,,,,,,,,,,,,,,,,,,,,,,,,***********%%%%%%%%%%%%%%%%(,.//,,*,*#(**/*/#%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#(/(##((((((((((#(((/***/((*******,,,,,,,,,,,,,,,,,,,,,,,,,,,*********/%%%%%%%%%%%%%%%%%(,,//,*(,*#(,,*(#%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#//##(###(((((((#(((//***(////******,,,,,,,,,,,,.,,,,,,,,,,,******///%%%%%%%%%%%%%%%%%%(,,(##%/,,(#(/*,,/%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#//(###############((///*/(((///**********,,,,,,,******,*,***/**////%%%%%%%%%%%%%%%%%%%(**(%%#/,,/*,*/**(%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@,.//(###(#(########(#((/////(((((//////*//**/**/////////**///*///((%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%####%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@,..,/((##((((###(####(##((((/(#(####(((##(#((((((((((((((//*///(//%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@&,,,..,((((((((((((#(((#(((((###(((#%%%%%%%%%%%%%%%%%##///**//(//(%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@,.....,,/(/(((/(((#(####((((######((((((((((((////////*///////**%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@/.......,,,((((//(((((##(((((((###%##(((((((((///////////////*,#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@*.........,,*/(///((####################((((/(((/////////**,* @&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%#%%%%%%%%%%%%%%%%%%%%&@@@@@@@@@@*...........,,*/////(#################%%########(((((//**,,  @@&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%#/((##%%%%%%%%%%%%%%&@@@@@@@@@@&@&*.............,,*//////##%#####%%&&%&&&&&&&%%%%%##/***,*.   @@@&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%#####((/(%%%%%&&@@@@@@@@@@@@@@@@@@&,....       ....,,*/*****/((##%%%%%%%%%%%%%%%##(/***,.     @@@@&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%#/**(##((#&@@@@@@@@@@@@@@@@@@@@@@@@@@@*.....          ...,********(((((((#((((/((((((/..        @@@@@@&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%#/**,****/&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,......             .,********/******/***//*,            %@@@@@@&%(###%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%#%&&&&@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,.......                 ./,,,**/**/(***(,             ..#%@@@@&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*,......                    (/**//%%%%#*.             ...%%@@@@&&&&&&&@@@@&@&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
&&&&@&&&@@@@@@@@@@@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@#,.....                  .*&@@@@@@@@@@&&&&&(        . ..,%%&&&&&%&%%&&@@@@@@@@&@&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%
&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&.....              .&&&&&&&&&&&@@@@@&&&&&&&%(     .  ,&&&&&&&&&&&&%%&&@@@@@@@@&@&&&&&&&%%%%%%%%%%%%%%%%%%%%%
    """)

    # for albums in list_of_lists[input_number_of_album_int]:
    #     if input_number_of_album_int == list_of_lists[index - 1]

    # input_class_list = ['artist', 'title', 'year', 'genre', 'lenght (mm:ss)']
    
    # for elem in input_class_list:
    #     element = input(f"Input {elem} : ")
    #     new_album.append(element)
    
    # one_line_space()
    # new_album_text = 'Your new album is: '
    # print(new_album_text)
    # one_line_space()
    # print(new_album)
    # one_line_space()
    
    # string = ",".join(edited_album)
    # with open('/home/acer/Documents/music_library/music_library/text_albums_data.txt', 'a+') as fo:
    # # with open('text_albums_data.txt', 'a+') as fo:
    #     print('It has been added to albums list')
    #     fo.writelines("%s" % "\n" + string)
    #     fo.close()
        
    # return new_album


main()