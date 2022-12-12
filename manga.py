import os
import anaconda
def trend():
    os.system('cls')
    mangas= ["01. One Piece",
             "02. Chainsaw man",
             "03. One Punch Man",
             "04. Black Clover",
             "05. Spy x Family",
             "06. Kakkou no Iinazuke",
             "07. Yofukashi no Uta",
             "08. Jujutsu Kaisen",
             "09. Demon Slayer",
             "10. Yakusoku no Neverland"]
    print('\nTOP 10 Manga on the week')
    #masukan : list iteration
    # for i in mangas:
    for i in range(10):
        print(mangas[i])
    print("="*25)    
    detail = input("\ninfo detail nomor : ")
    if detail == '1':
        os.system('cls')
        infile = open("onepiece.txt")
        print(infile.read())
        infile.close()
    elif detail == '2':
        os.system('cls')
        infile = open("chainsaw.txt")
        print(infile.read())
        infile.close()
    elif detail == '3':
        os.system('cls')
        infile = open("opm.txt")
        print(infile.read())
        infile.close()
    elif detail == '4':
        os.system('cls')
        infile = open("blackclover.txt")
        print(infile.read())
        infile.close()
    elif detail == '5':
        os.system('cls')
        infile = open("spy.txt")
        print(infile.read())
        infile.close()
    elif detail == '6':
        os.system('cls')
        infile = open("kakkou.txt")
        print(infile.read())
        infile.close()
    elif detail == '7':
        os.system('cls')
        infile = open("yofukashi.txt")
        print(infile.read())
        infile.close()
    elif detail == '8':
        os.system('cls')
        infile = open("jujutsu.txt")
        print(infile.read())
        infile.close()
    elif detail == '9':
        os.system('cls')
        infile = open("demonslayer.txt")
        print(infile.read())
        infile.close()
    elif detail == '10':
        os.system('cls')
        infile = open("yakusoku.txt")
        print(infile.read())
        infile.close()
    else:
        os.system('cls')
        trend()
    
    balik = input("\nBack to menu? ")
    if balik == 'y' or 'Y':
        os.system('cls')
        anaconda.main_menu()

def search():
    os.system('cls')
    
    komik = {"action" : "Chainsawman\n"+ 
                        "One Punch Man\n"+
                        "Black Clover\n"+
                        "Spy x Family\n"+
                        "Jujutsu Kaisen\n"+
                        "Demon Slayer\n",
            "fantasy" : "One Piece\n"+
                        "Chainsawman\n"+ 
                        "Black Clover\n"+
                        "Yakusoku no Neverland\n"+
                        "Jujutsu Kaisen\n"+
                        "Demon Slayer\n",
            "romance" : "Kakkou no Iinazuke\n"+
                        "Yofukashi no Uta\n",
            "comedy"  : "One Piece\n"+
                        "One Punch Man\n"+
                        "Black Clover\n"+
                        "Spy x Family\n"+
                        "Kakkou no Iinazuke\n"+
                        "Yofukashi no Uta\n"}
    
    print('\n-- Search manga by genre --\n')
    genre= ["1. Action",
            "2. Fantasy",
            "3. Romance",
            "4. Comedy"]
    
    for i in range(4):
        print(genre[i])
    
    choose = input("\npilih : ")
    if choose == '1':
        os.system('cls')
        print("Action--")
        print(komik["action"])
        back()
      
    elif choose == '2':
        os.system('cls')
        print("Fantasy--")
        print(komik["fantasy"])
        back()
      
    elif choose == '3':
        os.system('cls')
        print("Romance--")
        print(komik["romance"])
        back()
      
    elif choose == '4':
        os.system('cls')
        print("Comedy--")
        print(komik["comedy"])
        back()
      
    else:
        os.system('cls')
        search()

def back():
      b = input('\nback? ')
      if b == 'y' and 'Y':
            os.system('cls')
            anaconda.main_menu()