import os
import sys


def show_albums():
    print("")
    with open('lista.txt', 'r') as outfile:
        print("Albums:")
        for i, line in enumerate(outfile):
            lineSplitted = line.split(",")
            print("{}. {} ".format(
                i + 1,  lineSplitted[1]))

# funkcjazmieniająca czas w formacie "minuty:sekundy" na "sekundy"
def time_to_seconds(x):
    a = str(x)
    a = a.split(':')
    b = (int(a[0])*60)+int(a[1])
    return b

def switchPlaces(tab, i, j):
    temp = tab[j]
    tab[j] = tab[i]
    tab[i] = temp
    return tab


def sort_lenght():
    print("")
    HScoreTempList = []
    with open('lista.txt', 'r') as outfile:
        for i, line in enumerate(outfile):
            lineSplitted = line.split(",")
            HScoreTempList.append(lineSplitted)

        for i in range(0, len(HScoreTempList)):
            for j in range(0, len(HScoreTempList)-1):
                a = (HScoreTempList[j][4])
                b = (HScoreTempList[j+1][4])
                aa = time_to_seconds(a)
                bb = time_to_seconds(b)
                if aa > bb:
                    HScoreTempList = switchPlaces(HScoreTempList, j, j+1)

    with open('lista.txt', 'r') as outfile:
        f = open("temp.txt", "w+")
        for i, line in enumerate(HScoreTempList):
            lineToWrite = "{} | {} | {} | {} | {}".format(
                HScoreTempList[i][0], HScoreTempList[i][1], HScoreTempList[i][2], HScoreTempList[i][3], HScoreTempList[i][4])
            f.write(lineToWrite)
        
    return(HScoreTempList)

def show_temp():
    print("")
    with open('temp.txt', 'r') as outfile:
        album_len = 1 + dynamic_spaces_column(0,0)
        artist_len = 1 + dynamic_spaces_column(1,1)
        date_len = 1 + dynamic_spaces_column(2,2)
        genre_len = 1 + dynamic_spaces_column(3,3)
        album_lenght_len = 1 + dynamic_spaces_column(4,4)
        #nr_len = lenght_of_signs_in_name_of_column(5,5)
        print("|" + "Nr.".ljust(5, ' ') + "|" + "Name of Album:".ljust(album_len, ' ') + "|" + "Artist:".ljust(artist_len, ' ') + "|" + "Date:".ljust(date_len, ' ')+ "|" + "Genre:".ljust(genre_len, ' ') + "|" + "Lenght of Album:".ljust(album_lenght_len, ' '))
        print('-'.ljust(album_len + artist_len + date_len + genre_len + album_lenght_len + 5, '-'))
        for i, line in enumerate(outfile):
            lineSplitted = line.split(" | ")
            print("|{}|{}|{}|{}|{}|{}".format(
                (str(i + 1) + ".").ljust(5, ' '), lineSplitted[0].ljust(album_len, ' '), lineSplitted[1].ljust(artist_len, ' '), lineSplitted[2].ljust(date_len, ' '), lineSplitted[3].ljust(genre_len, ' '), lineSplitted[4].ljust(album_lenght_len, ' ')))
        print('-'.ljust(album_len + artist_len + date_len + genre_len + album_lenght_len + 5, '-'))


def make_list_of_list():   #make list of lists from file lista.txt
    results = []
    with open('lista.txt') as outfile:
        for line in outfile:
            results.append(line.strip().split(','))
    return results


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
    a = ["Name of Album:","Artist:","Date:", "Genre:","Lenght of Album:"]
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



show_albums()
sort_lenght()
show_temp()
