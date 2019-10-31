    # list_of_length_of_all_albums = return_list_of_length_of_albums(list_of_lists)
    # print(list_of_length_of_all_albums)
    # sum_of_list_of_length_of_all_albums = sum(list_of_length_of_all_albums)
    # print(sum_of_list_of_length_of_all_albums)
    # sum_of_list_of_length_of_all_albums_in_minutes = sum_of_list_of_length_of_all_albums / 60  # divided / 60
    # print(sum_of_list_of_length_of_all_albums_in_minutes)

    # length = sum_of_list_of_length_of_all_albums_in_minutes

    # minutes = int((length * 60) % 60)
    # seconds = int((length * 3600) % 60)
    # # print("%d:%02d.%02d" % (minutes, seconds))
    # print("%02d:%02d" % (minutes, seconds))    
    # # print('{}:{}'.format(minutes, seconds))
    # length2 = ("%02d:%02d" % (minutes, seconds))
    # print(length2)

    # print(time.strftime("%M:%S", time.gmtime(length)))
    # print(str(datetime.timedelta(seconds=length)))
    # print('---------')
    # length_of_all_albums = (time.strftime("%H:%M:%S", time.gmtime(sum_of_list_of_length_of_all_albums)))
    # print(length_of_all_albums)
    # str_sum_of_list_of_length_of_all_albums_in_minutes = str(sum_of_list_of_length_of_all_albums_in_minutes)
    # print(str_sum_of_list_of_length_of_all_albums_in_minutes)
    # (m, s) = str_sum_of_list_of_length_of_all_albums_in_minutes.split(',')
    # print(m)
    # print(s)
    # sum_of_all_albums = int(m) + 



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


