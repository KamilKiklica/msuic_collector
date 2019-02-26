import os
import sys

def time_to_seconds(x):  # funkcjazmieniająca czas w formacie "minuty:sekundy" na "sekundy"
    a = str(x)
    a = a.split(':')
    b = (int(a[0])*60)+int(a[1])
    return b

def switchPlaces(tab, i, j):
    temp = tab[j]
    tab[j] = tab[i]
    tab[i] = temp
    return tab

def make_list_of_list():   #make list of lists from file lista.txt
    results = []
    with open('lista.txt') as outfile:
        for line in outfile:
            results.append(line.strip().split(','))
    return results


def sort_lenght():
    print("")
    album_temp_list = []
    with open('lista.txt', 'r') as outfile:
        for i, line in enumerate(outfile):
            lineSplitted = line.split(",")
            album_temp_list.append(lineSplitted)

        for i in range(0, len(album_temp_list)):
            for j in range(0, len(album_temp_list)-1):
                a = (album_temp_list[j][4])
                b = (album_temp_list[j+1][4])
                aa = time_to_seconds(a)
                bb = time_to_seconds(b)
                if aa > bb:
                    album_temp_list = switchPlaces(album_temp_list, j, j+1)

    with open('lista.txt', 'r') as outfile:
        f = open("temp.txt", "w+")
        for i, line in enumerate(album_temp_list):
            lineToWrite = "{} | {} | {} | {} | {}".format(
               album_temp_list[i][0], album_temp_list[i][1], album_temp_list[i][2], album_temp_list[i][3], album_temp_list[i][4])
            f.write(lineToWrite)

    return(album_temp_list)

def show_temp(): #debug
    print("")
    with open('temp.txt', 'r') as outfile:
        artist_len = 1 + dynamic_spaces_column(0,0)
        album_len = 1 + dynamic_spaces_column(1,1)
        date_len = 1 + dynamic_spaces_column(2,2)
        genre_len = 1 + dynamic_spaces_column(3,3)
        album_lenght_len = 1 + dynamic_spaces_column(4,4)
        #nr_len = lenght_of_signs_in_name_of_column(5,5)
        print("|" + "Nr.".ljust(4, ' ') + "|" + "Artist:".ljust(artist_len, ' ') + "|" + "Name of Album:".ljust(album_len, ' ') + "|" + "Date:".ljust(date_len, ' ')+ "|" + "Genre:".ljust(genre_len, ' ') + "|" + "Lenght of Album:".ljust(album_lenght_len, ' '))
        print('-'.ljust(artist_len + album_len + date_len + genre_len + album_lenght_len + 5, '-'))
        for i, line in enumerate(outfile):
            lineSplitted = line.split(" | ")
            print("|{}|{}|{}|{}|{}|{}".format(
                (str(i + 1) + ".").ljust(4, ' '), lineSplitted[0].ljust(artist_len, ' '), lineSplitted[1].ljust(album_len, ' '), lineSplitted[2].ljust(date_len, ' '), lineSplitted[3].ljust(genre_len, ' '), lineSplitted[4].ljust(album_lenght_len, ' ')))
        print('-'.ljust(artist_len + album_len + date_len + genre_len + album_lenght_len + 5, '-'))



def lenght_of_signs(iterating_number_of_column):   # checking lenght of signs for the longest value in each column
    k = make_list_of_list()
    len_k = len(k)  #lenght of main list
    len_m = len(k[0])  #lenght of elements in list of list
    list_column = []
    for i in range(len_k):
        list_column.append(k[i][iterating_number_of_column])
        list_column.sort(key=len, reverse=True)  #sort list k by lenght of keys (longest to smallest)
    lenght = len(list_column[0])
    return lenght

  
def lenght_of_signs_in_name_of_column(parameter):
    a = ["Artist:","Name of Album:","Date:", "Genre:","Lenght of Album:"]
    if parameter == 0:
        a = len(a[0])
    elif parameter == 1:
        a = len(a[1])
    elif parameter == 2:
        a = len(a[2])
    elif parameter == 3:
        a = len(a[3])
    elif parameter == 4:
        a = len(a[4])
    #elif parameter == 5:
    #    a = len(a[5])
    return a

def dynamic_spaces_column(a,b):
    if lenght_of_signs_in_name_of_column(a) <= lenght_of_signs(b):
        a = lenght_of_signs(b)
    else:
        a = lenght_of_signs_in_name_of_column(a)
    return a


def show_all():
    print("")
    with open('lista.txt', 'r') as outfile:
        for i, line in enumerate(outfile):
            lineSplitted = line.split(",")
            print("{} . {} | {} | {} | {} | {}".format(
                i + 1, lineSplitted[0], lineSplitted[1], lineSplitted[2], lineSplitted[3], lineSplitted[4]))

def show_albums():
    print("")
    with open('lista.txt', 'r') as outfile:
        print("Albums:")
        for i, line in enumerate(outfile):
            lineSplitted = line.split(",")
            print("{}. {} ".format(
                i + 1,  lineSplitted[1]))


def show_time_range():          
    album_temp_list = sort_lenght()
    print("What time range of albums release would you like to see?")
    start_date = input("Enter start date: ")
    end_date = input("Enter end date: ")
    for i in range(len(album_temp_list)):
        if start_date <= album_temp_list[i][2] <= end_date:
            print(album_temp_list[i][0], album_temp_list[i][1])

def search_by_genre(): #szukanie po gatunku, sformatować drukowanie
    album_temp_list = sort_lenght()
    genre = input("Type genre that you looking for: ")
    for line in album_temp_list:
        if genre in line[3]:
            print(line)
    #else:
        #print("You don't have this kind of genre in collection.")

def search_by_album():
    album_temp_list = sort_lenght()
    search_album = input("Type the name of album: ").title() #problem dla rock, bo małe litery
    for line in album_temp_list:
        if search_album in line[1]:
            print(line)
    #else:      Cały czas się drukuje, narazie nie włączam
        #print("You don't have a such album.")

def search_by_artist():
    album_temp_list = sort_lenght()
    search_artist = input("Type the name of artist: ").title() #problem dla rock, bo małe litery
    for line in album_temp_list:
        if album_temp_list.index().title() == search_artist:
            print(line)

                
def main():  # powinno printować menu z wyborem sortowania
    print("1. Show albums" + "\n"
          "2. Find by year" + "\n"
          "3. Find album by name" + "\n"
          "4. Find by genre" + "\n"
          "5. Find by artist" + "\n"
          "6. Show shortest/longest" + "\n"
          "7. Show whole informations" + "\n"
          )
    user_input = input("Which option would you like to chose? <1-8>: ")
    if user_input == "1":
        show_albums()
    if user_input == "2":
        show_time_range()
    if user_input == "3":
        search_by_album()
    if user_input == "4":
        search_by_genre()
    if user_input == "5":
        search_by_artist()
    if user_input == "6":
        pass
    if user_input == "7":
        show_temp()


if __name__ == "__main__":
    main()
