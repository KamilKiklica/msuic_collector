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
        for i, line in enumerate(outfile):
            lineSplitted = line.split(" | ")
            print("{} . {} | {} | {} | {} | {}".format(
                i + 1, lineSplitted[0], lineSplitted[1], lineSplitted[2], lineSplitted[3], lineSplitted[4]))

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

def search_by_name():
    album_temp_list = sort_lenght()
    search = input("Enter what atrist are you looking for: ")
    if any(search in s for s in album_temp_list):
        print(album_temp_list[i][0], album_temp_list[i][1])


                
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
        pass
    if user_input == "4":
        search_by_name()
    if user_input == "5":
        pass
    if user_input == "6":
        sort_lenght()
    if user_input == "7":
        show_all()


if __name__ == "__main__":
    main()

