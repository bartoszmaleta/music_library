import csv


def main():
    data = import_files()
    print(data)
    list_of_lists = data
    print()
    print_records(list_of_lists)


def import_files(filename='text_albums_data.txt'):
    results = []
    with open(filename, newline='') as inputfile:
        for row in csv.reader(inputfile):
            results.append(row)
    return results


def print_records(list_of_lists):
    for elem in list_of_lists:
        print(elem)


# testowanie 1234
# testowanie 12366786867234234sasadasd

main()