import os
import music_reports







def show_all(filename, user_report=False, clear=True): #debug
    if clear == True:
        os.system('clear')
    elif clear == False:
        pass
    with open(filename, 'r') as outfile:
        artist_len = 1 + dynamic_spaces_column(0,0,filename)
        album_len = 1 + dynamic_spaces_column(1,1,filename)
        date_len = 1 + dynamic_spaces_column(2,2,filename)
        genre_len = 1 + dynamic_spaces_column(3,3,filename)
        album_lenght_len = 1 + dynamic_spaces_column(4,4,filename)
        a = (''.ljust(artist_len + album_len + date_len + genre_len + album_lenght_len + 9, '─'))
        if user_report == False:
            print('┌' + a + '┐')
            print("│" + "Nr.".ljust(4, ' ') + "│" + "Artist:".ljust(artist_len, ' ') + "│" + "Name of Album:".ljust(album_len, ' ') + "│" + "Date:".ljust(date_len, ' ')+ "│" + "Genre:".ljust(genre_len, ' ') + "│" + "Lenght of Album:".ljust(album_lenght_len, ' ') + '│')
            print('├' + a + '┤')
            for i, line in enumerate(outfile):
                lineSplitted = line.strip('\n').split(",")
                print("│{}│{}│{}│{}│{}│{}│".format(
                    (str(i + 1) + ".").ljust(4, ' '), lineSplitted[0].ljust(artist_len, ' '), lineSplitted[1].ljust(album_len, ' '), lineSplitted[2].ljust(date_len, ' '), lineSplitted[3].ljust(genre_len, ' '), lineSplitted[4].ljust(album_lenght_len, ' ')))
            print('└' + a + '┘')
        if user_report == True:
#            print(a)
            print(' LONGEST ALBUM '.center(artist_len + album_len + date_len + genre_len + album_lenght_len + 9, '░'))
#            print(a)
            music_reports.search_shortest()
            print(' SHORTEST ALBUM '.center(artist_len + album_len + date_len + genre_len + album_lenght_len + 9, '░'))
#            print(a)
            music_reports.search_longest()
            print(' OLDEST ALBUM '.center(artist_len + album_len + date_len + genre_len + album_lenght_len + 9, '░'))
#            print(a)
            music_reports.oldest_albums()
            print(' YOUNGEST ALBUM '.center(artist_len + album_len + date_len + genre_len + album_lenght_len + 9, '░'))
#            print(a)
            music_reports.youngest_albums()
            #sort_by_years(True,True)
            print(' ALL ALBUM COUNT '.center(artist_len + album_len + date_len + genre_len + album_lenght_len + 9, '░'))
            num_lines = music_reports.albums_count()
            print("             You have {} albums in your collection.".format(num_lines))
            music_reports.print_table(music_reports.additional_info(),"count,asc")
            print(a)
#            print(a)
#            print(a)


def lenght_of_signs(iterating_number_of_column, filename):   # checking lenght of signs for the longest value in each column
    k = music_reports.make_list_of_list(filename)
    len_k = len(k)  #lenght of main list
    #len_m = len(k[0])  #lenght of elements in list of list
    list_column = []
    for i in range(len_k):
        list_column.append(k[i][iterating_number_of_column])
        list_column.sort(key=len, reverse=True)  #sort list k by lenght of keys (longest to smallest)
    if os.stat(filename).st_size == 0:
        lenght = 1
    else:
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

def dynamic_spaces_column(a,b,filename):
    if lenght_of_signs_in_name_of_column(a) <= lenght_of_signs(b,filename):
        a = lenght_of_signs(b,filename)
    else:
        a = lenght_of_signs_in_name_of_column(a)
    return a


def display_menu():
    print("1. Show albums" + "\n"
            "2. Find by year" + "\n"
            "3. Find album by name" + "\n"
            "4. Find by genre" + "\n"
            "5. Find by artist" + "\n"
            "6. Show shortest/longest" + "\n"
            "7. Show report" + "\n"
            "8. Edit list of albums" + "\n"
            "9. Quit the program" + "\n"           
                )

def display_logo():
    print('''
     *                                                                    
   (  `                         (         (   (               )           
   )\))(     (      (           )\        )\  )\   (       ( /(      (    
  ((_)()\   ))\  (  )\   (    (((_)   (  ((_)((_) ))\  (   )\()) (   )(   
  (_()((_) /((_) )\((_)  )\   )\___   )\  _   _  /((_) )\ (_))/  )\ (()\  
  |  \/  |(_))( ((_)(_) ((_) ((/ __| ((_)| | | |(_))  ((_)| |_  ((_) ((_) 
  | |\/| || || |(_-<| |/ _|   | (__ / _ \| | | |/ -_)/ _| |  _|/ _ \| '_| 
  |_|  |_| \_,_|/__/|_|\__|    \___|\___/|_| |_|\___|\__|  \__|\___/|_|   
                                                                          
    ''')   

def display_edit_menu():
    print('''
1. Add new album to list
2. Edit existing album
3. Save new albums to external file
4. Go back to previous menu:
      
                ''')