import os
import sys

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
    with open("lista.txt", "r") as outfile:
        answer = input("")


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
        for i, line in enumerate(outfile):
            lineSplitted = line.split(" | ")
            print("{} . {} | {} | {} | {} | {}".format(
                i + 1, lineSplitted[0], lineSplitted[1], lineSplitted[2], lineSplitted[3], lineSplitted[4]))


def main():  # powinno printować menu z wyborem sortowania
    print("1. Show albums"
          "2. Sort by lenght"
          "3. Find album by name"
          "4. Find by genre"
          "5. Find by artist"
          "6. Show shortest/longest"
          "7. Show whole informations"
          )
    user_input = input("Which option would you like to chose? <1-8>: ")
    if user_input == "1":
        show_albums()
    if user_input == "2":
        pass
    if user_input == "3":
        pass
    if user_input == "4":
        pass
    if user_input == "5":
        pass
    if user_input == "6":
        pass
    if user_input == "7":
        show_all()


if __name__ == "__main__":
    main()

