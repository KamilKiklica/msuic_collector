import os
import sys


def show_albums():
    print("")
    with open('lista.txt', 'r') as outfile:
        for i, line in enumerate(outfile):
            lineSplitted = line.split(",")
            print("{} . Artist: {} | Album: {} | Year: {} | Genre: {} | Lenght: {}".format(
                i + 1, lineSplitted[0], lineSplitted[1], lineSplitted[2], lineSplitted[3], lineSplitted[4]))






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
                if int(HScoreTempList[j][4]) > int(HScoreTempList[j+1][4]):
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


sort_lenght()

show_temp()