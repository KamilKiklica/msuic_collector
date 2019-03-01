import os
import sys
import display

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

def make_list_of_list(filename):   #make list of lists from file lista.txt
    results = []
    with open(filename) as outfile:
        for line in outfile:
            results.append(line.strip().split(','))
    return results

def make_list_of_temp():   #make list of lists from file lista.txt
    a = []
    with open('temp.txt') as outfile:
        for line in outfile:
            results.append(line.strip().split(','))
    return a


def list_from_main_file(filename = "lista.txt"):
    print("")
    album_temp_list = []
    with open(filename, 'r') as outfile:
        for i, line in enumerate(outfile):
            lineSplitted = line.split(",")
            album_temp_list.append(lineSplitted)
    return album_temp_list

def sort_lenght():
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
            lineToWrite = "{},{},{},{},{}".format(
               album_temp_list[i][0], album_temp_list[i][1], album_temp_list[i][2], album_temp_list[i][3], album_temp_list[i][4])
            f.write(lineToWrite)
    return(album_temp_list)

def sort_by_years():
    album_temp_list = []
    with open('lista.txt', 'r') as outfile:
        for i, line in enumerate(outfile):
            lineSplitted = line.split(",")
            album_temp_list.append(lineSplitted)

        for i in range(0, len(album_temp_list)):
            for j in range(0, len(album_temp_list)-1):
                a = int(album_temp_list[j][2])
                b = int(album_temp_list[j+1][2]) 
                if a > b:
                    album_temp_list = switchPlaces(album_temp_list, j, j+1)
    with open('lista.txt', 'r') as outfile:
        f = open("temp.txt", "w+")
        for i, line in enumerate(album_temp_list):
            lineToWrite = "{},{},{},{},{}".format(
            album_temp_list[i][0], album_temp_list[i][1], album_temp_list[i][2], album_temp_list[i][3], album_temp_list[i][4])
            f.write(lineToWrite)
    return(album_temp_list)

def oldest_albums():
    album_temp_list = sort_by_years()
    years_range = album_temp_list[0][2]
    open('temp.txt', 'w').close()
    for line in album_temp_list:
       #if start_date <= album_temp_list[2] <= end_date:
#        if int(line[2]) in years_range:
        if line[2] in years_range:
            b = ','.join(line)
            f = open('temp.txt', 'a')
            f.write(b)
            f.close()
    display.show_all('temp.txt',False,False)


def youngest_albums():      
    album_temp_list = sort_by_years()
    years_range = album_temp_list[-1][2]
    open('temp.txt', 'w').close()
    for line in album_temp_list:
        #if start_date <= album_temp_list[2] <= end_date:
#        if int(line[2]) in years_range:
        if line[2] in years_range:
            b = ','.join(line)
            f = open('temp.txt', 'a')
            f.write(b)
            f.close()
    display.show_all('temp.txt',False,False)



def show_time_range():          
    album_temp_list = sort_by_years()
    print("What time range of albums release would you like to see?")
    start_date = input("Enter start date: ")
    while not (str.isdigit(start_date)):
        start_date = input("Enter correct start date: ")
    end_date = input("Enter end date: ")
    while not (str.isdigit(end_date)):
        end_date = input("Enter correct end date: ")
    while int(end_date) < int(start_date):
        end_date = input("End date can't be smaller then start date. Please enter correct end date: ")
    years_range = list(range(int(start_date), int(end_date)+1))
    open('temp.txt', 'w').close()
    for line in album_temp_list:
        #if start_date <= album_temp_list[2] <= end_date:
        if int(line[2]) in years_range:
            b = ','.join(line)
            f = open('temp.txt', 'a')
            f.write(b)
            f.close()
    display.show_all('temp.txt')
        


def search_by_genre(): #szukanie po gatunku, drukowanie działa
    album_temp_list = list_from_main_file()
    genre = input("Type genre that you looking for: ").casefold()
    open('temp.txt', 'w').close()
    for line in album_temp_list:
        if genre in line[3].casefold():
            b = ','.join(line)
            f = open('temp.txt', 'a')
            f.write(b)
            f.close()
    display.show_all('temp.txt')


def search_by_album():
    album_temp_list = list_from_main_file()
    search_album = input("Type the name of album: ").casefold()
    open('temp.txt', 'w').close()
    for line in album_temp_list:
        if search_album in line[1].casefold():
            b = ','.join(line)
            f = open('temp.txt', 'a')
            f.write(b)
            f.close()
            temp_list_txt = []
            temp_list_txt = list_from_main_file("lista.txt")
            genre_main = line[3]
            os.system('clear')
            print("          Founded albums in list for searched phrase: ")
            print('')
            display.show_all('temp.txt', False,False)
#            open('temp.txt', 'w').close()
            for line in temp_list_txt:
                if genre_main in line[3].casefold():
                    b = ','.join(line)
                    f = open('temp_line_separation.txt', 'a')
                    f.write(b)
                    f.close()
###############EXPERIMENTAL#####################
#            if len(list_from_main_file("temp.txt")) == 1:
 #               pass            
            if len(list_from_main_file("temp.txt")) >= 1:
                if not genre_main in line[3].casefold():
                    b = '▄▄▄▄▄▄▄▄▄▄,▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄,▄▄▄▄▄,▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄,▄▄▄▄▄\n'
                    f = open('temp_line_separation.txt', 'a')
                    f.write(b)
                    f.close()

##############END EXPERIMENTAL################## mozna w miejsce odstepu skasowac 1 linie w temp_line_separation.txt
            print(" ")        
            print("          Suggested albums by genre for searched phrase: ")
            print(" ")        
            display.show_all('temp_line_separation.txt', False, False)
    open('temp_line_separation.txt', 'w').close()

def search_by_artist():
    album_temp_list = list_from_main_file()
    search_artist = input("Type the name of artist: ").casefold()
    open('temp.txt', 'w').close()
    for line in album_temp_list:
        if search_artist in line[0].casefold():
            b = ','.join(line)
            f = open('temp.txt', 'a')
            f.write(b)
            f.close()
    display.show_all('temp.txt')

def search_shortest_longest():
    album_temp_list = sort_lenght()
    open('temp.txt', 'w').close()
    b = ','.join(album_temp_list[0])
    c = ','.join(album_temp_list[-1])
    f = open("temp.txt", "a")
    f.write(b)
    f.write(c)
    f.close()
    display.show_all('temp.txt', False,True)
    return album_temp_list

def search_longest():
    album_temp_list = sort_lenght()
    open('temp.txt', 'w').close()
    b = ','.join(album_temp_list[0])
    f = open("temp.txt", "a")
    f.write(b)
    f.close()
    display.show_all('temp.txt', False, False)
    return album_temp_list

def search_shortest():
    album_temp_list = sort_lenght()
    open('temp.txt', 'w').close()
    c = ','.join(album_temp_list[-1])
    f = open("temp.txt", "a")
    f.write(c)
    f.close()
    display.show_all('temp.txt', False, False)
    return album_temp_list

def albums_count():
    num_lines = sum(1 for line in open('lista.txt'))
    return num_lines
    
                
def main():  # powinno printować menu z wyborem sortowania
    os.system('clear')
    display.display_logo()
    user_not_turn_off = True
    while user_not_turn_off:
        display.display_menu()
        user_input = input("Which option would you like to chose? <1-9>: ")
        
        if user_input == "1":
            display.show_all("lista.txt")
        if user_input == "2":
            show_time_range()
        if user_input == "3":
            search_by_album()
        if user_input == "4":
            search_by_genre()
        if user_input == "5":
            search_by_artist()
        if user_input == "6":
            search_shortest_longest()
        if user_input == "7":
            display.show_all("lista.txt", True)
        if user_input == "8":
            edit_albums()
        if user_input == "9":
            user_not_turn_off = False
            #user_not_turn_off = False


def edit_albums():
    display.show_all('lista.txt')

    display.display_edit_menu()
    user_input = input("Which option would you like to chose? <1-4>: ")
    if user_input == "1":
        os.system('clear')
        display.show_all('lista.txt')
        artist = input('Name of Artist: ')
        album = input('Name of Album: ')
        date = input('Year: ')
        genre = input('Genre: ')
        album_lenght = input('Lenght of album in format "minutes:seconds": ')
        new_album = (artist + ',' + album + ',' + date + ',' + genre + ',' + album_lenght + '\n')
        with open('lista.txt','a') as f:
            f.write(new_album)
        os.system('clear')
        print('You have added new album succesfully!''\n')        
    if user_input == "2":
        nr = input('Choose number of album to edit: ')
        while not int(nr) in range(12):
            nr = input('Choose correct number of album to edit: ')
        nr = int(nr)-1
        artist = input('Name of Artist: ')
        album = input('Name of Album: ')
        date = input('Year: ')
        genre = input('Genre: ')
        album_lenght = input('Lenght of album in format "minutes:seconds": ')
        new_album = (artist + ',' + album + ',' + date + ',' + genre + ',' + album_lenght + '\n')
        replace_line('lista.txt',nr,new_album)
        os.system('clear')
        display.show_all('lista.txt')
        print('You have edited new album succesfully!''\n')  
    if user_input == "3":
        os.system('clear')
        display.show_all('lista.txt')
    if user_input == "4":
        os.system('clear')
        display.show_all('lista.txt')


def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()


def additional_info():
    album_temp_list = list_from_main_file()
    genre_list = []
    for i in range(len(album_temp_list)):
        genre_list.append(album_temp_list[i][3])

    additional = {x:genre_list.count(x) for x in genre_list}
    return (additional)

def print_table(inventory, order=None):
  k = list(inventory.keys())    #make list named k  from keys in dict.
  v = list(inventory.values())  #make list named v from values in dict
  k.sort(key=len,reverse=True)  #sort list k by lenght of keys (longest to smallest)
  v.sort(reverse=True)          #sort list v (values) from the biggest to the smallest
  key_len = len(k[0])           
  value_len = len(str(v[0]))
  if value_len <= 5:            #checks if lenght of biggest element in value is smaller than "name of column"
    count_len = 5               #if yes the width of values column is constans = 5 (len of count column)
  else:  
    count_len = value_len + 4   #set dynamic amount of spaces for len biggest value element > len column name
  if key_len <= 9:              #checks if lenght of biggest element in key column is smaller than "name of column"
    item_name_len = 5          #if yes the width of key column is constans = 13 (len of name column)
  else:
    item_name_len = key_len #set dynamic amount of spaces for len bigest key element > len column name
  #UNTIL HERE EVERYTHING IS GOOD

  print('genre'.ljust(item_name_len, ' ') + 'count'.rjust(count_len, ' '))
  print('-'.rjust(count_len + item_name_len, '-'))
  if order == None:
    for keys, values in inventory.items():
      print(str(values).rjust(count_len, ' ') + str(keys.rjust(item_name_len, ' ')))
      a = sum(inventory.values())
  elif order == "count,asc":
    for k,v in sorted(inventory.items(), key=lambda p:p[1]):
      print(str(k.ljust(item_name_len, ' ')) + str(v).rjust(count_len, ' '))
  elif order == "count,desc":
    for k,v in sorted(inventory.items(), key=lambda p:p[1], reverse=True):
      print(str(v).rjust(count_len, ' ') + str(k.rjust(item_name_len, ' ')))
  print('-'.rjust(count_len + item_name_len, '-'))
  a = sum(inventory.values())   #Counting whole amount of items
  



if __name__ == "__main__":
    main()







### ZASTANOWIC SIE NAD WYSWIETLANIEM RAPORTU
### idiotoodpornosc
### podział na dwa pliki
### zmniejszenie funkcji (podział na mniejsze???)
### exoprt do pliku listy albumów


#how many albums are given the genres)

