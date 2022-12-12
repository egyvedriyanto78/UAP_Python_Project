import os
import manga 
from login import account

key = account

def main_menu():
    # membuat daftar menu
    print('=' * 40)
    print('Welcome to Anaconda Manga Corner')
    print('=' * 40)
    print('1. Trending Manga')
    print('2. Search Manga')
    print('3. Exit')
 
    # input pilihan
    pilihan = input('\npilih menu: ')
 
    # pilihan menu
    if pilihan == '1':
        manga.trend()
    elif pilihan == '2':
        manga.search()
    elif pilihan == '3':
        print('Program EXIT')
        exit()
    else:
        os.system('cls')
        main_menu()

# fungsi login
def get_login():
    while True:
        try:
            print('=' * 40)
            print('Login Anaconda Account')
            username = (input('username : ')).upper()
            password = int(input('password : '))
            os.system('cls')
            if username == key.uname and password == key.pw:
                break
        except:
            os.system('cls')
    os.system('cls')
    main_menu()

#masukan : menambahkan casting pada error handling, dan memasukkan tipe error nya , misal name error atay type error.

# main program
if __name__=='__main__':
    get_login()